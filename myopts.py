#!/usr/bin/python
#
# myopts   Module of wxpoly.py program
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.
"""Module to process wxpoly command line options."""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####    Import Modules
#
# ---   General
import sys
try:
    import argparse
except ImportError:
    print "Error: wxpoly requires the argparse module."
    print "Users of python prior to 2.7 need to install it."
    print "\tsudo pip install argparse"
    sys.exit()

# --- My modules
try:
    import config
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()

def command_line_arguments():
    """Reads Command line options and returns n, scale and angle
         using defaults if necessary.Used in wxpoly project.

    """
    vertices = config.default_dict["vert_default"]
    rotation = config.default_dict["rotation_default"]
    scale = config.default_dict["scale_default"]
    parser = argparse.ArgumentParser(
                description='A Simple wxPython polygon generating application.',
                epilog="(c) Rbt. Y-Lee")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0.1')
    parser.add_argument("-n", "--number", type=int, dest="num",
                                    help="Number of polygon vertices", metavar="num")
    parser.add_argument("-s", "--scale", type=float, dest="scale" ,
                                    help="Polygon scale size", metavar="num")
    parser.add_argument("-r", "--rotation", type=float, dest="angle",
                                    help="Rotational Angle for polygon", metavar="num")
    args = parser.parse_args()
    options_dict = vars(args)

    for key, value in options_dict.items():
        if options_dict[key]:
            if key == "num":
                vertices = value
            elif key == "scale":
                scale = value
            elif key == "angle":
                rotation = value
    return vertices, rotation, scale

if __name__ == "__main__":
    # Someone is launching this directly
    my_cli_list = command_line_arguments()
    for argument in my_cli_list:
        print argument

