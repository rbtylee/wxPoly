# -*- coding: latin-1 -*-

# resource       Module of wxpoly.py program
#
#              This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

"""myresource module: Attempt to keep program language dependent resources
    seperate from all modules."""

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

PolyNames = ["dev/null", "point", "line segment", "equilateral triangle",
             "square", "pentagon", "hexagon", "heptagon", "octagon",
             "enneagon", "decagon", "hendecagon", "dodecagon",
             "tridecagon", "tetradecagon", "pendedecagon", "hexdecagon",
             "heptdecagon", "octdecagon", "enneadecagon", "icosagon"]

# see http://www.wxpython.org/onlinedocs.php for reference
pen_styles = [wx.SOLID, wx.TRANSPARENT, wx.DOT, wx.LONG_DASH, wx.SHORT_DASH,
              wx.DOT_DASH, wx.STIPPLE, wx.USER_DASH, wx.BDIAGONAL_HATCH,
              wx.CROSSDIAG_HATCH, wx.FDIAGONAL_HATCH, wx.CROSS_HATCH,
              wx.HORIZONTAL_HATCH, wx.VERTICAL_HATCH]

pen_style_names = ["solid", "transparent", "dot", "long dash", "short dash",
                   "dot dash", "stipple", "user dash", "bdiagonal hatch",
                   "crossdiaghatch", "fdiagonal hatch", "cross hatch",
                   "horizontal hatch", "vertical hatch"]

color_names = ["aquamarine", "black", "blue", "blue violet", "brown",
               "cadet blue", "coral", "cornflower blue", "cyan",
               "dark grey", "dark green", "dark olive green",
               "dark orchid", "dark slate blue", "dark slate grey",
               "dark turquoise", "dim grey", "firebrick", "forest green",
               "gold", "goldenrod", "grey", "green", "green yellow",
               "indian red", "khaki", "light blue", "light grey",
               "light steel blue", "lime green", "magenta", "maroon",
               "medium aquamarine", "medium blue",  "medium forest green",
               "medium goldenrod", "medium orchid","medium sea green",
               "medium slate blue", "medium spring green", "medium turquoise",
               "medium violet red", "midnight blue", "navy", "orange",
               "orange red", "orchid", "pale green", "pink", "plum", "purple",
               "red", "salmon", "sea green", "sienna", "sky blue", "slate blue",
               "spring green", "steel blue", "tan", "thistle", "turquoise",
               "violet", "violet red", "wheat", "white", "yellow", "yellow green"]

#### page list
#                       Holds HTML for About dialog
#
page = [ '<html><body> \
<p align = "center"><font color ="blue" size ="+3"><i>wxPoly version2</i></font></p> \
<center><img src ="images/homer.png"></center> \
<p align = "center"><font color ="black"><i>wxPoly is a simple wxPython application </i></font></p> \
<p align = "center"><font color ="black"><i>designed to demonstrate the mathematics</i></font></p> \
<p align = "center"><font color ="black"><i>of regular Polygons in The Guasian plane</i></font></p> \
<p align =  "center"><font color ="black"><br><i>As Well as explore basic wxPython API</i></font></p> \
<p align =  "center"><br><font color ="gray"  size ="+1"><i>© y-lee</i></font></p> \
</body></table></html>',

    '<html><body> \
<center><img src ="images/stoned2.jpg"></center> \
<p align = "center"><font color ="blue" size ="+3"><i>wxPoly version2</i></font></p> \
<p align = "center"><br><br><font color ="red" size ="+3"><i>Free as in Freedom</i></font></p> \
<p align = "center"><br><br><font color ="gray" size = "+1"><i>© y-lee</i></font></p> \
</body></table></html>']



