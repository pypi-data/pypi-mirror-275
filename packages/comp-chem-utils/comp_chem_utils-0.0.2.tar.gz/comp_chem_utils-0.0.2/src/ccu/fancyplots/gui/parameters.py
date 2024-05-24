from functools import partial
import tkinter as tk

from ccu.fancyplots.gui.fed import FreeEnergyDiagram
from ccu.fancyplots.gui.tooltip import create_tooltip
from ccu.fancyplots.gui.utils import mouse_coordinates
from ccu.fancyplots.gui.utils import obtain_boxsizes


def entry_tk(
    root: tk.Tk,
    row: int,
    column: int,
    dictionary: dict[str, int | str | tk.Entry | tk.Label],
    name: str,
    message: str,
) -> None:
    """Creates an entry and label and adds configuration to dictionary

    Args:
        root: The root window to which the entry and label will be added.
        row: The row to which the entry and label will be added.
        column: The column to which the entry and label will be added.
        dictionary: The dictionary in which to store the configuration.
        name: The text used for the label.
        message: The descriptive message to be displayed for the label.
    """
    dictionary[f"{name}_label"] = tk.Label(root, text=name)
    dictionary[f"{name}_label_row"] = row
    dictionary[f"{name}_label_column"] = column
    dictionary[f"{name}_label_message"] = message
    dictionary[name] = tk.Entry(root, width=10, justify=tk.CENTER)
    dictionary[f"{name}_row"] = row
    dictionary[f"{name}_column"] = column + 1


def make_formatting_entries(
    windows: dict[str, tk.Tk | None],
    param_dict: dict[str, int | str | tk.Entry | tk.Label],
) -> None:
    """Create `tk.Entry`s and `tk.Label`s for setting graph parameters

    Args:
        windows: A dictionary mapping names to `tk.Tk`s and containing the root window.
        param_dict: A dictionary containing the parameters used to configure the graph.
    """
    entry_tk(
        windows["root"],
        row=3,
        column=1,
        dictionary=param_dict,
        name="boxsize",
        message="Defines the width:height ratio of the graph by specifying "
        "*width*,*height* in inches.",
    )
    entry_tk(
        windows["root"],
        row=3,
        column=3,
        dictionary=param_dict,
        name="xaxis",
        message="Defines a non-default x-range by specifying *xmin*,*xmax*.",
    )
    entry_tk(
        windows["root"],
        row=3,
        column=5,
        dictionary=param_dict,
        name="yaxis",
        message="Defines a non-default y-range by specifying *ymin*,*ymax*.",
    )
    entry_tk(
        windows["root"],
        row=3,
        column=7,
        dictionary=param_dict,
        name="font",
        message="Defines a non-default font type. Currently supported: "
        "'serif', 'sans-serif', 'monospace', 'cursive', 'fantasy'.",
    )
    entry_tk(
        windows["root"],
        row=4,
        column=1,
        dictionary=param_dict,
        name="xlabel",
        message="Defines a label for the x-axis. If no label is desired, "
        "leave this space in blank.",
    )
    entry_tk(
        windows["root"],
        row=4,
        column=3,
        dictionary=param_dict,
        name="ylabel",
        message="Defines a label for the y-axis. If no label is desired, "
        "leave this space in blank.",
    )
    entry_tk(
        windows["root"],
        row=4,
        column=5,
        dictionary=param_dict,
        name="tick_loc",
        message="Defines the tick's location - inside or outside of the "
        "graph's margin. Supports 'in' and 'out' keywords.",
    )
    entry_tk(
        windows["root"],
        row=4,
        column=7,
        dictionary=param_dict,
        name="tick_dec",
        message="Defines the tick's decimal numbers. If '2' is stated, ticks "
        "will show e.g. 1.00, 2.00,...",
    )
    entry_tk(
        windows["root"],
        row=5,
        column=1,
        dictionary=param_dict,
        name="tick_min",
        message="Defines how many minor ticks between the major ones are "
        "desired.",
    )
    entry_tk(
        windows["root"],
        row=5,
        column=3,
        dictionary=param_dict,
        name="tick_double",
        message="If True, ticks will be shown on the right-hand side as well.",
    )
    entry_tk(
        windows["root"],
        row=5,
        column=5,
        dictionary=param_dict,
        name="fontsize",
        message="Size of the font for x-axis, y-axis and paths' labels. Title"
        "will have a value of the fontize+1 and additional text fontsize-2.",
    )
    entry_tk(
        windows["root"],
        row=5,
        column=7,
        dictionary=param_dict,
        name="linewidth",
        message="Width of the paths' lines, graph's margins are affected as "
        "well.",
    )
    entry_tk(
        windows["root"],
        row=6,
        column=1,
        dictionary=param_dict,
        name="legend_loc",
        message="Location of the legends. Accepted keywords: best, upper "
        "right, upper left, lower right, lower left, upper center, lower "
        "center, center left, center right, center.",
    )
    entry_tk(
        windows["root"],
        row=6,
        column=3,
        dictionary=param_dict,
        name="colors",
        message="Color palettes are shown if 'Color Palettes' button is "
        "clicked.",
    )
    entry_tk(
        windows["root"],
        row=6,
        column=5,
        dictionary=param_dict,
        name="title",
        message="States the title of the graph, leave this space in black if "
        "no title is desired.",
    )
    entry_tk(
        windows["root"],
        row=6,
        column=7,
        dictionary=param_dict,
        name="savename",
        message="Saves the figure with its corresponding extension (png,jpg,"
        "pdf,...).",
    )
    entry_tk(
        windows["root"],
        row=7,
        column=1,
        dictionary=param_dict,
        name="dpi",
        message="Dots per inch defines the resolution of the figure. This "
        "number will do nothing for pdf, svg and eps formats since these are "
        "vector images.",
    )
    entry_tk(
        windows["root"],
        row=7,
        column=3,
        dictionary=param_dict,
        name="visual",
        message="Visual is enabled by default and cannot be changed. This "
        "keyword is recognized by fancy plots to enable GUI.",
    )
    param_dict["visual"].insert(0, "True")
    param_dict["visual"].config(state="disabled")


