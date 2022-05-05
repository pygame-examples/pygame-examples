import click
import webbrowser
from typing import Optional
import os
from os import listdir
import pgex
from pgex.cli import output
from pgex.cli.styles import OutputStyle
from pgex.utils import user_path
import importlib


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    pass


@main.command(help="View example's source code on https://github.dev/")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def view(name: str) -> None:
    if not name:
        example_names = os.listdir(
            user_path + "/examples/"
        )  # + [f"dummy{n}" for n in range(7)]
        output.list_options(OutputStyle.RAINBOW_BOX, example_names)

        try:
            n = int(input(": "))
        except ValueError:
            output.error(ValueError, "Input must be a number!")

        name = example_names[n]

    webbrowser.open(
        f"https://github.dev/Matiiss/pygame_examples/pgex/examples/blob/main/{name}/main.py"
    )


@main.command(help="Run an example")
@click.option("--name", "-n", is_flag=False, flag_value="", help="Name of the example")
def run(name: str) -> None:
    if not name:
        example_names = os.listdir(user_path + "/examples/")
        output.list_options(OutputStyle.RANDOM_PERIOD, example_names)

        try:
            n = int(input(": "))
        except ValueError:
            output.error(ValueError, "Input must be a number!", end=True)

        name = example_names[n]

    try:
        main = importlib.import_module(f"pgex.examples.{name}.main")
    except ImportError as err:
        click.echo(err)
        output.error(
            ImportError, "This example requires the above module to be installed."
        )
