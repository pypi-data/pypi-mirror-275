import contextlib
from functools import partial
import tkinter as tk
from tkinter import messagebox

from ccu.fancyplots.gui.fed import FreeEnergyDiagram
from ccu.fancyplots.gui.menu import make_textmenu
from ccu.fancyplots.gui.menu import show_textmenu
from ccu.fancyplots.gui.root import Root
from ccu.fancyplots.gui.utils import get_path


class MechanismSection:
    """GUI element for specifying mechanism free energies

    Attributes:
        npaths_var: A `tk.IntVar` indicating the number of paths in the mechanism
        full_pathway_names: A `tk.Entry` containing the name of each pathway.
    """

    def __init__(
        self,
        windows: dict[str, tk.Tk | None],
        full_pathway: list[str],
        paths_dict: dict[str, float | str],
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        matplotlib_params: dict,
        execution: dict,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
    ) -> None:
        """_summary_
        Create a mechanism section for a given root window.

        Args:
            windows: A dictionary mapping names to `tk.Tk` instances and containing the root window.
            full_pathway: A list of strings, each string representing a step in a mechanism.
            paths_dict: Free energies & legend labels for each step in each pathway in the mechanism.
            param_dict: A dictionary mapping parameters to their values or `tk.Entry` or `tk.Label` instances.
            parameters: A list of strings indicating the figure configuration parameters.
            matplotlib_params: _description_
            execution: _description_
            add_text_dict: A dictionary mapping integers to lists of strings specifying additional text/formatting.
            add_text: `add_text_dict` but flat and with x/y coordinates as floats.
        """
        root: tk.Tk = windows["root"]
        tk.Label(root, text="").grid(row=8, column=1)  # blank line

        tk.Label(root, text="Number of Paths: ").grid(
            row=9, column=4, columnspan=1
        )
        npaths_var = tk.IntVar(root, 1)
        npaths_box = tk.Spinbox(
            root, from_=1, to=30, textvariable=npaths_var, width=3
        )
        npaths_box.grid(row=10, column=4, padx=0)

        tk.Label(root, text="Full Mechanism Divisions: ").grid(
            row=9, column=1, columnspan=3
        )
        full_pathway_names = tk.Entry(root, width=30, justify=tk.CENTER)
        full_pathway_names.grid(row=10, column=1, columnspan=3)

        tk.Button(
            root,
            text="Define Gibbs Free Energies",
            command=partial(
                MechanismWindow.define_free_energies,
                full_pathway,
                full_pathway_names,
                npaths_var,
                paths_dict,
                windows,
            ),
        ).grid(row=10, column=5, columnspan=2, padx=10)

        tk.Button(
            root,
            text="Reorder Pathways",
            command=partial(
                MechanismSection.reorder_paths,
                paths_dict,
                windows,
                param_dict,
                parameters,
                full_pathway,
                matplotlib_params,
                execution,
                add_text_dict,
                add_text,
            ),
        ).grid(row=10, column=5, columnspan=9, padx=199)
        self.npaths_var = npaths_var
        self.full_pathway_names = full_pathway_names

    @staticmethod
    def reorder_paths(
        paths_dict: dict[str, float | str],
        windows: dict[str, tk.Tk | None],
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        full_pathway: list[str],
        matplotlib_params,
        execution,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
    ):
        if windows["reorder"]:
            Root.quit_window(windows, "reorder")
        npaths = 0
        namelist = []
        for name in paths_dict:
            if (
                name.split("_")[0].split(" ")[0] == "Pathway"
                and name.split("-")[-1] != "legendlabel"
            ):
                if int(name.split("_")[0].split(" ")[1]) >= npaths:
                    npaths = int(name.split("_")[0].split(" ")[1])
                storename = f"Pathway {name.split('_')[0].split(' ')[1]}"
                if storename not in namelist:
                    namelist.append(storename)
        if npaths < 2:
            messagebox.showerror(
                "Is there a Pathway?", "Please define at least 2 pathways."
            )
        else:
            windows["reorder"] = tk.Toplevel()
            windows["reorder"].geometry("250x100")
            windows["reorder"].title("Fancy Plots - Reordering pathways")
            windows["reorder"].protocol(
                "WM_DELETE_WINDOW",
                partial(Root.quit_window, windows, "reorder"),
            )
            old = []
            for i in namelist:
                old.append(i.split(" ")[1])
            tk.Label(windows["reorder"], text="Old Arrangement").grid(
                row=1, column=1, sticky=tk.W
            )
            tk.Label(windows["reorder"], text="New Arrangement").grid(
                row=1, column=2, sticky=tk.E, padx=30
            )
            tk.Label(windows["reorder"], text=",".join(old)).grid(
                row=2, column=1, sticky=tk.W
            )
            new_arrangement = tk.Entry(
                windows["reorder"], width=10, justify=tk.CENTER
            )
            new_arrangement.grid(row=2, column=2)
            tk.Label(windows["reorder"], text="").grid(
                row=3, column=1
            )  # empty line
            tk.Button(
                windows["reorder"],
                text="Reorder",
                command=partial(
                    MechanismSection.reorder_save,
                    paths_dict,
                    old,
                    new_arrangement,
                    param_dict,
                    parameters,
                    full_pathway,
                    windows,
                    matplotlib_params,
                    execution,
                    add_text_dict,
                    add_text,
                ),
            ).grid(row=4, column=1, columnspan=2)
            windows["reorder"].bind(
                "<Return>",
                partial(
                    MechanismSection.reorder_save,
                    paths_dict,
                    old,
                    new_arrangement,
                    param_dict,
                    parameters,
                    full_pathway,
                    windows,
                    matplotlib_params,
                    execution,
                    add_text_dict,
                    add_text,
                ),
            )
            windows["reorder"].protocol(
                "WM_DELETE_WINDOW",
                partial(Root.quit_window, windows, "reorder"),
            )

    @staticmethod
    def reorder_save(
        paths_dict: dict[str, float | str],
        old,
        new,
        param_dict: dict[str, int | str | tk.Entry | tk.Label],
        parameters: list[str],
        full_pathway: list[str],
        windows: dict[str, tk.Tk | None],
        matplotlib_params,
        execution,
        add_text_dict: dict[int, list[str]],
        add_text: list[list[float | str]],
        event=None,
    ):
        try:
            _new_arrangement = new.get().split(",")
            new_arrangement = []
            for i in _new_arrangement:
                int(i)
                if i not in old:
                    raise ValueError
                elif i in new_arrangement:
                    pass
                else:
                    new_arrangement.append(i)
            if len(old) != len(new_arrangement):
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Error!",
                "Oh, no... Something went wrong. Make sure you type your desired "
                "order in this format --> 3,1,2 and that the path number is "
                "defined.",
            )
            windows["reorder"].lift()
            windows["reorder"].after(
                1, lambda: windows["reorder"].focus_force()
            )
            new_arrangement = False

        if new_arrangement:
            buffer = {}
            rearrange = {}
            for i, j in zip(old, new_arrangement, strict=False):
                rearrange[j] = i
            for name in paths_dict:
                if (
                    name.split("_")[0].split(" ")[0] == "Pathway"
                    and name.split("-")[-1] != "legendlabel"
                ):
                    number = name.split("_")[0].split(" ")[1]
                    if name.split("_")[1].lower() == "ts":
                        label = f"{name.split('_')[1]}_{name.split('_')[2]}"
                    else:
                        label = name.split("_")[1]
                    buffer[f"Pathway {rearrange[number]}_{label}"] = (
                        paths_dict[f"Pathway {number}_{label}"]
                    )
                elif name.split("-")[-1] == "legendlabel":
                    number = name.split("-")[0].split(" ")[1]
                    buffer[f"Pathway {rearrange[number]}-legendlabel"] = (
                        paths_dict[f"Pathway {number}-legendlabel"]
                    )
            paths_dict.clear()
            for name in buffer:
                paths_dict[name] = buffer[name]
            FreeEnergyDiagram.create(
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
            Root.quit_window(windows, "reorder")


class MechanismWindow:
    @staticmethod
    def make_path_windows(
        energy_window: tk.Tk,
        variable: tk.StringVar,
        full_pathway: list[str],
        paths_dict: dict[str, float | str],
        define_entries: dict[str, str | tk.Entry | tk.Label],
        keyword=None,
    ) -> None:
        """Create windows for specifying the free energies of each path.

        This method modifies `define_entries` in place.

        Args:
            energy_window: The `tk.Tk` instance for specifying free energies.
            variable: A `tk.StringVar` storing the current pathway.
            full_pathway: A list of strings, each string representing a step in a pathway.
            paths_dict: Free energies & legend labels for each step in each pathway in the mechanism.
            define_entries: An empty dictionary to be used to store the free energies and legend labels of the pathway.
            keyword: _description_. Defaults to None.
        """
        energy_window.geometry(f"400x{160+(15*(len(full_pathway)//2))}")
        pathway = variable.get()

        tk.Label(energy_window, text="").grid(row=2, column=1)

        if len(full_pathway) < 3:
            define_entries["title"] = tk.Label(
                energy_window, text=pathway
            ).grid(row=3, column=1, columnspan=100, sticky=tk.W)
        else:
            define_entries["title"] = tk.Label(energy_window, text=pathway)
            define_entries["title"].grid(row=3, column=1, columnspan=100)
            define_entries["title"].configure(anchor="center")

        # Place `tk.Entry`s for defining free energies
        row_offset = 3

        for i, step in enumerate(full_pathway):
            match i % 3:
                case 0:
                    row_offset += 1
                    column_offset = 1
                case _:
                    column_offset += 2

            label = tk.Label(energy_window, text=step)
            define_entries[f"{step}_label"] = label
            label.grid(row=row_offset, column=column_offset)
            define_entries[step] = tk.Entry(energy_window, width=12)

            if paths_dict:
                with contextlib.suppress(ValueError, KeyError):
                    value = str(float(paths_dict[f"{pathway}_{step}"]))
                    define_entries[step].insert(0, value)

            define_entries[step].grid(row=row_offset, column=column_offset + 1)

        # Legend Labels
        tk.Label(energy_window, text="").grid(row=4, column=1)

        tk.Label(energy_window, text="Path Label \n (Legend)").grid(
            row=97, column=1, columnspan=3, sticky=tk.W
        )
        define_entries["legendlabel"] = tk.Entry(energy_window, width=25)
        define_entries["legendlabel"].grid(
            row=97, column=1, columnspan=10, sticky=tk.W, padx=70
        )

        tk.Label(energy_window, text="").grid(row=98, column=1)
        tk.Label(energy_window, text="").grid(row=99, column=1)

        legendlabel = f"{pathway}-legendlabel"
        if legendlabel in paths_dict:
            value = str(paths_dict[legendlabel]).encode()
            define_entries["legendlabel"].insert(0, value)

        tk.Button(
            energy_window,
            text="Save",
            command=partial(
                MechanismWindow.save_values,
                paths_dict,
                define_entries,
                pathway,
                energy_window,
            ),
        ).grid(row=1, column=1, columnspan=10, sticky=tk.W, padx=105)

    @staticmethod
    def save_values(
        paths_dict: dict[str, float | str],
        define_entries: dict[str, str | tk.Entry | tk.Label],
        pathway: str,
        energy_window: tk.Tk,
    ) -> None:
        """Save the values from `define_entries` to `paths_dict`.

        This method modifies `paths_dict` in place.

        Args:
            paths_dict: Free energies & legend labels for each step in each pathway in the mechanism
            define_entries: A dictionary used to define the free energies and legend labels for a pathway.
            pathway: The name of the pathway.
            energy_window: The `tk.Tk` instance for specifying free energies.
        """
        success = True
        for name, value in define_entries.items():
            if name.split("_")[-1] == "label" or name == "title":
                pass
            elif name == "legendlabel":
                # pdict[f'{pathway}-legendlabel'] = value.get()
                paths_dict[f"{pathway}-legendlabel"] = (
                    value.get().encode().decode("unicode_escape")
                )
            else:
                try:
                    paths_dict[f"{pathway}_{name}"] = float(value.get())
                except ValueError:
                    if value.get():
                        success = False
                        messagebox.showwarning(
                            "Number not recognized!",
                            f"'{value.get()}' is not recognized as a number, "
                            "region '{name}' will be ignored for this pathway.",
                        )
                        energy_window.lift()
                        energy_window.after(
                            1, lambda: energy_window.focus_force()
                        )
                    if f"{pathway}_{name}" in paths_dict:
                        del paths_dict[f"{pathway}_{name}"]
        if success:
            messagebox.showinfo(
                "Save",
                f"Values on {pathway} saved successfully. Click on 'Show Graph' "
                "to create or update figure.",
            )
            energy_window.lift()
            energy_window.after(1, lambda: energy_window.focus_force())

    @staticmethod
    def define_free_energies(
        full_pathway: list[str],
        full_pathway_names: tk.Entry,
        npaths_var: tk.IntVar,
        paths_dict: dict[str, float | str],
        windows: dict[str, tk.Tk | None],
    ):
        """Specify free energies for each step and labels for each pathway

        Args:
            full_pathway: A list of strings, each string representing a step in a pathway
            full_pathway_names: A `tk.Entry` containing the name of each pathway.
            npaths_var: A `tk.IntVar` indicating the number of paths in the mechanism
            paths_dict: Free energies & legend labels for each step in each pathway in the mechanism.
            windows: A dictionary mapping names to `tk.Tk`s and containing the root window.
        """
        if windows["energy_window"]:
            Root.quit_window(windows, "energy_window")
        if not full_pathway_names.get():
            messagebox.showerror(
                "Divisions not found!",
                "Please define the mechanism's divisions in 'Full Mechanism "
                "Divisions' entry box.",
            )
            paths_dict.clear()
        else:
            windows["energy_window"] = tk.Toplevel()
            windows["energy_window"].geometry("350x80")
            windows["energy_window"].title("Fancy Plots - Energy Declaration")
            the_menu = make_textmenu(windows["energy_window"])
            windows["energy_window"].bind_class(
                "Entry",
                "<Button-3><ButtonRelease-3>",
                partial(show_textmenu, the_menu),
            )
            windows["energy_window"].bind_class(
                "Entry",
                "<Control-q>",
                partial(Root.callback_select_all, windows["root"]),
            )
            get_path(full_pathway, full_pathway_names)
            npaths = npaths_var.get()
            params = [f"Pathway {i+1!s}" for i in range(int(npaths))]

            for string in list(paths_dict):
                number = string.split(" ")[1].split("_")[0].split("-")[0]
                if float(number) > int(npaths):
                    del paths_dict[string]

            define_entries = {}
            variable = tk.StringVar(windows["energy_window"], params[0])
            dropdown = tk.OptionMenu(
                windows["energy_window"],
                variable,
                *params,
                command=partial(
                    MechanismWindow.make_path_windows,
                    windows["energy_window"],
                    variable,
                    full_pathway,
                    paths_dict,
                    define_entries,
                ),
            )
            MechanismWindow.make_path_windows(
                windows["energy_window"],
                variable,
                full_pathway,
                paths_dict,
                define_entries,
            )

            dropdown.grid(row=1, column=1, columnspan=10, sticky=tk.W)

            windows["energy_window"].protocol(
                "WM_DELETE_WINDOW",
                partial(Root.quit_window, windows, "energy_window"),
            )
