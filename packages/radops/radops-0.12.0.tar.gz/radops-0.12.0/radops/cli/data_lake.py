import os
from typing import Optional

import rich
import typer
from rich.text import Text
from typing_extensions import Annotated

from radops.data_lake import (
    File,
    add_from_url,
    add_local_file,
    get_local_path,
    get_unsynced_files,
    list_local_files,
)
from radops.data_lake.cloud_ops import (
    create_presigned_url,
    delete_folder_from_s3,
    file_exists_in_s3,
    is_folder,
    list_files_and_folders,
)

from .common import _y_n_prompt_loop

app = typer.Typer()


@app.command(name="ls")
def ls(folder: Annotated[Optional[str], typer.Argument()] = ""):
    """list all files in the datalake"""
    local_files = list_local_files()

    def _style(c):
        return "b" if os.path.join(folder, c) in local_files else "i"

    files, folders = list_files_and_folders(folder)
    folders = [Text(f"{f}/", style="yellow") for f in folders]
    files = [Text(f, style=f"{_style(f)} green") for f in files]

    rich.print(*(folders + files), sep="\t")


@app.command(name="purge-local-storage")
def purge_local_storage():
    unsynced_files = get_unsynced_files()
    for uid in unsynced_files:
        os.remove(get_local_path(uid))

    rich.print(f"Removed files {unsynced_files} from local storage.")


@app.command(name="info")
def info(uid: str):
    """display the info and lineage of the specified file"""
    f = File(uid)
    if not f.exists_in_cloud():
        rich.print(f"[red]File {uid} does not exist in the data lake.")
    else:
        f.print_info()


@app.command(name="add")
def add(
    path_or_url: str,
    uid: str,
    move: bool = False,
    copy: bool = False,
    recursive: Annotated[bool, typer.Option("--recursive", "-r")] = False,
):
    if move and copy:
        rich.print("[red]Cannot set both --move and --copy")
        raise typer.Exit()
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        if move or copy:
            rich.print(
                "[red]Cannot use '--move' or '--copy' when adding a file from a url."
            )
            raise typer.Exit()
        add_from_url(url=path_or_url, output_uid=uid)
    else:
        if not os.path.exists(path_or_url):
            rich.print(
                f"[red] File {path_or_url} does not exist. First argument to `datalake add` must be"
                " either a url (starting with 'http' or 'htttps') or a local file."
            )
            raise typer.Exit()
        if (not move) and (not copy):
            while True:
                resp = typer.prompt(
                    "Enter 'move' if local file should be moved to local storage or 'copy' if it should be copied"
                )
                if resp not in ["move", "copy"]:
                    rich.print("[yellow]Invalid response")
                else:
                    break
            copy = resp == "copy"

        if os.path.isdir(path_or_url):
            if not recursive:
                rich.print(
                    f"`{path_or_url} is a directory. Use --recursive / -r to add all files in it."
                )
                raise typer.Exit()

            # iterate through all files including in subfolders
            for root, _, files in os.walk(path_or_url):
                for fname in files:
                    output_uid = os.path.join(
                        uid,
                        os.path.relpath(
                            os.path.join(root, fname), path_or_url
                        ),
                    )

                    add_local_file(
                        path=os.path.join(root, fname),
                        output_uid=output_uid,
                        copy=copy,
                    )

        else:
            add_local_file(path=path_or_url, output_uid=uid, copy=copy)


@app.command(name="delete")
def delete(
    uid: str,
    recursive: Annotated[bool, typer.Option("--recursive", "-r")] = False,
):
    """deletes a file from the datalake (both local and in the cloud)"""
    if is_folder(uid):
        if not recursive:
            rich.print(
                f"[yellow]The file [blue]{uid}[/blue] is a folder. Use --recursive / -r to delete all files in it."
            )
            raise typer.Exit()
        _y_n_prompt_loop(
            f"Are you sure you want to delete the folder[blue]{uid}[/blue] and all of its contents?"
        )
        delete_folder_from_s3(uid)
        rich.print(
            f"Succesfully deleted folder [blue]{uid}[/blue] and all of its contents."
        )
        return

    f = File(uid)
    downstream_uids = f.get_all_downstream()
    if len(downstream_uids) != 0:
        _y_n_prompt_loop(
            f"The file {uid} has the following downstream dependencies: {downstream_uids}. "
            "Deleting will delete all of these. Continue?"
        )

    if not f.exists_in_cloud() and not f.exists_locally():
        rich.print(f"[yellow]File [blue]{uid}[/blue] is not in the datalake.")
        raise typer.Exit()
    deleted = f.delete(cascade=True)
    rich.print(f"Succesfully deleted file(s) {deleted}")


@app.command(name="delete-local")
def delete_local(uid: str):
    """deletes a file from local storage (but not from the cloud)"""
    f = File(uid)
    if not f.exists_locally():
        rich.print(f"[yellow]File [blue]{uid}[/blue] does not exist locally.")
        raise typer.Exit()
    f.delete_local()
    rich.print(
        f"Succesfully deleted file [blue]{uid}[/blue] from local storage."
    )


@app.command(name="local-path")
def local_path(uid: str):
    local_path = File(uid).storage_path
    if not file_exists_in_s3(uid):
        rich.print(f"[yellow]File `{uid}` is not in the datalake.")
    elif local_path.exists():
        rich.print(local_path)
    else:
        rich.print(
            f"[yellow]File [blue]{uid}[/blue] has not been downloaded. You can do this by running[/yellow]: ",
            f"radops datalake download {uid}",
        )


@app.command(name="download")
def download(uid: str):
    f = File(uid)
    if not f.exists_in_cloud():
        rich.print(f"[yellow]File [blue]{uid}[/blue] is not in the datalake.")
        raise typer.Exit()
    elif f.exists_locally():
        rich.print(f"[yellow]File [blue]{uid}[/blue] already exists locally.")
        raise typer.Exit()
    return File(uid).download_from_cloud()


@app.command(name="presigned-url")
def presigned_url(
    uid: str,
    expiration: Annotated[
        int,
        typer.Argument(
            help="the expiration time in seconds. defaults to 3600 (1 hour)"
        ),
    ] = 60
    * 60,
):
    """create a presigned url for a file. this allows sharing a file with someone
    who does not have access to the data lake.
    """
    url = create_presigned_url(uid, expiration)
    rich.print(f"Presigned url: {url}, set to expire in {expiration} seconds.")
