"""This module contains the ccu.structure package CLI logic."""

import pathlib

import click

from ccu.adsorption import adsorbatecomplex
from ccu.adsorption.adsorbates import ALL


@click.group()
def main():
    """Adsorption calculation tools."""


@main.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.argument(
    "adsorbate",
    type=click.Choice(list(ALL.keys()), case_sensitive=False),
    required=True,
)
@click.argument(
    "structure",
    required=True,
    type=click.Path(exists=True, path_type=pathlib.Path),
)
@click.argument(
    "destination",
    default=pathlib.Path.cwd(),
    type=click.Path(file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "-s",
    "--separation",
    help="how far the adsorbate should be placed from the surface",
    default=1.8,
    type=float,
)
@click.option(
    "-c",
    "--special-centres",
    help=(
        "whether or not the adsorbate will be placed using "
        "atom-centred placement"
    ),
    flag_value=True,
    is_flag=True,
)
@click.option(
    "-Y",
    "--symmetric",
    help="whether or not the adsorbate is to be treated as symmetric",
    flag_value=True,
    is_flag=True,
)
@click.option(
    "-V",
    "--vertical",
    help=(
        "whether or not vertical adsorption configurations are to "
        "be generated"
    ),
    flag_value=True,
    is_flag=True,
)
def place_adsorbate(
    adsorbate,
    structure,
    destination,
    separation,
    special_centres,
    symmetric,
    vertical,
):
    """Creates adsorbate-surface complexes for adsorption configurations on a
    given structure and writes them to a .traj file.

    Args:
        ADSORBATE is the name of the adsorbate to place on the surface.
        STRUCTURE is the path to the surface on which the adsorbate will be
            placed.
        DESTINATION is the directory in which to write the .traj files. The
            directory is created if it does not exist. Defaults to the current
            working directory.
    """
    complexes = adsorbatecomplex.run(
        adsorbate,
        structure,
        destination,
        separation,
        special_centres,
        symmetric,
        vertical,
    )
    print(f"{len(complexes)} complexes created.")
