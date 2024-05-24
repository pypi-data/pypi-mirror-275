from pathlib import Path

import click

from ccu.fancyplots.gui.main import run


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "--cache",
    type=click.Path(path_type=Path),
    help="Load fancyplots with a cached session.",
)
@click.option(
    "--data",
    type=click.Path(path_type=Path),
    help="Initialize fancyplots with free energy diagram data.",
)
@click.option(
    "--style",
    type=click.Path(path_type=Path),
    help="Specify a style file.",
)
def main(cache: Path, data: Path, style: Path):
    """Launches fancyplots GUI"""
    run(cache=cache)
