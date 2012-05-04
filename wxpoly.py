#!/usr/bin/python

# wxpoly.py
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

""" Main Entry Point of wxPoly Application
        wxPoly is a simple wxPython application designed to demonstrate the mathematics
        of regular Polygons in The Guasian plane as Well as explore basic wxPython API

"""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####    Import Modules
#
# ---   General
import os
import sys
try:
    import wx
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()

# ---   My modules
try:
    import gpoly
    import myapp
    import myopts
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()

####    Main Entry Point of wxpoly Application
#
# ---       Initialize data
pn = os.path.dirname(sys.argv[0])
current_path = str(os.path.abspath(pn))
n, scale, rotation = myopts.command_line_arguments()
polygon = gpoly.Graphical(gpoly.Basic(n, scale, rotation), current_path)

# ---        Launch Application
app = wx.App()
myapp.Ngon(None, -1, 'Polygon Generator', polygon)
app.MainLoop()

# ---       On second thought, let's not go to Camelot. It is a silly place.
