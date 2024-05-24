from functools import partial
import importlib.resources
import tkinter as tk

from PIL import Image
from PIL import ImageTk

from ccu.fancyplots.gui.fed import FreeEnergyDiagram
from ccu.fancyplots.gui.root import Root


class FooterSection:
    def __init__(
        self,
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        paths_dict: dict[str, float | str],
        full_pathway: list[str],
        windows: dict[str, tk.Tk | None],
        matplotlib_params: dict,
        execution: dict,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
        images: list,
    ) -> None:
        tk.Button(
            windows["root"],
            text="Default Settings",
            command=partial(
                FreeEnergyDiagram.set_default_settings,
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
        ).grid(row=14, column=1, columnspan=2, pady=30)
        tk.Button(
            windows["root"],
            text="Show Graph",
            command=partial(
                FreeEnergyDiagram.create,
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
        ).grid(row=14, column=2, columnspan=10, pady=30, padx=70, sticky=tk.W)
        tk.Button(
            windows["root"],
            text="Save Graph",
            command=partial(
                FreeEnergyDiagram.generate_figure,
                param_dict,
                parameters,
                paths_dict,
                full_pathway,
                add_text_dict,
                add_text,
                save=True,
            ),
        ).grid(row=14, column=3, columnspan=10, pady=30, padx=79, sticky=tk.W)

        tk.Button(
            windows["root"],
            text="Color Palettes",
            command=partial(FooterSection.mpl_palette, windows, images),
        ).grid(row=14, column=4, columnspan=10, pady=30, padx=96, sticky=tk.W)
        tk.Button(
            windows["root"],
            text="Instructions",
            command=partial(FooterSection.instructions, windows, images),
        ).grid(row=14, column=5, columnspan=10, pady=30, padx=91, sticky=tk.W)

    @staticmethod
    def instructions(windows, images):
        if windows["instructions_window"]:
            Root.quit_window(windows, "instructions_window")

        windows["instructions_window"] = tk.Toplevel()
        windows["instructions_window"].geometry("1400x788")
        windows["instructions_window"].title("Fancy Plots - Instructions")
        tutorial = FooterSection.open_image(
            "fancy_plots_tutorial.png", 1400, 788
        )
        images[1] = tutorial
        tk.Label(windows["instructions_window"], image=images[1]).grid(
            row=0, column=0, columnspan=3
        )
        windows["instructions_window"].protocol(
            "WM_DELETE_WINDOW",
            partial(Root.quit_window, windows, "instructions_window"),
        )

    @staticmethod
    def mpl_palette(windows, images):
        if windows["matplotlib_palette"]:
            Root.quit_window(windows, "matplotlib_palette")

        windows["matplotlib_palette"] = tk.Toplevel()
        windows["matplotlib_palette"].geometry("553x800")
        windows["matplotlib_palette"].title("Fancy Plots - Color Palettes")

        """color_scheme has to be added to a list so it's not garbage collected,
        and consequently not shown to the screen.
        Fixes to this issue are: Declare color_scheme as a global variable -
        not recommended.
                                    Create a class and declare color_scheme as
                                    self.color_scheme
                                    Create a list and add this image to it.
        Creating classes would simplify this code and get rid of most of lists
        and dictionaries, but that is something to be done in the future,
        as the original fancy plots was written class-free and has to be
        rewritten almost entirely from scratch."""

        color_scheme = FooterSection.open_image("color_palette.png", 553, 771)
        images[0] = color_scheme
        tk.Label(windows["matplotlib_palette"], image=images[0]).grid(
            row=0, column=0, columnspan=3
        )

        tk.Label(
            windows["matplotlib_palette"], text="Source: matplotlib.org"
        ).grid(row=1, column=1)

        windows["matplotlib_palette"].protocol(
            "WM_DELETE_WINDOW",
            partial(Root.quit_window, windows, "matplotlib_palette"),
        )

    @staticmethod
    def open_image(name, xsize, ysize):
        images_ = importlib.resources.files("ccu.fancyplots.images")
        image = Image.open(images_.joinpath(name))
        image = image.resize((xsize, ysize), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        return image
