"""DearPyGui's simple contains wrappings of the core API.
"""
from contextlib import contextmanager
from typing import List, Any, Callable, Union
import dearpygui.core as internal_dpg

########################################################################################################################
# context manager container wrappers
########################################################################################################################


@contextmanager
def managed_columns(name: str, columns: int, border: bool = True, show: bool = True, parent: str = "",
                    before: str = ""):
    """Wraps add_managed_columns() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        columns: The number of columns to be created.
        border: Shows a border.
        show: Decides if the item is shown of not.
        parent: Parent this item will be added to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        yield internal_dpg.add_managed_columns(name, columns, border=border, show=show, parent=parent, before=before)

    finally:
        internal_dpg.end()


@contextmanager
def window(name: str, width: int = 200, height: int = 200, x_pos: int = 200, y_pos: int = 200, autosize: bool = False,
           no_resize: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False,
           no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False,
           no_bring_to_front_on_focus: bool = False, menubar: bool = False, no_close: bool = False,
           no_background: bool = False, label: str = "__DearPyGuiDefault", show: bool = True,
           on_close: Callable = None):
    """Wraps add_window() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        width: Width of the item.
        height: Height of the item.
        x_pos: x position the window will start at
        y_pos: y position the window will start at
        autosize: Autosized the window to fit it's items.
        no_resize: Allows for the window size to be changed or fixed
        no_title_bar: Title name for the title bar of the window
        no_move: Allows for the window's position to be changed or fixed
        no_scrollbar: Disable scrollbars (window can still scroll with mouse or programmatically)
        no_collapse: Disable user collapsing window by double-clicking on it
        horizontal_scrollbar: Allow horizontal scrollbar to appear (off by default).
        no_focus_on_appearing: Disable taking focus when transitioning from hidden to visible state
        no_bring_to_front_on_focus: Disable bringing window to front when taking focus (e.g. clicking on it or
            programmatically giving it focus)
        menubar: Decides if the menubar is shown or not.
        no_close: Decides if the window can be closed.
        no_background:
        label: Displayed name of the item.
        show: sets if the item is shown or not window.
        on_close: Callback ran when window is closed

    Returns:
        None
    """
    try:
        if label == "__DearPyGuiDefault":
            yield internal_dpg.add_window(name, width=width, height=height, x_pos=x_pos, y_pos=y_pos, autosize=autosize,
                                          no_resize=no_resize, no_title_bar=no_title_bar, no_move=no_move,
                                          no_scrollbar=no_scrollbar, no_collapse=no_collapse,
                                          horizontal_scrollbar=horizontal_scrollbar,
                                          no_focus_on_appearing=no_focus_on_appearing,
                                          no_bring_to_front_on_focus=no_bring_to_front_on_focus,
                                          menubar=menubar, no_close=no_close, no_background=no_background,
                                          show=show, on_close=on_close)
        else:
            yield internal_dpg.add_window(name, width=width, height=height, x_pos=x_pos, y_pos=y_pos, autosize=autosize,
                                          no_resize=no_resize, no_title_bar=no_title_bar, no_move=no_move,
                                          no_scrollbar=no_scrollbar, no_collapse=no_collapse,
                                          horizontal_scrollbar=horizontal_scrollbar,
                                          no_focus_on_appearing=no_focus_on_appearing,
                                          no_bring_to_front_on_focus=no_bring_to_front_on_focus,
                                          menubar=menubar, no_close=no_close,
                                          no_background=no_background, label=label, show=show, on_close=on_close)
    finally:
        internal_dpg.end()


@contextmanager
def menu_bar(name: str, show: bool = True, parent: str = "", before: str = ""):
    """Wraps add_menu_bar() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        show: Decides if the item is shown of not.
        parent: Parent this item will be added to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        yield internal_dpg.add_menu_bar(name, show=show, parent=parent, before=before)
    finally:
        internal_dpg.end()


@contextmanager
def menu(name: str, label: str = "__DearPyGuiDefault", show: bool = True, tip: str = "", parent: str = "",
         before: str = "", enabled: bool = True):
    """Wraps add_menu() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        label: Displayed name of the item.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip
        parent: Parent this item will be added to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        enabled: Will enable or disable the menu.

    Returns:
        None
    """
    try: 
        if label == "__DearPyGuiDefault":
            yield internal_dpg.add_menu(name, show=show, tip=tip, parent=parent, before=before, enabled=enabled)
        else:
            yield internal_dpg.add_menu(name, label=label, show=show, tip=tip, parent=parent,
                                        before=before, enabled=enabled)
    finally:
        internal_dpg.end()


