import contextlib
from functools import partial
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

from ccu.fancyplots.gui.menu import make_textmenu
from ccu.fancyplots.gui.menu import show_textmenu


class Root(tk.Tk):
    """Root window for Fancy Plots GUI"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("835x350")
        self.title("Fancy Plots GUI")

    def configure_window(self, windows: dict[str, tk.Tk | None]) -> None:
        """Define subwindows and key bindings for GUI.

        Args:
            windows: A dictionary mapping names to `tk.Tk`s and containing the root window.
        """
        the_menu = make_textmenu(self)
        self.bind_class(
            "Entry",
            "<Button-3><ButtonRelease-3>",
            partial(show_textmenu, the_menu),
        )  # right mouse click popup cut, copy and paste menu
        self.bind_class(
            "Entry",
            "<Control-q>",
            partial(Root.callback_select_all, self),
        )  # select all key binding - q
        self.protocol(
            "WM_DELETE_WINDOW", partial(Root.quitall, windows)
        )  # redefine x button

    @staticmethod
    def quit_window(
        root: dict[str, tk.Tk | None],
        keyword: str,
        additional_dict=None,
        to_delete=None,
    ) -> None:
        Root.tkdestroy(root[keyword])
        root[keyword] = None
        if additional_dict:
            del additional_dict[to_delete]

    @staticmethod
    def tkdestroy(window):
        with contextlib.suppress(tk.TclError):
            window.destroy()

    @staticmethod
    def destroyall(root):
        for value in root.values():
            if value:
                Root.tkdestroy(value)

    @staticmethod
    def quitall(root):
        save_cache = None
        cache = Path(".cache.fancy")
        if cache.exists():
            save_cache = messagebox.askyesnocancel(
                "Quit", "Do you want to save all settings to a file?"
            )
            if save_cache:
                if "savename" in root:
                    Root.tkdestroy(root["savename"])
                root["savename"] = tk.Tk()
                root["savename"].geometry("300x75")
                root["savename"].title("Save cached information")

                tk.Label(root["savename"], text="Name of the file: ").grid(
                    row=1, column=1
                )
                name = tk.Entry(root["savename"], width=20, justify=tk.CENTER)
                name.grid(row=1, column=2)
                tk.Button(
                    root["savename"],
                    text="Save File",
                    command=partial(Root.ok_click, root, name),
                ).grid(row=2, column=1, columnspan=2)

            elif save_cache is False:
                cache.unlink()
                Root.destroyall(root)

            else:
                pass

        else:
            Root.destroyall(root)

    @staticmethod
    def ok_click(root, name, event=None):
        filename = name.get()
        cache = Path(f"{filename}.fancy")
        old_cache = Path(".cache.fancy")
        if not cache.exists():
            old_cache.rename(str(cache))
            Root.destroyall(root)
        else:
            overwrite = messagebox.askquestion(
                "Overwrite",
                f"Are you sure you want to overwrite {filename}.fancy?",
            )
            if overwrite == "yes":
                old_cache.rename(str(cache))
                Root.destroyall(root)

    @staticmethod
    def callback_select_all(root, event):
        # select text after 50ms
        root.after(50, lambda: event.widget.select_range(0, "end"))
