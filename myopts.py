#!/usr/bin/python
#
# myopts   Module of wxpoly.py program
#
#               Defintion of returnValues Function
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
from optparse import OptionParser, IndentedHelpFormatter, OptionValueError
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
    usage = " usage: %prog [-n] [-s] [-r] [-h] [--version]"
    version = "2.0.1"
    vertices = config.default_dict["vert_default"]
    rotation = config.default_dict["rotation_default"]
    scale = config.default_dict["scale_default"]

    helpscr = IndentedHelpFormatter(indent_increment=5, max_help_position=50)
    parser = OptionParser(prog = "wxpoly" , usage = usage,
                        version="  %prog "+ version +" by Rbt. Y-Lee", formatter = helpscr)

    parser.add_option("-n", "--number", type="int", dest="num",
                                    help="  Number of polygon vertices", metavar="num")
    parser.add_option("-s", "--scale", type="float", dest="scale" ,
                                    help="  Polygon scale size", metavar="num")
    parser.add_option("-r", "--rotation", type="float", dest="angle",
                                    help="  Rotational Angle for polygon", metavar="num")
    args = []
    try:
        (options, args) = parser.parse_args()
    except OptionValueError:
        # unreachable code
        # need to subclass OptionParser and override exit() and/or error().
        # http://docs.python.org/lib/optparse-how-optparse-handles-errors.html
        if args:
            print "Incorrect usage: type wxpoly -h for help"
        sys.exit()
    options_dict = vars(options)

    for key, value in options_dict.items():
        if options_dict[key] is not None:
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