@contextmanager
def child(name: str, show: bool = True, tip: str = "", parent: str = "", before: str = "", width: int = 0,
          height: int = 0, border: bool = True, popup: str = "", autosize_x: bool = False, autosize_y: bool = False,
          no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False):
    """Wraps add_child() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        width: Width of the item.
        height: Height of the item.
        border: Shows/Hides the border around the sides
        popup: Name of the popup that will be tied to this item.
        autosize_x: Autosize the window to fit its items in the x.
        autosize_y: Autosize the window to fit its items in the y.
        no_scrollbar: Disable scrollbars (window can still scroll with mouse or programmatically)
        menubar: adds a bar to add menus

    Returns:
        None
    """
    try: 
        yield internal_dpg.add_child(name, show=show, tip=tip, parent=parent, before=before, width=width,
                                     height=height, border=border, popup=popup, autosize_x=autosize_x, autosize_y=autosize_y,
                                     no_scrollbar=no_scrollbar, horizontal_scrollbar=horizontal_scrollbar,
                                     menubar=menubar)
    finally:
        internal_dpg.end()


@contextmanager
def collapsing_header(name: str, label: str = "__DearPyGuiDefault", show: bool = True, 
                      tip: str = "", parent: str = "", before: str = "",closable: bool = False, 
                      default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, 
                      leaf: bool = False, bullet: bool = False):
    """Wraps add_collapsing_header() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        label: Displayed name of the item.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        closable: Decides if the header can be collapsed.
        default_open: Decides if item is open by default.
        open_on_double_click: Need double-click to open node.
        open_on_arrow: Only open when clicking on the arrow part.
        leaf: No collapsing, no arrow (use as a convenience for leaf nodes).
        bullet: Display a bullet instead of arrow.


    Returns:
        None
    """
    try:
        if label == "__DearPyGuiDefault":
            yield internal_dpg.add_collapsing_header(name, show=show, tip=tip, parent=parent, before=before, 
                                                     closable=closable, default_open=default_open, 
                                                     open_on_double_click=open_on_double_click,
                                                     open_on_arrow=open_on_arrow, leaf=leaf, bullet=bullet)
        else:
            yield internal_dpg.add_collapsing_header(name, show=show, tip=tip, parent=parent, before=before, 
                                                     closable=closable, default_open=default_open, 
                                                     open_on_double_click=open_on_double_click,
                                                     open_on_arrow=open_on_arrow, leaf=leaf, bullet=bullet)
    finally:
        internal_dpg.end()


@contextmanager
def group(name: str, show: bool = True, tip: str = "", parent: str = "", before: str = "", width: int = 0,
          horizontal: bool = False, horizontal_spacing: float = -1.0, popup: str = ""):
    """Wraps add_group() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        width: Width of the item.
        horizontal: Adds the items on the same row by default.
        horizontal_spacing: Decides the spacing for the items.
        popup: Name of the popup that will be tied to this item.

    Returns:
        None
    """
    try:
        yield internal_dpg.add_group(name, show=show, tip=tip, parent=parent, before=before, width=width,
                                     horizontal=horizontal, horizontal_spacing=horizontal_spacing, popup=popup)
    finally:
        internal_dpg.end()


@contextmanager
def tab_bar(name: str, reorderable: bool = False, callback: str = "", callback_data: str = "",  show: bool = True,
            parent: str = "", before: str = ""):
    """Wraps add_tab_bar() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        reorderable: Allows for moveable tabs.
        callback: Registers a callback.
        callback_data: Callback data.
        show: Decides if the item is shown of not.
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        yield internal_dpg.add_tab_bar(name, reorderable=reorderable, callback=callback, callback_data=callback_data,
                                       show=show, parent=parent, before=before)
    finally:
        internal_dpg.end()


@contextmanager
def tab(name: str, closable: bool = False, label: str = "__DearPyGuiDefault", show: bool = True, tip: str = "",
        parent: str = "", before: str = ""):
    """Wraps add_tab() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        closable: creates a button on the tab that can hide the tab.
        label: Displayed name of the item.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip.
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        if label == "__DearPyGuiDefault":
            yield internal_dpg.add_tab(name, closable=closable, show=show, tip=tip, parent=parent, before=before)
        else:
            yield internal_dpg.add_tab(name, closable=closable, label=label, show=show, tip=tip, parent=parent,
                                       before=before)
    finally:
        internal_dpg.end()


