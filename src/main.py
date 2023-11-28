from typing import Annotated
import typer

ccwc = typer.Typer()


@ccwc.command(
    "w",
    rich_help_panel="ccwc --{option} <filename>",
    help="Takes filename and outputs the number of words in a file.",
)
def wordCount(
    filename: Annotated[
        str,
        typer.Argument(),
    ] = None,
):
    with open(filename, "r") as file:
        data = file.read()
        word_count = len(data.split())
        typer.echo(f"Number of words in {filename}: {word_count}")


@ccwc.command(
    "c",
    rich_help_panel="ccwc --{option} <filename>",
    help="Takes filename and outputs the number of bytes in a file.",
)
def bytesCount(
    filename: Annotated[
        str,
        typer.Argument(),
    ] = None,
):
    with open(filename, "rb") as file:
        data = file.read()
        byte_count = len(data)
        typer.echo(f"Number of bytes in {filename}: {byte_count}")


@ccwc.command(
    "l",
    rich_help_panel="ccwc --{option} <filename>",
    help="Takes filename and outputs the number of lines in a file.",
)
def linesCount(
    filename: Annotated[
        str,
        typer.Argument(),
    ] = None,
):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        typer.echo(f"Number of lines in {filename}: {len(lines)}")


@ccwc.command(
    "m",
    rich_help_panel="ccwc --{option} <filename>",
    help="Takes filename and outputs the number of characters in a file.",
)
def characterCount(
    filename: Annotated[
        str,
        typer.Argument(),
    ] = None,
):
    with open(filename, "rb") as file:
        characters = file.read()
        count = 0
        for character in characters:
            if character != "\n":
                count += 1
    typer.echo(f"Number of characters in {filename}: {count}")


if __name__ == "__main__":
    ccwc()
