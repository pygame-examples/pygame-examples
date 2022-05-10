"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Implements CLI commands
"""

import importlib
import webbrowser

import click
import colorama
import keyboard

from pgex.cli import output
from pgex.cli.styles import OutputStyle
from pgex.common import EXAMPLES_DIR


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    """
    main CLI function
    """


def _get_sublists(lst, n):
    """
    Given a list of multiple elements, convert this
    into a list of multiple sublists each containing n number of elements
    from the original list in order.
    The last sublist may not contain the same number of elements/contain the excess elements.

    Parameters:
        lst: List to create sublists out of.
        n: Maximum size of sublist.
    """
    return [lst[i * n : i * n + n] for i in range(-(-len(lst) // n))]


def _get_user_example_input(output_style: OutputStyle):
    """
    Shows available example options, prompts user for input

    Parameters:
        output_style: Styling used for output.
    """
    MAX_INDEX = 8
    page_index = 0

    example_names = _get_sublists(
        [i.name for i in EXAMPLES_DIR.iterdir()], MAX_INDEX + 1
    )
    MAX_PAGE_INDEX = len(example_names) - 1
    highlight_index = [0 for _ in range(MAX_PAGE_INDEX + 1)]
    output.list_options(output_style, example_names[page_index])
    while True:
        output.cls()
        print(highlight_index)
        click.echo("Enter 'ctrl + c' to quit.")
        click.echo("Use arrow keys to move.\n")

        output.color_output(
            f"\t Page {page_index}/{MAX_PAGE_INDEX}\n", colorama.Fore.LIGHTRED_EX
        )
        output.list_options(
            output_style, example_names[page_index], highlight_index[page_index]
        )

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":
                highlight_index[page_index] -= 1
                if highlight_index[page_index] < 0:
                    highlight_index[page_index] = MAX_INDEX
            elif event.name == "down":
                highlight_index[page_index] += 1
                if highlight_index[page_index] > MAX_INDEX:
                    highlight_index[page_index] = 0
            elif event.name == "right":
                page_index += 1
                if page_index > MAX_PAGE_INDEX:
                    page_index = 0

            elif event.name == "left":
                page_index -= 1
                if page_index < 0:
                    page_index = MAX_PAGE_INDEX

            elif event.name == "enter":
                break

    return example_names[page_index][highlight_index[page_index]]


@main.command(help="View example's source code on https://github.com/")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def view(name: str) -> None:
    """
    View example's source code on https::/github.com/

    Parameters:
        name: Name of the example.
    """
    if not name:
        name = _get_user_example_input(OutputStyle.RAINBOW_BOX)

    webbrowser.open(
        "https://github.com/Matiiss/"
        f"pygame_examples/tree/main/pgex/examples/{name}"
    )


@main.command(help="Run an example")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def run(name: str) -> None:
    """
    Run an example on web or desktop.

    Parameters:
        name: Name of the example.
    """
    if not name:
        name = _get_user_example_input(OutputStyle.RANDOM_PERIOD)

    try:
        importlib.import_module(f"pgex.examples.{name}")
    except ImportError as err:
        click.echo(err)
        output.error(
            ImportError, "This example requires the above module to be installed."
        )
