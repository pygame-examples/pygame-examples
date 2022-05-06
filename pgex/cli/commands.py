import click
import webbrowser
import importlib
import os
from typing import Optional
import pgex
from pgex.cli import output
from pgex.cli.styles import OutputStyle
from pgex.globals import USER_PATH


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    pass


@main.command(help="View example's source code on https://github.dev/")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def view(name: str) -> None:
    """
    View example's source code on https::/github.dev/
    
    Parameters:
        name: Name of the example.
    """
    if not name:
        example_names = os.listdir(
            USER_PATH + "/examples/"
        )
        output.list_options(OutputStyle.RAINBOW_BOX, example_names)

        try:
            n = int(input(": "))
            name = example_names[n]
        except ValueError:
            output.error(ValueError, "Input must be a number!", end=True)

    webbrowser.open(
        f"https://github.dev/Matiiss/pygame_examples/pgex/examples/blob/main/{name}/main.py"
    )


@main.command(help="Run an example")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def run(name: str) -> None:
    """
    Run an example on web or desktop.

    Parameters:
        nameL Name of the example.
    """
    if not name:
        example_names = os.listdir(USER_PATH + "/examples/")
        output.list_options(OutputStyle.RANDOM_PERIOD, example_names)

        try:
            n = int(input(": "))
            name = example_names[n]
        except ValueError:
            output.error(ValueError, "Input must be a number!", end=True)

    try:
        main = importlib.import_module(f"pgex.examples.{name}")
    except ImportError as err:
        click.echo(err)
        output.error(
            ImportError, "This example requires the above module to be installed."
        )
