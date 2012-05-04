#!/usr/bin/python
#
# mydisplay   Module of wxpoly.py program
#
#                Functions and a function pointer class necessary to draw
#                   polygon objects on canvas.
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

""" mydisplay module : Functions and a function pointer class necessary to draw
    polygon objects on canvas.
"""


__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####    Import Modules
#
# ---   General
import sys
from math import  pi, cos
try:
    import wx
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()


#### functions to draw polygon objects
#
def _circ(ngon, obj, canvas, rts_unity):
    """Internal function to draw Circuscribe circle."""
    canvas.SetBrush(wx.Brush(ngon.view["Circumscribe"]['paper']))
    canvas.DrawCircle(0, 0, ngon.poly_data.scale)

def _insc(ngon, obj, canvas, rts_unity):
    """Internal function to draw Inscribed circle."""
    try:
        inradius = ngon.poly_data.scale * cos(pi/ngon.poly_data.vertices)
    except ZeroDivisionError:
        #   degenerate case where n= 0
        inradius = 0
    canvas.SetBrush(wx.Brush(ngon.view['Inscribe']['paper']))
    canvas.DrawCircle(0, 0, inradius)

def _verts(ngon, obj, canvas, rts_unity):
    """Internal function to draw vertices"""
    for k in range(ngon.poly_data.vertices):
        canvas.DrawCircle(rts_unity[k].real, rts_unity[k].imag, 1)

def _center(ngon, obj, canvas, rts_unity):
    """Internal function to draw center"""
    canvas.DrawCircle(0, 0,  obj["size"])

def _axis(ngon, obj, canvas, rts_unity):
    """Internal function to draw axis."""
    canvas.CrossHair(0, 0)

def _sides(ngon, obj, canvas, rts_unity):
    """Internal function to draw polygon sides."""
    if ngon.poly_data.vertices > 1:
        canvas.DrawLinePoint((rts_unity[ngon.poly_data.vertices - 1].real, \
                        rts_unity[ngon.poly_data.vertices - 1].imag) , \
                        (rts_unity[0].real, rts_unity[0].imag))
    for k in range(ngon.poly_data.vertices - 1):
        if k+1 < ngon.poly_data.vertices :
            canvas.DrawLinePoint((rts_unity[k].real, \
                            rts_unity[k].imag), (rts_unity[k+1].real, \
                            rts_unity[k+1].imag))

def _diags(ngon, obj, canvas, rts_unity):
    """Internal function to draw polygon diagonals."""
    if ngon.poly_data.vertices > 3:
        for k in range(ngon.poly_data.vertices):
            for cur in range (k+2, ngon.poly_data.vertices):
                test_flag = cur - k + 1
                if not (test_flag == ngon.poly_data.vertices):
                    canvas.DrawLinePoint((rts_unity[k].real,
                        rts_unity[k].imag), \
                        (rts_unity[cur].real, rts_unity[cur].imag))

#### Class to store function pointers in
#
class ObjDraw :
    """ObjDraw class stores pointers to functions that
        draw the objects that make up our polygon.
        Class supports iteration and numeric index.

    """

    def __init__(self):
        self.n = -1
        self.fn_list =   [None, _circ, _insc, _center, _verts, _diags, _sides, _axis ]

    def __iter__(self):
        return self

    def next(self):
        """Iterate thru function pointers."""
        if self.n ==  len(self.fn_list) -1:
            self.n = -1
            raise StopIteration
        self.n = self.n + 1
        return self.fn_list[self.n]

    def __getitem__(self, index):
        try:
            return self.fn_list[index]
        except IndexError:
            sys.stderr.write( "wxpoly: object index out of range " + str(index) + "\n")
            return self.fn_list[0]

    def __len__(self):
        return len(self.fn_list)

    def get_name(self, index):
        """Returns name of the function at position index in list."""
        return self.fn_list[index]


# Someone is launching this directly
if __name__ == "__main__":

    print "\nmydisplay module --- wxpoly \n"
    d = ObjDraw()
    print "     iteration test\n"
    for a in d:
        print a
    print "\n     Index test\n"
    for a in range(len(d)):
        print a, d[a]



