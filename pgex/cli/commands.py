"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Implements CLI commands
"""

import importlib
import webbrowser

import click

from pgex.cli import output
from pgex.cli.styles import OutputStyle
from pgex.globals import EXAMPLES_DIR


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    """
    main CLI function
    """


def _get_user_example_input(output_style: OutputStyle):
    """
    Shows available example options, prompts user for input
    """
    example_names = [i.name for i in EXAMPLES_DIR.iterdir()]
    output.list_options(output_style, example_names)

    try:
        return example_names[int(input(": "))]
    except ValueError:
        output.error(ValueError, "Input must be a number!", end=True)
    except IndexError:
        output.error(ValueError, "Input must within given range!", end=True)

    return ""


@main.command(help="View example's source code on https://github.dev/")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def view(name: str) -> None:
    """
    View example's source code on https::/github.dev/

    Parameters:
        name: Name of the example.
    """
    if not name:
        name = _get_user_example_input(OutputStyle.RAINBOW_BOX)

    webbrowser.open(
        "https://github.dev/Matiiss/"
        f"pygame_examples/pgex/examples/blob/main/{name}/main.py"
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
