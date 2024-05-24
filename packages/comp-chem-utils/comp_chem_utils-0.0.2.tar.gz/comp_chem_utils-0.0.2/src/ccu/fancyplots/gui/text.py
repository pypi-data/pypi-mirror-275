from functools import partial
import tkinter as tk
from tkinter import messagebox

from ccu.fancyplots.gui.fed import FreeEnergyDiagram
from ccu.fancyplots.gui.utils import mouse_coordinates
from ccu.fancyplots.gui.utils import obtain_boxsizes


def show_text_def(
    number_text: tk.IntVar,
    add_text_dict: dict[int, list[str]],
    add_text_widget: tk.Entry,
    add_text_x: tk.Entry,
    add_text_y: tk.Entry,
    add_text_color: tk.Entry,
    add_text_fontsize: tk.Entry,
    event=None,
) -> None:
    """Show the parameters for the additional text indicated by the present number.

    Args:
        number_text: A `tk.IntVar` for numbering annotations.
        add_text_dict: _description_
        add_text_widget: `tk.Entry` for adding annotations.
        add_text_x: `tk.Entry` for specifying the x-position of the annotation.
        add_text_y: `tk.Entry` for specifying the y-position of the annotation.
        add_text_color: `tk.Entry` for specifying the annotation text colour.
        add_text_fontsize: `tk.Entry` for specifying the annotation font size.
        event: _description_. Defaults to None.
    """
    nth = number_text.get()
    add_text_x.delete(0, tk.END)
    add_text_y.delete(0, tk.END)
    add_text_color.delete(0, tk.END)
    add_text_fontsize.delete(0, tk.END)
    add_text_widget.delete(0, tk.END)
    if add_text_dict:
        for index, value in add_text_dict.items():
            if int(index) == int(nth):
                add_text_x.insert(0, str(value[0]))
                add_text_y.insert(0, str(value[1]))
                add_text_widget.insert(0, str(value[2]))
                if len(value) >= 4:
                    add_text_color.insert(0, str(value[3]).split("=")[1])
                if len(value) == 5:
                    add_text_fontsize.insert(0, str(value[4]).split("=")[1])


def add_text_def(
    number_text: tk.IntVar,
    add_text: list[list[float | str]],
    add_text_dict: dict[int, list[str]],
    add_text_widget: tk.Entry,
    add_text_x: tk.Entry,
    add_text_y: tk.Entry,
    add_text_color: tk.Entry,
    add_text_fontsize: tk.Entry,
    graph_window: tk.Tk | None,
    param_dict: dict[str, int | str | tk.Entry | tk.Label],
    parameters: list[str],
    paths_dict: dict[str, float | str],
    full_pathway: list[str],
    matplotlib_params,
    execution,
) -> None:
    """Record newly defined additional text and add to free energy diagram.

    The function modifies `add_text_dict` in place.

    Args:
        number_text: A `tk.IntVar` for numbering annotations.
        add_text:
        add_text_dict: A dictionary mapping integers to lists of strings
            representing text/formatting used to annotate the free energy diagram.
        add_text_widget: `tk.Entry` for adding annotations.
        add_text_x: `tk.Entry` for specifying the x-position of the annotation.
        add_text_y: `tk.Entry` for specifying the y-position of the annotation.
        add_text_color: `tk.Entry` for specifying the annotation text colour.
        add_text_fontsize: `tk.Entry` for specifying the annotation font size.
        graph_window: _description_
        param_dict: A dictionary containing all figure parameters, `tk.Entry`s, and `tk.Label`s
        parameters: A list of strings representing free energy diagram parameters
        paths_dict: _description_
        full_pathway: A dictionary mapping integers to lists of strings specifying additional text/formatting
        matplotlib_params: _description_
        execution: _description_
    """
    # text = add_text_widget.get()
    text = (
        add_text_widget.get().encode().decode("unicode_escape")
    )  # recognizes \n
    x = add_text_x.get()
    y = add_text_y.get()
    nth = number_text.get()
    if add_text_color.get():
        color = f"color={add_text_color.get()}"
    else:
        color = "color=k"

    if add_text_fontsize.get():
        fontsize = f"fontsize={add_text_fontsize.get()}"
        add_text_dict[nth] = [x, y, text, color, fontsize]
    else:
        add_text_dict[nth] = [x, y, text, color]

    _continue = True

    if not add_text_dict[nth][2]:
        del add_text_dict[nth]
    elif add_text_dict[nth][2] and (
        not isinstance(add_text_dict[nth][0], float)
        or not isinstance(add_text_dict[nth][1], float)
    ):
        try:
            float(x)
            float(y)
            messagebox.showinfo("Save", f"Text {nth} saved successfully.")
        except ValueError:
            messagebox.showerror(
                "Error!",
                "Text is defined but at least one coordinate is not set or "
                "not valid. Please set your desired x AND y coordinates "
                "using numbers.",
            )
            del add_text_dict[nth]
            _continue = False
    if graph_window and _continue:
        FreeEnergyDiagram.update_graph(
            param_dict,
            parameters,
            paths_dict,
            full_pathway,
            graph_window,
            matplotlib_params,
            add_text_dict,
            add_text,
        )
        execution["initial_coordinates"] = tk.Label(
            graph_window, text="x=0.000 y=0.000"
        )
        execution["initial_coordinates"].grid(row=10, column=1, sticky=tk.S)
        graph_window.bind(
            "<Control-Motion>",
            partial(
                mouse_coordinates,
                graph_window,
                execution,
                matplotlib_params["ax1"],
                param_dict,
            ),
        )
        scale_window_x, scale_window_y = obtain_boxsizes(parameters)
        graph_window.geometry(
            f"{int((120*scale_window_x)+80)}x{int((120*scale_window_y)+80)}"
        )
