#!/usr/bin/python
#
# show.py   Module of wxpoly.py program
#
#
#               Defintion of View Preference class
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

"""show module for viewer preferences to store color and style data on polygon objects.
   Specifically stores name, visibility flag, style, ink and display functions for
   the objects that make up our polygon.
        """

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####    Import Modules
#
# ---   General
import sys
try:
    import wx
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()
#
# ---   My modules
try:
    import mydisplay
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()



#### Preference Class
#
#
class Preference :
    """Preference class for viewer preferences to store data on polygon objects.
        Specifically stores name, visibility flag, style, ink and display functions for
        the objects that make up our polygon.
        Class supports iteration and key index.

    """
    ###     Initialize Preference class
    #
    def __init__(self):

        #           index postition for iteration support
        self.n = -1
        #       Data used by initialize internal Dictionary for Preference Class
        self.polygon_objs = ["Background", "Circumscribe", "Inscribe",
                                "Center", "Vertices", "Diagonals",
                                    "Sides", "Axis"]
        self.polygon_color = ["white", "blue", "medium violet red",
                                "sky blue", "black", "black", "blue", "grey"]
        #        Background visibility is set to False, this avoids onPaint calling
        #           display Function for background
        self.polygon_vis =   [False, True, False, False,  False, True,
                                    True, False]
        self.polygon_style = [wx.SOLID, wx.DOT_DASH, wx.DOT_DASH,
                                 wx.SOLID, wx.SOLID, wx.SOLID,
                                    wx.SOLID, wx.SOLID]
        display_fns_pointers = mydisplay.ObjDraw()

        #       Initialize Internal  Dictionary
        bg_color = self.polygon_color[0]
        self.dict_pref = dict()
        for obj in range(len(self.polygon_objs)):
            name = self.polygon_objs[obj]
            visiblity = self.polygon_vis[obj]
            style = self.polygon_style[obj]
            ink = self.polygon_color[obj]
            display_fn = display_fns_pointers[obj]
            self.dict_pref[name] = {"name" : name, "n":5, "isVisible": visiblity, "size":1,
                "style" : style, "ink": ink, "paper":  bg_color, "display": display_fn}

    ###                Iteration support
    #
    def __iter__(self):
        return self

    def next(self):
        """Provide Iteration support."""
        if self.n ==  len(self.polygon_objs) -1:
            self.n = -1
            raise StopIteration
        self.n = self.n + 1
        return self.get_byindex(self.n)

    ###     Index Support
    #
    #
    def __getitem__(self, name):
        """Helps provide iteration support."""
        return self.dict_pref[name]

    def get_byindex(self, index):
        """Returns object preference dictionary from index."""
        return self.dict_pref[self.polygon_objs[index]]

    def _get_index(self, name):
        """Returns index in polygon objects list of obj with a given name."""
        for cur in range(len(self.polygon_objs)):
            if self.polygon_objs[cur] == name:
                return cur

    ###     Support functions for Preference
    #
    def is_visible(self, obj):
        """Returns True if obj is visible, False otherwise."""
        return self.dict_pref[obj]["isVisible"]
    def toggle_visiblity(self, obj):
        """Toggles Visibility flag for obj."""
        self.dict_pref[obj]["isVisible"] = not self.dict_pref[obj]["isVisible"]
    def restore_default(self):
        """Restore Preference data to default state."""
        self.__init__()
    def restore_default_color(self):
        """Restore Preference color data to default state."""
        for cur in self.dict_pref:
            self.dict_pref[cur]['ink'] = self.polygon_color[self._get_index(cur)]

####        Display Function
#
#
def display(ngon, obj, canvas, rts_unity):
    """Calls the display function for polygon object."""
    try:
        obj["display"](ngon, obj, canvas, rts_unity)
    except TypeError:
        sys.stderr.write( "wxpoly: TypeError    obj = " + str( obj) +"\n")


# Someone is launching this directly
# if __name__ == "__main__":

