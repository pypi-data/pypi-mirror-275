"""Fancy plots GUI"""

import json
import logging
from pathlib import Path
import tkinter as tk

# import tkinter.ttk as ttk
from tkinter import messagebox

from ccu.fancyplots.gui.annotation import AnnotationSection
from ccu.fancyplots.gui.fed import FreeEnergyDiagram
from ccu.fancyplots.gui.footer import FooterSection
from ccu.fancyplots.gui.mechanism import MechanismSection
from ccu.fancyplots.gui.mechanism import MechanismWindow
from ccu.fancyplots.gui.parameters import bind_functions
from ccu.fancyplots.gui.parameters import make_formatting_entries
from ccu.fancyplots.gui.parameters import pack_entries
from ccu.fancyplots.gui.root import Root
from ccu.fancyplots.gui.text import show_text_def

logger = logging.getLogger(__name__)


def initialize_windows(windows: dict[str, tk.Tk | None]) -> None:
    """Initialize windows

    Args:
        windows: A dictionary mapping names to `tk.Tk`s and containing the root window.
    """
    windows["energy_window"] = None
    windows["graph_window"] = None
    windows["reorder"] = None
    windows["tight_layout"] = None
    windows["instructions_window"] = None
    windows["matplotlib_palette"] = None


def update_settings(
    dictionary: dict[str, int | str | tk.Entry | tk.Label],
    parameters: list[str],
) -> None:
    """Update tk.Entry values using parameter values.

    This function modifies the `tk.Entry`s in `dictionary`.

    Args:
        dictionary: A parameter dictionary containing `tk.Entry`s.
        parameters: A dictionary mapping parameter names to values that will be used to update `dictionary`.
    """
    for value in dictionary.values():
        if isinstance(value, tk.Entry):
            value.delete(0, tk.END)

    for parameter in parameters:
        name, value = parameter.split("=")
        if name == "visual":
            pass
        else:
            entry = dictionary[name]
            entry.insert(0, value)


def load_cache(
    cache: Path,
    param_dict: dict[str, int | str | tk.Entry | tk.Label],
    add_text_dict: dict[int, list[str]],
    annotation_section: AnnotationSection,
    mechanism_section: MechanismSection,
    paths_dict: dict[str, float | str],
    windows: dict[str, tk.Tk | None],
    full_pathway: list[str],
) -> None:
    """Load FancyPlots data from a saved cache file.

    Args:
        cache: The filename from which to read.
        param_dict: _description_
        add_text_dict: _description_
        annotation_section: _description_
        mechanism_section: _description_
        paths_dict: _description_
        windows: _description_
        full_pathway: _description_
    """
    try:
        with cache.open(mode="r", encoding="utf-8") as file:
            all_unpacked = json.load(file)

        if len(all_unpacked) != 5:
            messagebox.showwarning(
                "Cache Warning!",
                f"File '{cache}' has wrong format. It will be ignored.",
            )
        else:
            unpickled_parameters = all_unpacked[0]
            unpickled_full_pathway = all_unpacked[1]
            unpickled_list_dicts = all_unpacked[2]
            unpickled_labelling = all_unpacked[3]
            unpickled_text = all_unpacked[4]
            update_settings(param_dict, unpickled_parameters)

            # Additional Text
            for index, value in enumerate(unpickled_text):
                text_params = list(value)
                add_text_dict[index + 1] = text_params

            show_text_def(
                annotation_section.number_text,
                add_text_dict,
                annotation_section.add_text_widget,
                annotation_section.add_text_x,
                annotation_section.add_text_y,
                annotation_section.add_text_color,
                annotation_section.add_text_fontsize,
            )

            # Mechanism
            mechanism_section.npaths_var.set(len(unpickled_list_dicts))
            mechanism_section.full_pathway_names.insert(
                0, ",".join(unpickled_full_pathway)
            )

            for index, dictionary in enumerate(unpickled_list_dicts):
                for name, value in dictionary.items():
                    paths_dict[f"Pathway {index+1}_{name}"] = value
                paths_dict[f"Pathway {index+1}-legendlabel"] = (
                    unpickled_labelling[index]
                )

            MechanismWindow.define_free_energies(
                full_pathway,
                mechanism_section.full_pathway_names,
                mechanism_section.npaths_var,
                paths_dict,
                windows,
            )
    except json.JSONDecodeError:
        messagebox.showwarning(
            "Cache Warning!",
            f"File '{cache}' could not be opened - It either is not a ."
            "fancy file or it was damaged. It will be ignored.",
        )


