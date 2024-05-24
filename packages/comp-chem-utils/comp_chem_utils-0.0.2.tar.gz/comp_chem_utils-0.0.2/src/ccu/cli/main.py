"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will
  cause problems: the code will get executed twice:

  - When you run `python -m ccu` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``ccu.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``ccu.__main__`` in ``sys.modules``.

  Also see (1) from https://click.palletsprojects.com/en/5.x/setuptools/
  #setuptools-integration
"""

import importlib

import click

import ccu

COMMANDS = (
    ("ccu.adsorption.cli", "adsorption"),
    ("ccu.bader.cli", "bader"),
    ("ccu.fancyplots.cli", "fed"),
    ("ccu.structure.cli", "structure"),
    ("ccu.thermo.cli", "thermo"),
)


@click.group(
    name="ccu",
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "-v",
    "--version",
    is_flag=True,
    default=False,
    help="Show the version and exit.",
)
def main(version):
    if version:
        click.echo(f"ccu-{ccu.__version__}")


def add_subcommands():
    for module, name in COMMANDS:
        command = importlib.import_module(module).main
        main.add_command(command, name=name)


add_subcommands()
