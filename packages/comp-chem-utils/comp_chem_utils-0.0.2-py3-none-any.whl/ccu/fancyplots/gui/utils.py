import tkinter as tk


def convert_path_to_list(paths_dict, full_pathway: list[str]):
    full_list = []
    paths = []
    adict = {}
    labelling = []

    for name in paths_dict:
        name = name.split("_")[0].split("-")[0]
        if name not in paths:
            paths.append(name)
    paths.sort()
    for path in paths:
        for name in full_pathway:
            full_name = f"{path}_{name}"
            if full_name in paths_dict:
                adict[name] = paths_dict[full_name]
        full_list.append(adict)
        adict = {}
        legendlabel = f"{path}-legendlabel"
        if legendlabel in paths_dict:
            labelling.append(paths_dict[legendlabel])
    return full_list, labelling


def add_path(entry, dict_list):
    dict_list.append(entry)


def get_path(
    mechanism_path: list[str], path_names: tk.Entry, event=None
) -> None:
    """Creates full mechanism path from the value in the relevant `tk.Entry`.

    This method modifies `path` in place.

    Args:
        path: A list of strings representing the full mechanism path.
        path_names: A `tk.Entry` containing the full mechanism definition.
        event: _description_. Defaults to None.
    """
    mechanism_path.clear()
    for i in path_names.get().split(","):
        string = ""
        for j in i:
            if j == " ":
                pass
            else:
                string += j
        mechanism_path.append(string)


def mouse_coordinates(root, execution, ax1, param_dict, event):
    x, y = event.x, event.y
    if isinstance(param_dict, dict):
        xfactor = float(param_dict["boxsize"].get().split(",")[0])
        yfactor = float(param_dict["boxsize"].get().split(",")[1])
    elif isinstance(param_dict, list):
        for item in param_dict:
            if item.split("=")[0] == "boxsize":
                xfactor = float(item.split("=")[1].split(",")[0])
                yfactor = float(item.split("=")[1].split(",")[1])
    cursor_xmin = 15 * xfactor
    cursor_xmax = 108 * xfactor
    cursor_ymin = 107 * yfactor
    cursor_ymax = 15 * yfactor
    if int(x) < cursor_xmin:
        x = cursor_xmin
    elif int(x) > cursor_xmax:
        x = cursor_xmax
    if int(y) < cursor_ymax:
        y = cursor_ymax
    elif int(y) > cursor_ymin:
        y = cursor_ymin

    xmin, xmax = ax1.get_xlim()
    ymin, ymax = ax1.get_ylim()

    x = xmin + (x - cursor_xmin) * (xmax - xmin) / (cursor_xmax - cursor_xmin)
    y = ymin + (y - cursor_ymin) * (ymax - ymin) / (cursor_ymax - cursor_ymin)
    execution["initial_coordinates"].destroy()
    execution["coordinates"] = tk.Label(root, text=f"x={x:.3f} y={y:.3f}")
    execution["coordinates"].grid(row=10, column=1, sticky=tk.S)


# Get Info


def obtain_boxsizes(parameters):
    for word in parameters:
        if word.split("=")[0] == "boxsize":
            scale_window_x = float(word.split("=")[1].split(",")[0])
            scale_window_y = float(word.split("=")[1].split(",")[1])
            if scale_window_x < 2:
                scale_window_x = 2
    return scale_window_x, scale_window_y


def add_text_converter(add_text_dict: dict[int, list[str]], add_text) -> None:
    """Convert the x and y additional text coordinates to floating point numbers.

    This function modifies `add_text` in place.

    Args:
        add_text_dict: A dictionary mapping integers to lists of strings specifying additional text/formatting.
        add_text: `add_text_dict` but flat and with x/y coordinates as floats.
    """
    dict_sorted = dict(sorted(add_text_dict.items()))
    add_text.clear()
    for value in dict_sorted.values():
        add_text.append([float(value[0]), float(value[1]), *value[2:]])
