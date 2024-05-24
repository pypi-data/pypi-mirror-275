# Keys: legend entries, pathway names
# Values: energies for each step
from dataclasses import dataclass
from typing import TypedDict

FEDData = dict[str, list[float | None]]


@dataclass
class FormattingParameters:
    boxsize: tuple[float, float] = (6.0, 4.5)
    font: str = "Sans Serif"
    fontsize: float = 14
    markeredgewidth: float = 0.3
    markersize: int = 7
    linewidth: float = 1.5

    xscale: float | None = None
    yscale: float | None = None
    tick_loc: str = "out"
    tick_dec: float = 2.0
    tick_min: float = 1.0
    tick_double: bool = False
    legend_loc: str = "best"
    xlabel: str = "Reaction Coordinate"
    ylabel: str = "$\\Delta$G / eV"
    colors: tuple[str, ...] = ("black", "blue", "red", "lime", "fuschia")

    visual: bool = True
    savename: str = "fed.svg"
    dpi: int = 1200
    title: str = "Fancy Plots GUI"


class FancyCache(TypedDict):
    style_parameters: FormattingParameters
    pathways: FEDData