def run(*, cache: Path | None = None) -> None:
    """GUI Logic"""
    # A dictionary mapping names to `tk.Tk`s and containing the root window
    windows: dict[str, tk.Tk | None] = {}
    root = Root()
    windows["root"] = root
    root.configure_window(windows)
    initialize_windows(windows)

    matplotlib_params = {}

    # A dictionary containing all figure formatting parameters, `tk.Entry`s, and `tk.Label`s
    param_dict: dict[str, int | str | tk.Entry | tk.Label] = {}

    # Free energy diagram parameters (e.g., parameter=value) constructed from `params_dict`
    parameters: list[str] = []

    # A list of strings, each string representing a step in a pathway
    full_pathway = []

    # Free energies & legend labels for each step in each pathway in the mechanism
    # e.g., Pathway 1_a: 0, Pathway 1-legendlabel
    paths_dict: dict[str, float | str] = {}

    # A dictionary mapping integers to lists of strings specifying additional text/formatting
    add_text_dict: dict[int, list[str]] = {}

    # `add_text_dict` but flat and with x/y coordinates as floats
    add_text: list[list[float | str]] = []

    execution = {}

    images = [None, None]

    # Parameters
    tk.Label(
        windows["root"], text="Parameters", font="Helvetica 11 bold"
    ).grid(row=1, column=1, columnspan=30)
    tk.Label(windows["root"], text="").grid(row=2, column=1)  # empty line
    make_formatting_entries(windows, param_dict)
    pack_entries(param_dict)

    mechanism_section = MechanismSection(
        windows=windows,
        full_pathway=full_pathway,
        paths_dict=paths_dict,
        param_dict=param_dict,
        parameters=parameters,
        matplotlib_params=matplotlib_params,
        execution=execution,
        add_text_dict=add_text_dict,
        add_text=add_text,
    )

    FreeEnergyDiagram.set_default_settings(
        param_dict=param_dict,
        parameters=parameters,
        paths_dict=paths_dict,
        full_pathway=full_pathway,
        windows=windows,
        matplotlib_params=matplotlib_params,
        execution=execution,
        add_text_dict=add_text_dict,
        add_text=add_text,
    )

    bind_functions(
        param_dict,
        parameters,
        paths_dict,
        full_pathway,
        windows,
        matplotlib_params,
        execution,
        add_text_dict,
        add_text,
    )
    tk.Label(windows["root"], text="").grid(row=11, column=1)

    annotation_section = AnnotationSection(
        root,
        windows.get("graph_window"),
        full_pathway,
        paths_dict,
        param_dict,
        parameters,
        matplotlib_params,
        execution,
        add_text_dict,
    )

    _ = FooterSection(
        param_dict=param_dict,
        parameters=parameters,
        paths_dict=paths_dict,
        full_pathway=full_pathway,
        windows=windows,
        matplotlib_params=matplotlib_params,
        execution=execution,
        add_text_dict=add_text_dict,
        add_text=add_text,
        images=images,
    )

    if cache and cache.exists():
        load_cache(
            cache=cache,
            param_dict=param_dict,
            add_text_dict=add_text_dict,
            annotation_section=annotation_section,
            mechanism_section=mechanism_section,
            paths_dict=paths_dict,
            windows=windows,
            full_pathway=full_pathway,
        )

    root.mainloop()


if __name__ == "__main__":
    run()
