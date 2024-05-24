import logging
from typing import Literal
from typing import TextIO

import click

from ccu.thermo import chempot_calculator
from ccu.thermo.gibbs import DEFAULT_PRESSURE
from ccu.thermo.gibbs import DEFAULT_TEMPERATURE
from ccu.thermo.gibbs import calculate_free_energy

logger = logging.getLogger()

DEFAULT_APPROXIMATION = "HARMONIC"


@click.group()
def main():
    """Thermochemistry tools."""


def _name_energy_file() -> TextIO:
    """Name the energy file based on the approximation"""
    prefix = "harmonic"
    if ctx := click.get_current_context(silent=True):
        prefix = ctx.params.get("approximation", "") or prefix

    return f"{prefix.lower()}_free_energy.e"


def report_state(ctx: click.Context) -> None:
    logger.debug("Parameters and Sources".center(80, "-"))
    for k, v in ctx.params.items():
        value = getattr(v, "name", str(v))
        logger.debug(f"{k}={value} from {ctx.get_parameter_source(k).name}")


@main.command(
    "gibbs",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    default=0,
    count=True,
    help="Controls the verbosity. 0: Show messages of level warning and "
    "higher. 1: Show messages of level info and higher. 2: Show all messages"
    "-useful for debugging.",
    show_default=True,
)
@click.option(
    "-T",
    "--transition-state",
    is_flag=True,
    default=False,
    help=(
        "Assume that the system is a transition state when calculating the "
        "free energy of the system. One imaginary vibrational mode "
        "(corresponding to the reaction coordinate) will be discarded."
    ),
    show_default=True,
)
@click.option(
    "-S",
    "--solution-phase",
    "frequency_threshold",
    default=False,
    flag_value=100,
    help=(
        "Assume that the system is in solution when calculating the free "
        "energy of the system. When activated, low vibrations are "
        "shifted to 100 cm^-1; otherwise, low vibrations are shifted to "
        "12 cm^-1."
    ),
    show_default=True,
)
@click.option(
    "--frequency-threshold",
    "frequency_threshold",
    default=12,
    help=(
        "All vibrations less than this value will be shifted to this "
        "value. Units in cm^-1."
    ),
    hidden=True,
)
@click.option(
    "--ideal-gas",
    "approximation",
    is_eager=True,
    flag_value="IDEAL_GAS",
    help=(
        "Use the ideal gas limit to calculate the free energy. With N "
        "atoms, 3N - 6 vibrational modes will be considered (3N - 5 "
        "if the '--linear' flag is provided)."
    ),
    show_default=True,
)
@click.option(
    f"--{DEFAULT_APPROXIMATION.lower()}",
    "approximation",
    default=True,
    is_eager=True,
    flag_value=DEFAULT_APPROXIMATION,
    help=(
        f'Use the {DEFAULT_APPROXIMATION.lower().replace("_", " ")} limit to '
        'calculate the free energy. All vibrational modes will be considered.'
    ),
    show_default=True,
)
@click.option(
    "-Y",
    "--symmetry",
    default=1,
    help=(
        "Specify the symmetry number of the system. Note that this is only "
        "relevant under the ideal gas approximation."
    ),
    show_default=True,
)
@click.option(
    "--linear",
    "geometry",
    flag_value="linear",
    help=(
        "Specify that the system is linear. Note that this is only "
        "relevant under the ideal gas approximation."
    ),
    show_default=True,
)
@click.option(
    "--non-linear",
    "geometry",
    default=True,
    flag_value="nonlinear",
    help=(
        "Specify that the system is nonlinear. Note that this is only "
        "relevant under the ideal gas approximation."
    ),
    show_default=True,
)
@click.option(
    "-t",
    "--temperature",
    default=DEFAULT_TEMPERATURE,
    help="Specify the temperature (in Kelvin).",
    show_default=True,
)
@click.option(
    "-p",
    "--pressure",
    default=DEFAULT_PRESSURE,
    help=(
        "Specify the temperature (in bar). Note that this is only applicable for "
        "the ideal gas approximation."
    ),
    show_default=True,
)
@click.option(
    "-s",
    "--spin",
    default=0,
    help=(
        "Specify the spin. Note that this is only relevant for the gas-phase "
        "approximation."
    ),
    show_default=True,
)
@click.option(
    "--atoms-file",
    default="in.traj",
    help=(
        "The name of the file containing the structure corresponding to the "
        "vibrational frequencies. Note that this is only used in the ideal "
        "gas approximation."
    ),
    show_default=True,
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "--dg-file",
    default="dg_ase.log",
    help=("The name of the file in which the save the quantity dG + ZPVE."),
    show_default=True,
    type=click.File(mode="w", encoding="utf-8"),
)
@click.option(
    "--freq-file",
    default="gibbs_freq_used.txt",
    help=(
        "The name of the file in which to save the frequencies used to "
        'calculate the free energy. Use "-" to print to the standard output.'
    ),
    show_default=True,
    type=click.File(mode="w", encoding="utf-8"),
)
@click.option(
    "--vib-file",
    default="vib.txt",
    help=(
        "The name of the file from which to read the frequencies used to "
        "calculate the free energy."
    ),
    show_default=True,
    type=click.File(mode="r", encoding="utf-8"),
)
@click.option(
    "--log-file",
    default="free_energy.log",
    help=(
        "The name of the file in which to save all the information used to "
        'calculate the free energy. Use "-" to print to the standard output.'
    ),
    type=click.File(mode="w", encoding="utf-8"),
)
@click.option(
    "--energy-file",
    default=_name_energy_file,
    help=(
        'The name of the file in which to save the free energy. Use "-" to print to the standard output.'
    ),
    type=click.File(mode="w", encoding="utf-8"),
)
@click.pass_context
def gibbs(
    ctx: click.Context,
    verbosity: int,
    transition_state: bool,
    frequency_threshold: float,
    approximation: Literal["IDEAL_GAS", "HARMONIC"],
    symmetry: int,
    geometry: Literal["linear", "nonlinear"],
    temperature: float,
    pressure: float,
    spin: int,
    atoms_file: str,
    dg_file: TextIO,
    freq_file: TextIO,
    vib_file: TextIO,
    log_file: TextIO,
    energy_file: TextIO,
) -> None:
    """Calculate the free energy of a system"""
    match verbosity:
        case 0:
            level = logging.WARNING
        case 1:
            level = logging.INFO
        case _:
            level = logging.DEBUG

    logging.basicConfig(stream=log_file, level=level)

    if energy_file is None:
        energy_file = f"{approximation.lower()}_free_energy.e"

    report_state(ctx=ctx)

    delta_g, zpve, frequencies = calculate_free_energy(
        log_file=log_file,
        vib_file=vib_file,
        approximation=approximation,
        symmetry=symmetry,
        geometry=geometry,
        transition_state=transition_state,
        frequency_threshold=frequency_threshold,
        temperature=temperature,
        pressure=pressure,
        spin=spin,
        atoms_file=atoms_file,
    )
    _ = energy_file.write(str(delta_g + zpve))
    logger.info(f"Free energy written to {energy_file.name}")
    _ = dg_file.write(str(delta_g))
    logger.info(
        f"{approximation.capitalize().replace('_', ' ')} free energy written "
        f"to {dg_file.name}"
    )
    header = "Frequencies used for Gibbs Free energy calculation".center(
        80, "-"
    )
    freq_lines = [
        f"{header}\n",
        *[f"{freq}\n" for freq in frequencies],
        "-" * 80,
    ]
    _ = freq_file.writelines(freq_lines)
    logger.info(f"Frequencies written to {freq_file.name}")
    click.echo(f"Free energy: {delta_g + zpve}")


@main.command("chempot-calculator")
def chempot() -> None:
    chempot_calculator.main()
