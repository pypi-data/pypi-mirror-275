import os
from pathlib import PosixPath
from typing import Callable, List, Tuple, Union

import boto3
import botocore
from tqdm import tqdm

from radops.settings import settings

_s3 = None


def get_s3_client():
    global _s3
    if _s3 is not None:
        return _s3
    if not settings.local_mode:
        _s3 = boto3.client(
            "s3",
            endpoint_url=settings.s3_endpoint_url,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key.get_secret_value(),
            region_name="auto",
        )
        try:
            _s3.create_bucket(Bucket=settings.bucket_name)
        except (
            _s3.exceptions.BucketAlreadyOwnedByYou,
            botocore.exceptions.ClientError,
        ):
            pass

    else:
        _s3 = None

    return _s3


def upload_file_to_s3(
    path: Union[str, PosixPath], object_name: str, metadata: dict = None
):
    file_size = os.stat(path).st_size

    with tqdm(
        total=file_size, unit="B", unit_scale=True, desc=f"Uploading {path}"
    ) as pbar:
        args = (path, settings.bucket_name, object_name)
        kwargs = {
            "Callback": lambda bytes_transferred: pbar.update(
                bytes_transferred
            )
        }
        if metadata is not None:
            kwargs["ExtraArgs"] = {"Metadata": metadata}

        get_s3_client().upload_file(*args, **kwargs)


def download_file_from_s3(object_name: str, out_path: Union[str, PosixPath]):
    bucket = settings.bucket_name

    object_size = get_s3_client().head_object(Bucket=bucket, Key=object_name)[
        "ContentLength"
    ]

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with tqdm(
        total=object_size,
        unit="B",
        unit_scale=True,
        desc=f"Downloading {object_name}",
    ) as pbar:
        get_s3_client().download_file(
            bucket,
            object_name,
            out_path,
            Callback=lambda bytes_transferred: pbar.update(bytes_transferred),
        )
    return out_path


def delete_file_from_s3(object_name: str):
    get_s3_client().delete_object(Bucket=settings.bucket_name, Key=object_name)


def file_exists_in_s3(object_name: str) -> bool:
    s3 = get_s3_client()
    if s3 is None:
        return False
    try:
        s3.head_object(Bucket=settings.bucket_name, Key=object_name)
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            return False
        raise e

    return True


def list_files_in_s3(
    filterer: Callable[[str], bool] = None, Prefix: str = ""
) -> List[str]:
    """Get all files in s3, potentially those satisfying a filter

    Parameters
    ----------
    filterer
        function that takes in a uid (i.e. object key) and returns whether or not
        that should be included

    Returns
    -------
    list of uids (i.e. object keys)
    """
    filterer = filterer or (lambda _: True)
    MaxKeys = 1000
    ret = []

    # AWS has a limit returned objects on each call so we may have to make multiple
    objs = get_s3_client().list_objects_v2(
        Bucket=settings.bucket_name, MaxKeys=MaxKeys, Prefix=Prefix
    )
    while True:
        if "Contents" not in objs:
            break
        ret.extend(
            [obj["Key"] for obj in objs["Contents"] if filterer(obj["Key"])]
        )
        if not objs.get("IsTruncated", False):
            break

        next_marker = objs.get("NextContinuationToken", None)
        if next_marker is None:
            break

        objs = get_s3_client().list_objects_v2(
            Bucket=settings.bucket_name,
            MaxKeys=MaxKeys,
            ContinuationToken=next_marker,
        )
    return ret


def list_files_and_folders(base_folder="") -> Tuple[List[str], List[str]]:
    """
    Parameters
    ----------
    base_folder
        folder to start with

    Returns
    -------
    first item in the tuple is a list of all the files in the folder and the second
    is a list of subfolders
    """
    if base_folder and not base_folder.endswith("/"):
        base_folder += "/"

    response = get_s3_client().list_objects_v2(
        Bucket=settings.bucket_name, Prefix=base_folder, Delimiter="/"
    )

    file_paths = []

    # Add files under the specified prefix
    if "Contents" in response:
        for obj in response["Contents"]:
            file_paths.append(obj["Key"])

    # Recursively add files under subfolders
    if "CommonPrefixes" in response:
        folders = [cp["Prefix"] for cp in response["CommonPrefixes"]]
    else:
        folders = []

    def _make_relative(paths):
        return [os.path.relpath(p, base_folder) for p in paths]

    file_paths = _make_relative(file_paths)
    folders = _make_relative(folders)

    return file_paths, folders


def create_presigned_url(object_name: str, expiration: int) -> str:
    """Create a pre-signed url

    Parameters
    ----------
    object_name
        object to generate a pre-signed url for
    expiration
        number of seconds until the url expires
    """
    return get_s3_client().generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": settings.bucket_name, "Key": object_name},
        ExpiresIn=expiration,
    )


def delete_folder_from_s3(folder: str):
    """Deletes a folder and everything (recursively) within it, including subfolders."""
    if folder[-1] == "/":
        folder = folder[:-1]
    files, folders = list_files_and_folders(folder)
    for f in files:
        delete_file_from_s3(f"{folder}/{f}")
    for f in folders:
        delete_folder_from_s3(f"{folder}/{f}")


def is_folder(path: str) -> bool:
    """Check if a path is a folder"""
    files, _ = list_files_and_folders(path)
    return len(files) > 0
