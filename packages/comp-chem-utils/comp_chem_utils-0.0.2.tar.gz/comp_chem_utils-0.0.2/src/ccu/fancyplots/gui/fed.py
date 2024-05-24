from functools import partial
import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ccu.fancyplots import fancyplots
from ccu.fancyplots.gui.defaults import DEFAULTS
from ccu.fancyplots.gui.root import Root
from ccu.fancyplots.gui.tooltip import create_tooltip
from ccu.fancyplots.gui.utils import add_text_converter
from ccu.fancyplots.gui.utils import convert_path_to_list
from ccu.fancyplots.gui.utils import mouse_coordinates
from ccu.fancyplots.gui.utils import obtain_boxsizes


class FreeEnergyDiagram:
    @staticmethod
    def create(
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        paths_dict: dict[str, float | str],
        full_pathway: list[str],
        windows: dict[str, tk.Tk | None],
        matplotlib_params,
        execution,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
    ):
        """Create a free energy diagram."""
        if windows["graph_window"]:
            try:
                destroy = FreeEnergyDiagram.update_graph(
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
                execution["initial_coordinates"].grid(
                    row=10, column=1, sticky=tk.S
                )
                windows["graph_window"].bind(
                    "<Control-Motion>",
                    partial(
                        mouse_coordinates,
                        windows["graph_window"],
                        execution,
                        matplotlib_params["ax1"],
                        parameters,
                    ),
                )
            except tk.TclError:
                windows["graph_window"] = None
                destroy = FreeEnergyDiagram.create(
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
            if destroy:
                Root.quit_window(
                    windows, "graph_window", matplotlib_params, "canvas"
                )
            else:
                scale_window_x, scale_window_y = obtain_boxsizes(parameters)
                windows["graph_window"].geometry(
                    f"{int((120*scale_window_x)+80)}x{int((120*scale_window_y)+80)}"
                )
        else:
            windows["graph_window"] = tk.Toplevel()
            FreeEnergyDiagram.make_parameters(param_dict, parameters)
            scale_window_x, scale_window_y = obtain_boxsizes(parameters)
            windows["graph_window"].geometry(
                f"{int((120*scale_window_x)+80)}x{int((120*scale_window_y)+80)}"
            )
            windows["graph_window"].title("Fancy Plots - Graph")

            FreeEnergyDiagram.make_parameters(param_dict, parameters)

            execution = {}
            execution["initial_coordinates"] = tk.Label(
                windows["graph_window"], text="x=0.000 y=0.000"
            )
            execution["initial_coordinates"].grid(
                row=10, column=1, sticky=tk.S
            )

            cleanup_button = tk.Button(
                windows["graph_window"],
                text="Hold to Preview Graph with Tight Layout",
            )
            cleanup_button.grid(row=11, column=1, sticky=tk.S)
            cleanup_button.bind(
                "<ButtonPress-1>",
                partial(
                    FreeEnergyDiagram.tight_layout_on_press,
                    param_dict,
                    parameters,
                    paths_dict,
                    full_pathway,
                    matplotlib_params,
                    add_text_dict,
                    add_text,
                    windows,
                ),
            )
            cleanup_button.bind(
                "<ButtonRelease-1>",
                partial(
                    FreeEnergyDiagram.tight_layout_on_release,
                    windows,
                    matplotlib_params,
                ),
            )
            create_tooltip(
                cleanup_button,
                text="Sometimes the y-label is cut off from the graph (does "
                "not apply to the final figure).\n"
                "Tight Layout often fixes this issue, but the coordinate "
                "system displayed above is no longer consistent.\n"
                "Previewing by holding this button will allow you to see how "
                "the labels will look like in the figure you will save,\n"
                "without having to save it.",
            )
            introduction = tk.Label(
                windows["graph_window"],
                text="""Hold down CTRL to check your cursor's coordinates.""",
            )
            introduction.grid(row=1, column=1)
            destroy = FreeEnergyDiagram.update_graph(
                param_dict,
                parameters,
                paths_dict,
                full_pathway,
                windows["graph_window"],
                matplotlib_params,
                add_text_dict,
                add_text,
            )
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
            windows["graph_window"].protocol(
                "WM_DELETE_WINDOW",
                partial(
                    Root.quit_window,
                    windows,
                    "graph_window",
                    matplotlib_params,
                    "canvas",
                ),
            )
            if destroy:
                Root.quit_window(
                    windows, "graph_window", matplotlib_params, "canvas"
                )
        return destroy

    @staticmethod
    def update_graph(
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        paths_dict: dict[str, float | str],
        full_pathway: list[str],
        root: tk.Tk,
        matplotlib_params,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
    ) -> bool:
        (
            matplotlib_params["ax1"],
            matplotlib_params["fig"],
        ) = FreeEnergyDiagram.generate_figure(
            param_dict,
            parameters,
            paths_dict,
            full_pathway,
            add_text_dict,
            add_text,
        )
        if "canvas" in matplotlib_params:
            matplotlib_params["canvas"]._tkcanvas.destroy()
        matplotlib_params["canvas"] = FigureCanvasTkAgg(
            matplotlib_params["fig"], master=root
        )
        matplotlib_params["canvas"].draw()
        matplotlib_params["canvas"].get_tk_widget().grid(
            row=9, column=1, padx=30
        )
        return not matplotlib_params["ax1"] and not matplotlib_params["fig"]

    @staticmethod
    def generate_figure(
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        paths_dict: dict[str, float | str],
        full_pathway: list[str],
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
        save=False,
    ):
        FreeEnergyDiagram.make_parameters(param_dict, parameters)
        add_text_converter(add_text_dict, add_text)
        list_of_dicts, labelling = convert_path_to_list(
            paths_dict, full_pathway
        )
        with Path(".cache.fancy").open(mode="w", encoding="utf-8") as file:
            json.dump(
                [parameters, full_pathway, list_of_dicts, labelling, add_text],
                file,
                indent=4,
            )

        if not list_of_dicts:
            messagebox.showerror(
                "Error!", "No pathway is defined, please define at least one."
            )
            ax1, fig = None, None
        else:
            if save:
                old_params = []
                for i in parameters:
                    if i == "visual=True":
                        old_params.append("visual=False")
                    else:
                        old_params.append(i)
                parameters = old_params

            ax1, fig, savename = fancyplots.init(
                "Gibbs",
                parameters,
                full_pathway,
                list_of_dicts,
                labelling=labelling,
                add_text=add_text,
            )
            if save:
                messagebox.showinfo(
                    "Save", f"Figure '{savename}' saved successfully."
                )

        return ax1, fig

    @staticmethod
    def make_parameters(
        dictionary: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
    ) -> None:
        """Construct the list of parameters from the parameter dictionary.

        This method edits `parameters` in place.

        Args:
            dictionary: The parameter dictionary.
            parameters: The list of parameters.
        """
        parameters.clear()
        parameters.append("visual=True")
        for name, value in dictionary.items():
            if isinstance(value, tk.Entry):
                if (name in ["xlabel", "ylabel"]) and not value.get():
                    parameters.append(f"{name}={' '}")
                elif val := value.get():
                    encoded_val = val.encode()
                    decoded_val = encoded_val.decode("unicode_escape")
                    parameters.append(f"{name}={decoded_val}")

    # TODO: This code is relevant to FormattingSection and should be moved there
    @staticmethod
    def set_default_settings(
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        paths_dict: dict[str, float | str],
        full_pathway: list[str],
        windows: dict[str, tk.Tk | None],
        matplotlib_params: dict,
        execution: dict,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
    ) -> None:
        """Set the default parameter values

        This method edits `parameters` in place.

        Args:
            param_dict: A dictionary containing parameter values.
            parameters: An empty list in which the default parameters will be placed.
            paths_dict: Free energies & legend labels for each step in each pathway in the mechanism.
            full_pathway: A list of strings, each string representing a step in a mechanism.
            windows: A dictionary containing the application windows.
            matplotlib_params: _description_
            execution: _description_
            add_text_dict: A dictionary mapping integers to lists of strings specifying additional text/formatting.
            add_text: `add_text_dict` but flat and with x/y coordinates as floats
        """
        # Delete existing values
        for value in param_dict.values():
            if isinstance(value, tk.Entry):
                value.delete(0, tk.END)

        # Set default values
        for name, value in DEFAULTS.items():
            entry: tk.Entry = param_dict[name]
            entry.insert(0, value)

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
            execution["initial_coordinates"].grid(
                row=10, column=1, sticky=tk.S
            )
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

    @staticmethod
    def tight_layout_on_press(
        param_dict,
        parameters,
        paths_dict,
        full_pathway,
        matplotlib_params,
        add_text_dict,
        add_text,
        windows,
        event=None,
    ):
        if windows["tight_layout"]:
            Root.quit_window(
                windows, "tight_layout", matplotlib_params, "canvas_tl"
            )
        windows["tight_layout"] = tk.Toplevel()
        scale_window_x, scale_window_y = obtain_boxsizes(parameters)
        windows["tight_layout"].geometry(
            f"{int((120*scale_window_x)+80)}x{int((120*scale_window_y)+80)}"
        )
        windows["tight_layout"].title("Fancy Plots - Preview")
        fig = matplotlib_params["fig"]
        fig.tight_layout()
        if "canvas_tl" in matplotlib_params:
            matplotlib_params["canvas_tl"]._tkcanvas.destroy()
        matplotlib_params["canvas_tl"] = FigureCanvasTkAgg(
            fig, master=windows["tight_layout"]
        )
        matplotlib_params["canvas_tl"].draw()
        matplotlib_params["canvas_tl"].get_tk_widget().grid(
            row=9, column=1, padx=30
        )
        windows["tight_layout"].protocol(
            "WM_DELETE_WINDOW",
            partial(
                Root.quit_window,
                windows,
                "tight_layout",
                matplotlib_params,
                "canvas_tl",
            ),
        )

    @staticmethod
    def tight_layout_on_release(windows, matplotlib_params, event=None):
        Root.quit_window(
            windows, "tight_layout", matplotlib_params, "canvas_tl"
        )
