# mymenu.py
#
#                Initialize Ngon application menu
#
#                create_menu_bar(self)
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

""" Functions to Initialize Ngon application menu.
        Used in wxPoly project

                 create_menu_bar(self).

"""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

#### Import Modules
#
# --- General
import sys
try:
    import wx
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()


def _m_data(self):
    """ Function to return menu list"""
    return [("&File", (
                ("&New\tCtrl+N", "Create New Polygon", self._on_new_poly),
                ("&Open\tCtrl+O", "Open file", self._on_open),
                ("", "", ""),
                ("&Save\tCtrl+S", "Save File", self._on_save),
                ("S&ave As\tCtrl+A", "Save File as", self._on_save),
                ("Export", "Save as image", self._on_export),
                ("", "", ""),
                ("&Quit\tCtrl+Q", "Exit program", self._on_quit))),
           ("&Edit",(
                ("Set n", "Polygon Data", self._on_new_n),
                ("Set radius", "Polygon Data", self._on_new_radius),
                ("Set angle", "Polygon Data", self._on_new_rotation),
                ("Pr&ef\tCtrl+E", "Program Preferences", self._on_new_pref))),
                ("", "", ""),
           ("&View", (
                ("Center", "Show Center", self._show_center, wx.ITEM_CHECK,
                        self.view.is_visible("Center")),
                ("", "", ""),
                ("Vertices", "Show Vertices", self._show_vertices,
                        wx.ITEM_CHECK, self.view.is_visible("Vertices")),
                ("Sides", "Show Sides", self._show_sides, wx.ITEM_CHECK,
                        self.view.is_visible("Sides")),
                ("Diagonals", "Show Diagonals", self._show_diags,
                        wx.ITEM_CHECK, self.view.is_visible("Diagonals") ),
                ("", "", ""),
                ("Circumscribe", "Circumscribed Circle", self._show_circ,
                        wx.ITEM_CHECK, self.view.is_visible("Circumscribe")),
                ("Inscribe", "Inscribed Circle", self._show_ins, wx.ITEM_CHECK,
                         self.view.is_visible("Inscribe") ),
                ("", "", ""),
                ("Show Axis", "Show Axis", self._show_axis, wx.ITEM_CHECK,
                        self.view.is_visible("Axis") ))),
           ("&Polygon", (
                ("&Random\tCtrl+R", "Set Random pentagon", self._on_new_rnd),
                ("", "", ""),
                ("Nex&t\tCtrl+T", "Next Polygon", self._on_next),
                ("&Previous\tCtrl+P", "Previous Polygon", self._on_prev),
                ("", "", ""),
                ("&Wicca\tCtrl+W", "Set to pentagon", self._on_wicca))),
           ("&Help", (
                ("&Contents\tCtrl+C", "Contents", self._on_help),
                ("", "", ""),
                ("&About\tCtrl+A", "About", self._on_about)))]

def create_menu_bar(self):
    """Wrapper for wx.MenuBar."""
    menu_bar = wx.MenuBar()
    for each_m_data in _m_data(self):
        m_label = each_m_data[0]
        m_items = each_m_data[1]
        menu_bar.Append(create_menu(self, m_items), m_label)
    self.SetMenuBar(menu_bar)

def create_menu(self, menu_data):
    """ Creates a wx.Menu"""
    menu = wx.Menu()
    for cur in menu_data:
        if len(cur) == 2:
            label = cur[0]
            sub_menu = create_menu(self, cur[1])
            menu.AppendMenu(wx.NewId(), label, sub_menu)
        else:
            create_menu_item(self, menu, *cur)
    return menu

def create_menu_item(self, menu, label, status, handler, kind=wx.ITEM_NORMAL,
                         checked = False):
    """ Helper function for create_menu."""
    if not label:
        menu.AppendSeparator()
        return
    menu_item = menu.Append(-1, label, status, kind)
    if checked:
        menu_item.Check(True)
    self.Bind(wx.EVT_MENU, handler, menu_item)