def pack_entries(dictionary: dict[str, int | str | tk.Entry | tk.Label]):
    """Organize parameter entries and create tooltips

    Args:
        dictionary: A parameter dictionary containing the tk.Entry and tk.Label instances
            to organize.
    """
    for name, value in dictionary.items():
        if isinstance(value, tk.Entry | tk.Label):
            value.grid(
                row=dictionary[f"{name}_row"],
                column=dictionary[f"{name}_column"],
            )
        if name.split("_")[-1] == "label":
            create_tooltip(value, text=dictionary[f"{name}_message"])


def bind_functions(
    param_dict: dict[str, int | str | tk.Entry | tk.Label],
    parameters: list[str],
    paths_dict: dict[str, float | str],
    full_pathway: list[str],
    windows: dict[str, tk.Tk | None],
    matplotlib_params: dict,
    execution: dict,
    add_text_dict: dict[int, list[str]],
    add_text: list[list[float | str]],
):
    """Bind updating the graph to pressing return in a parametry entry box"""
    for value in param_dict.values():
        if isinstance(value, tk.Entry):
            value.bind(
                "<Return>",
                partial(
                    make_parameters_and_plot,
                    param_dict,
                    parameters,
                    paths_dict,
                    full_pathway,
                    windows,
                    matplotlib_params,
                    execution,
                    add_text_dict,
                    add_text,
                ),
            )


def make_parameters_and_plot(
    param_dict: dict[str, int | str | tk.Entry | tk.Label],
    parameters: list[str],
    paths_dict: dict[str, float | str],
    full_pathway: list[str],
    windows: dict[str, tk.Tk | None],
    matplotlib_params,
    execution,
    add_text_dict: dict[int, list[str]],
    add_text: list[list[float | str]],
    event=None,
):
    FreeEnergyDiagram.make_parameters(param_dict, parameters)
    if windows["graph_window"]:
        FreeEnergyDiagram.update_graph(
            param_dict,
            parameters,
            paths_dict,
            full_pathway,
            windows["graph_window"],
            matplotlib_params,
            add_text_dict,
            add_text,
        )
        execution["initial_coordinates"] = tk.Label(
            windows["graph_window"], text="x=0.000 y=0.000"
        )
        execution["initial_coordinates"].grid(row=10, column=1, sticky=tk.S)
        windows["graph_window"].bind(
            "<Control-Motion>",
            partial(
                mouse_coordinates,
                windows["graph_window"],
                execution,
                matplotlib_params["ax1"],
                param_dict,
            ),
        )
        scale_window_x, scale_window_y = obtain_boxsizes(parameters)
        windows["graph_window"].geometry(
            f"{int((120*scale_window_x)+80)}x{int((120*scale_window_y)+80)}"
        )