@contextmanager
def tree_node(name: str, label: str = "__DearPyGuiDefault", show: bool = True, tip: str = "", parent: str = "", 
              before: str = "", default_open: bool = False, open_on_double_click: bool = False, 
              open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False):
    """Wraps add_tree_node() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        label: Displayed name of the item.
        show: Decides if the item is shown of not.
        tip: Adds a simple tooltip.
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        default_open: Decides if item is open by default.
        open_on_double_click: Need double-click to open node.
        open_on_arrow: Only open when clicking on the arrow part.
        leaf: No collapsing, no arrow (use as a convenience for leaf nodes).
        bullet: Display a bullet instead of arrow.

    Returns:
        None
    """
    try:
        if label == "__DearPyGuiDefault":
            yield internal_dpg.add_tree_node(name, show=show, tip=tip, parent=parent,
                                             before=before, default_open=default_open, 
                                             open_on_double_click=open_on_double_click, 
                                             open_on_arrow=open_on_arrow,
                                             leaf=leaf, bullet=bullet)
        else:
            yield internal_dpg.add_tree_node(name, show=show, tip=tip, parent=parent,
                                             before=before, default_open=default_open, 
                                             open_on_double_click=open_on_double_click, 
                                             open_on_arrow=open_on_arrow,
                                             leaf=leaf, bullet=bullet)
    finally:
        internal_dpg.end()


@contextmanager
def tooltip(tipparent: str, name: str, parent: str = "", before: str = "", show: bool = True):
    """Wraps add_tooltip() and automates calling end().

    Args:
        tipparent: Sets the item's tool tip to be the same as the named item's tool tip.
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        show: Decides if the item is shown of not.

    Returns:
        None
    """
    try:
        yield internal_dpg.add_tooltip(tipparent, name, parent=parent, before=before, show=show)
    finally:
        internal_dpg.end()


@contextmanager
def popup(popupparent: str, name: str, mousebutton: int = 1, modal: bool = False, parent: str = "", 
          before: str = "", width: int = 0, height: int = 0, show: bool = True):
    """Wraps add_popup() and automates calling end().

    Args:
        popupparent: Parent that the popup will be assigned to.
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        mousebutton: The mouse code that will trigger the popup. Default is 1 or mvMouseButton_Right.
            (mvMouseButton_Left, mvMouseButton_Right, mvMouseButton_Middle, mvMouseButton_X1, mvMouseButton_X2)
        modal: Makes the popup modal.
        parent: Parent to add this item to. (runtime adding)
        before: This item will be displayed before the specified item in the parent. (runtime adding)
        width: Width of the item.
        height: Height of the item.
        show: Decides if the item is shown of not.

    Returns:
        None
    """
    try:
        yield internal_dpg.add_popup(popupparent, name, mousebutton=mousebutton, modal=modal, parent=parent,
                                     before=before, width=width, height=height, show=show)
    finally:
        internal_dpg.end()

########################################################################################################################
# Old Commands
########################################################################################################################


# window configure
def set_window_pos(window: str, x: int, y: int):
    """Sets the top left corner of the window to the specified position.

    Args:
        window: Parent that the popup will be assigned to.
        x: The x position.
        y: The y position.

    Returns:
        None
    """
    internal_dpg.configure_item(window, x_pos=x, y_pos=y)


def get_window_pos(window: str) -> Union[List[int], None]:
    """Gets the top left corner of the window to the specified position.

    Args:
        window: Parent that the popup will be assigned to.
        x: The x position.
        y: The y position.

    Returns:
        list as [x,y] or None
    """
    config = internal_dpg.get_item_configuration(window)
    return [config["x_pos"], config["y_pos"]]


def show_item(item: str):
    """Shows the item.

    Args:
        item: Item to show.

    Returns:
        None
    """
    internal_dpg.configure_item(item, show=True)


def hide_item(item: str, children_only: bool = False):
    """Hides the item.

    Args:
        item: Item to hide.

    Returns:
        None
    """
    if children_only:
        children = internal_dpg.get_item_children(item)
        for child in children:
            internal_dpg.configure_item(child, show=False)
    else:
        internal_dpg.configure_item(item, show=False)


