from webbrowser import Error
import click
from typing import Iterable, Tuple
from colorama import Fore, Style
from pgex.cli.styles import OutputStyle


def list_options(output_style: OutputStyle, options: Iterable) -> None:
    """
    List options. 

    Parameters:
        output_style: Style in which output will be made.
        options: An iterable containing options to display.
    """
    for n, option in enumerate(options):
        output_prefix = output_style.value[0].replace("n", str(n))
        output_color = next(output_style.value[1])
        content = f"{output_color} {output_prefix} {option}"
        click.echo(content)
        print(Style.RESET_ALL, end="")


def error(error_type, msg, end=False) -> None:
    """
    Displays error in red text.

    Parameters:
        error_type: Given error to display.
        msg: Message to display with error.
        end: Whether or not the program should end after this error.
    """
    click.echo(f"{Fore.RED}{str(error_type)[8:-2]}: {msg}{Style.RESET_ALL}")

    if end:
        raise SystemExit
