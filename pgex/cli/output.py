from webbrowser import Error
import click
import enum
from pgex.cli.styles import OutputStyle
from typing import Iterable, Tuple
from colorama import Fore, Style


def list_options(output_style: OutputStyle, options: Iterable) -> None:
    for n, option in enumerate(options):
        output_prefix = output_style[0].replace("n", str(n))
        output_color = next(output_style[1])
        content = f"{output_color} {output_prefix} {option}"
        click.echo(content)
        print(Style.RESET_ALL, end="")


def error(ErrorType, msg, end=False) -> None:
    click.echo(f"{Fore.RED}{str(ErrorType)[8:-2]}: {msg}{Style.RESET_ALL}")

    if end:
        raise SystemExit
