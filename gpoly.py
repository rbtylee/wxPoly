
# gpoly       Module of wxpoly.py program
#
#                Defintion of Geometric Polygon class
#
#                gPoly(n, rotation, scale, center)
#
#              This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

""" Basic polygon class -- Basic Geometric polygon class contains
                                        n, rotational angle, scale and center.

    All aruments are optional and in this case or in case or error returns default Polygon

            gPoly()
            gPoly(n, rotation, scale, center)

    Graphical Polygon class  contains a Basic polygon object as well as pathname
    and a show.Preference object which stores viewer preferences for color visibility and so on.

        Graphical( poly_data, pathname, preferences)

 """

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####Import Modules
#
# --- General
import sys
import math
# --- My modules
try:
    import show
    import config
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()

#### gPoly Class
#
#
class Basic:
    """Geometric polygon class contains n, rotational angle, scale and center.
            All aruments are optional and in this case or in case or error returns default Polygon

            Basic()
            Basic(n, rotation, scale, center)

            """
    def __init__(self, vertex_number = config.default_dict["vert_default"],
                rotation= config.default_dict["rotation_default"],
                scale= config.default_dict["scale_default"],
                center= config.default_dict["center_default"] ):
        """Initialize Basic polygon class"""
        if (type( vertex_number)  is int and  vertex_number >= config.default_dict["vert_min"]
                and  vertex_number <= config.default_dict["vert_max"]) :
            self.vertices = vertex_number
        else:
            self.vertices = config.default_dict["vert_default"]
            raise ValueError
        if type(rotation)  is int or type(rotation) is float:
            self.rotation = math.pi* (rotation % 360)/180
        else:
            self.rotation = math.pi* (config.default_dict["rotation_default"])/180
            raise ValueError
        if (scale >= config.default_dict["scale_min"] and \
                scale <= config.default_dict["scale_max"] ) \
                and (type(scale)  is int or type(scale) is float) :
            self. scale = scale
        else:
            self.scale = config.default_dict["scale_default"]
            raise ValueError
        if type(center)  is complex :
            self.center = center
        else:
            self.center = config.default_dict["center_default"]
            raise ValueError

    def out(self):
        """Print all polygon data"""
        print "     n         = %d" %  self.vertices
        print "     rotation  = %f" %  self.rotation
        print "     scale     = %d" %  self.scale
        print "     center    = (%f, %f) " % (self.center.real, self.center.imag)


    def return_n(self):
        """Returns number of vertices of the polygon."""
        return(self.vertices)

    def return_scale(self):
        """Returns polygon scale."""
        return(self.scale)

    def return_rotation(self):
        """Returns rotation of the polygon"""
        return(self.rotation)

#### Simple minded class to store polygon data in
#
class Graphical:
    """Graphical polygon class to store polygon data, pathname and graphical preferences."""
    def __init__(self, poly_data, pathname, pref = None):

        self.poly_data = poly_data
        self.pathname = pathname
        if pref is None:
            self.pref = show.Preference()
        else:
            self.pref = pref

    def get_basic_polygon(self):
        """Return polygon data class."""
        return(self.poly_data)

    def get_pathname(self):
        """Returns current pathname."""
        return(self.pathname)

    def get_preferences(self):
        """Returns graphical prefernces for polygon objects."""
        return(self.pref)

if __name__ == "__main__":
    # Someone is launching this directly
    poly = Basic( )
    poly.out()
    #test graphical
