"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Defines utility funtions help with CLI outputs
"""

from typing import Iterable, Optional

import click
from colorama import Fore, Style
import colorama
import os

from pgex.cli.styles import OutputStyle


def list_options(output_style: OutputStyle, options: Iterable, highlight_index: Optional[int] = None) -> None:
    """
    List options.

    Parameters:
        output_style: Style in which output will be made.
        options: An iterable containing options to display.
    """

    for i, option in enumerate(options):
        output_prefix = output_style.value[0].replace("n", str(i))
        output_color = output_style.value[1][i]
        content = f"{output_color} {output_prefix} {option}"

        if highlight_index is not None and highlight_index == i:
            content = f"> {output_color} {output_prefix} {option}"
        click.echo(content + Style.RESET_ALL)


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


def color_output(msg: str, color) -> None:
    """
    Function that outputs message in given color, and resets
    the terminal color.

    Parameters:
        msg: Message to echo.
        color: Color to echo message in.
    """
    click.echo(f"{color}{msg}{colorama.Style.RESET_ALL}")

def cls():
    """
    Cross platform function to clear console.
    """
    os.system('cls||clear')
