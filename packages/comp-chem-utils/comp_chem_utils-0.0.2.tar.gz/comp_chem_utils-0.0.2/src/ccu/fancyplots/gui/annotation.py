from functools import partial
import tkinter as tk

from ccu.fancyplots.gui.text import add_text_def
from ccu.fancyplots.gui.text import show_text_def


class AnnotationSection:
    """GUI component for adding annotations to the free energy diagram

    Attributes:
        number_text: A `tk.IntVar` for numbering annotations.
        add_text_widget: `tk.Entry` for adding annotations.
        add_text_x: `tk.Entry` for specifying the x-position of the annotation.
        add_text_y: `tk.Entry` for specifying the y-position of the annotation.
        add_text_color: `tk.Entry` for specifying the annotation text colour.
        add_text_fontsize: `tk.Entry` for specifying the annotation font size.
    """

    def __init__(
        self,
        root: tk.Tk,
        graph_window: tk.Tk | None,
        full_pathway: list[str],
        paths_dict: dict[str, float | str],
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        matplotlib_params: dict,
        execution: dict,
        add_text_dict: dict[int, list[str]],
    ) -> None:
        """Create section for adding annotations to the free energy diagram"""
        tk.Label(root, text="Additional Text: ").grid(
            row=12, column=1, columnspan=3
        )
        add_text_widget = tk.Entry(root, width=30, justify=tk.CENTER)
        add_text_widget.grid(row=13, column=1, columnspan=3)

        tk.Label(root, text="X Coordinate: ").grid(
            row=12, column=4, columnspan=1
        )
        add_text_x = tk.Entry(root, width=10, justify=tk.CENTER)
        add_text_x.grid(row=13, column=4)

        tk.Label(root, text="Y Coordinate: ").grid(
            row=12, column=5, columnspan=1
        )
        add_text_y = tk.Entry(root, width=10, justify=tk.CENTER)
        add_text_y.grid(row=13, column=5)

        tk.Label(root, text="Color: ").grid(row=12, column=6, columnspan=1)
        add_text_color = tk.Entry(root, width=10, justify=tk.CENTER)
        add_text_color.grid(row=13, column=6)

        add_text_fontsize = tk.Label(root, text="Fontsize: ").grid(
            row=12, column=7, columnspan=1
        )
        add_text_fontsize = tk.Entry(root, width=3, justify=tk.CENTER)
        add_text_fontsize.grid(row=13, column=7)

        tk.Label(root, text="Text Number: ").grid(
            row=12, column=8, columnspan=1
        )
        number_text = tk.IntVar(root, 1)
        n_text = tk.Spinbox(
            root,
            from_=1,
            to=100,
            textvariable=number_text,
            width=3,
            command=partial(
                show_text_def,
                number_text,
                add_text_dict,
                add_text_widget,
                add_text_x,
                add_text_y,
                add_text_color,
                add_text_fontsize,
            ),
        )
        n_text.grid(row=13, column=8)
        n_text.bind(
            "<Return>",
            partial(
                show_text_def,
                number_text,
                add_text_dict,
                add_text_widget,
                add_text_x,
                add_text_y,
                add_text_color,
                add_text_fontsize,
            ),
        )

        tk.Button(
            root,
            text="Save Text",
            command=partial(
                add_text_def,
                number_text,
                add_text_dict,
                add_text_widget,
                add_text_x,
                add_text_y,
                add_text_color,
                add_text_fontsize,
                graph_window,
                param_dict,
                parameters,
                paths_dict,
                full_pathway,
                matplotlib_params,
                execution,
            ),
        ).grid(row=13, column=9, columnspan=1, sticky=tk.W)

        self.number_text = number_text
        self.add_text_widget = add_text_widget
        self.add_text_x = add_text_x
        self.add_text_y = add_text_y
        self.add_text_color = add_text_color
        self.add_text_fontsize = add_text_fontsize
