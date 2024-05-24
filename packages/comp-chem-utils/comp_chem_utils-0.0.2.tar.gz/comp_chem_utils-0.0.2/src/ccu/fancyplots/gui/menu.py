"""This module defines functions for menu creation and manipulation."""

import tkinter as tk


def make_textmenu(root) -> tk.Menu:
    the_menu = tk.Menu(root, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")
    the_menu.add_separator()
    the_menu.add_command(label="Select all")
    return the_menu


def show_textmenu(the_menu, event):
    e_widget = event.widget
    the_menu.entryconfigure(
        "Cut", command=lambda: e_widget.event_generate("<<Cut>>")
    )
    the_menu.entryconfigure(
        "Copy", command=lambda: e_widget.event_generate("<<Copy>>")
    )
    the_menu.entryconfigure(
        "Paste", command=lambda: e_widget.event_generate("<<Paste>>")
    )
    the_menu.entryconfigure(
        "Select all", command=lambda: e_widget.select_range(0, "end")
    )
    the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)