# item configure commands
def set_item_name(item: str, name: str):
    """Sets the item's name, anything after the characters "##" in the name will not be shown.

        If no label is specified then by default this will be the displayed label.

    Args:
        item: Item name will be applied to.
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.

    Returns:
        None
    """
    internal_dpg.configure_item(item, name=name)


def set_item_label(item: str, label: str):
    """Sets the item's displayed label, anything after the characters "##" in the name will not be shown.

    Args:
        item: Item label will be applied to.
        label: Displayed name of the item.

    Returns:
        None
    """
    internal_dpg.configure_item(item, label=label)


def set_item_popup(item: str, popup: str):
    """Sets the item's popup.

    Args:
        item: Item the Popup will be applied to.
        popup: Popup to be applied.

    Returns:
        None
    """
    internal_dpg.configure_item(item, popup=popup)


def set_item_tip(item: str, tip: str):
    """Sets the item's tip.

    Args:
        item: Item the tip will be applied to.
        tip: tip to be applied.

    Returns:
        None
    """
    internal_dpg.configure_item(item, tip=tip)


def set_item_width(item: str, width: int):
    """Sets the item's width.

    Args:
        item: Item the Width will be applied to.
        width: Width of the item. width to be applied.

    Returns:
        None
    """
    internal_dpg.configure_item(item, width=width)


def set_item_height(item: str, height: int):
    """Sets the item's height.

    Args:
        item: Item the Height will be applied to.
        height: Height of the item. height to be applied.

    Returns:
        None
    """
    internal_dpg.configure_item(item, height=height)


def get_item_label(item: str) -> Union[str, None]:
    """Gets the item's label.

    Returns:
        label as a string or None
    """
    return internal_dpg.get_item_configuration(item)["label"]


def get_item_popup(item: str) -> Union[str, None]:
    """Gets the item's popup.

    Returns:
        popup as a string or None
    """
    return internal_dpg.get_item_configuration(item)["popup"]


def get_item_tip(item: str) -> Union[str, None]:
    """Gets the item's tip.

    Returns:
        tip as a string or None
    """
    return internal_dpg.get_item_configuration(item)["tip"]


def get_item_width(item: str) -> Union[int, None]:
    """Gets the item's width.

    Returns:
        width as a int or None
    """
    return internal_dpg.get_item_configuration(item)["width"]


def get_item_height(item: str) -> Union[int, None]:
    """Gets the item's height.

    Returns:
        height as a int or None
    """
    return internal_dpg.get_item_configuration(item)["height"]


# drawing configure commands
def set_drawing_origin(drawing: str, x: float, y: float):
    """Sets the drawing's origin (the bottom left corner) to the specified position.

    Args:
        drawing: Drawing that will be set.
        x: x position to set
        y: y position to set

    Returns:
        None
    """
    internal_dpg.configure_item(drawing, originx=x, originy=y)


def set_drawing_scale(drawing: str, x: float, y: float):
    """Sets the drawing's scale.

    Args:
        drawing: Drawing that will be set.
        x: x scale to set
        y: y scale to set

    Returns:
        None
    """
    internal_dpg.configure_item(drawing, scalex=x, scaley=y)


def set_drawing_size(drawing: str, width: int, height: int):
    """Sets the drawing's size, width and height.

    Args:
        drawing: Drawing that will be set.
        width: x axis width to set
        height: y axis height to set

    Returns:
        None
    """
    internal_dpg.configure_item(drawing, width=width, height=height)


def get_drawing_origin(drawing: str) -> Union[List[float], None]:
    """Gets the drawing's origin, (bottom left corner).

    Args:
        drawing: Drawing that will be set.

    Returns:
        list as [x,y] or None
    """
    config = internal_dpg.get_item_configuration(drawing)
    return [config["originx"], config["originy"]]


def get_drawing_scale(drawing: str) -> Union[List[float], None]:
    """Gets the drawing's scale.

    Args:
        drawing: Drawing that will be set.

    Returns:
        list as [x,y] or None
    """
    config = internal_dpg.get_item_configuration(drawing)
    return [config["scalex"], config["scaley"]]


def get_drawing_size(drawing: str) -> Union[List[int], None]:
    """Gets the drawing's scale.

    Args:
        drawing: Drawing that will be set.

    Returns:
        list as [width, height] or None
    """
    config = internal_dpg.get_item_configuration(drawing)
    return [config["width"], config["height"]]