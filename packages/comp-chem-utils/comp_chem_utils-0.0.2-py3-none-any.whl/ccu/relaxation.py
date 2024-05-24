import logging
from pathlib import Path

from ase import Atoms
from numpy.linalg import norm
from pymatgen.command_line.bader_caller import BaderAnalysis
from pymatgen.command_line.chargemol_caller import ChargemolAnalysis

logger = logging.getLogger(__name__)


def run_relaxation(
    atoms: Atoms, *, run_bader: bool = False, run_chargemol: bool = False
) -> None:
    """Run a relaxation calculation and log the output

    Args:
        atoms: An Atoms object with an attached calculator with which to run
            the relaxation calculation.
        run_bader: Whether or not to run Bader analysis afterwards.
        run_chargemol: Whether or not to run chargemol afterwards.
    """
    e = atoms.get_potential_energy()
    logger.info(f"final energy {e} eV")

    with Path("final.e").open(mode="x", encoding="utf-8") as file:
        file.write(f"{e}\n")

    forces = atoms.get_forces()

    if forces is not None:
        f = str(norm(max(forces, key=norm)))
        logger.info(f"max force {f} eV/Å")

    atoms.write("final.traj")

    if run_bader:
        _ = BaderAnalysis()
    if run_chargemol:
        _ = ChargemolAnalysis()
