
# myApp.py
#
#                Defintion of Ngon application window
#
#                Ngon( self, parent, id, title, poly_data, pathname)
#
#           This program is free software. It comes without any warranty, to
#            the extent permitted by applicable law. You can redistribute it
#            and/or modify it under the terms of the Do What The Fuck You Want
#            To Public License, Version 2, as published by Sam Hocevar. See
#            http://sam.zoy.org/wtfpl/COPYING for more details.

""" Defintion of Ngon application window.
    Used in wxPoly project.

    Ngon( self, parent, id, title, poly_data, pathname).

"""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

WX_POLY = "wxpoly3 213023"

#### Import Modules
#
# --- General
import os
import sys
import math
import cmath
import random
try:
    import wx
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()
#
# --- My modules
try:
    import myicon
    import config
    import myresource
    import show
    import gpoly
    from setpoly import NewPoly, SetDialog, NewPref
    from myabout import MyAbout
    from mymenu import create_menu_bar
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()

#### Polygon Application Main Window
#
#
class Ngon( wx.Frame ):
    """ Frame class that implements wxPoly program window
         Ngon(self, parent, id, title, poly_data, pathname).

    """
    ##### Initialize Ngon data, set window up and display
    #
    def __init__(self, parent, id_num, title, default_poly):
        #           initialize internal data
        self.poly_data = default_poly.poly_data
        self.path = default_poly.pathname
        self.view = default_poly.pref
        self.EXPORT_FLAG = False
        self.selection =""
        #           initialize window
        wx.Frame.__init__(self, parent, id_num, title, size=(config.WIN_WIDTH, config.WIN_HEIGHT))
        icon1 = myicon.get_icon()
        self.SetIcon(icon1)
        create_menu_bar(self)
        self.statusbar = self.CreateStatusBar()
        self.Bind(wx.EVT_LEFT_DOWN, self._on_next)
        self.Bind(wx.EVT_RIGHT_DOWN, self._on_prev)
        self.Bind(wx.EVT_CLOSE, self._on_close_window)
        self.Bind(wx.EVT_PAINT, self._on_paint)
        #           display window
        self.Centre()
        self.Show(True)

    ##### Internal Functions for display
    #
    # --- Close Window and Shut down : EVT_CLOSE
    def _on_close_window(self, event):
        """Close window and shut down."""
        self.Destroy()
    #
    # --- Process onPaint event : EVT_PAINT
    #
    def _on_paint(self, event):
        """Draws polygon on canvas area of Ngon."""
        # --- initialize WIndow
        self._display_status()
        canvas = wx.PaintDC(self)
        canvas.SetBackground(wx.Brush(self.view['Background']['ink']))
        canvas.Clear()
        size_x, size_y = self.GetClientSizeTuple()
        canvas.SetDeviceOrigin(size_x/2, size_y/2)
        # --- Calculate polygon vertices
        cangle = cmath.exp(-self.poly_data.rotation*1j)
        rts_unity = [self.poly_data.scale*cmath.exp((2*k*math.pi/self.poly_data.vertices)*1j)\
                *(cangle) for k in range(self.poly_data.vertices)]
        # --- Draw polygon objects
        for obj in self.view:
            if obj["isVisible"]:
                canvas.SetPen(wx.Pen(obj["ink"], obj["size"], obj["style"]))
                show.display( self, obj, canvas, rts_unity)
        # --- Save as bitmap if export flag is set
        if self.EXPORT_FLAG :
            savebmp( self)
            self.EXPORT_FLAG = False
    #
    # --- Set Stautus text with polygon information
    #
    def _display_status(self) :
        """Sets Stautis Text with polygon data"""
        dangle = round((self.poly_data.rotation*180)/math.pi)
        if self.poly_data.vertices > 20:
            status_text = "   Polygon  n ="+str(self.poly_data.vertices) + "   r =" + \
                str(self.poly_data.scale) + "   Angle =" + str(dangle)
        elif self.poly_data.vertices == 0:
            status_text = "   " + myresource.PolyNames[self.poly_data.vertices] + " : n ="\
                + str(self.poly_data.vertices) + "   r =" + str(self.poly_data.scale)  +\
                "   Angle =" + str(dangle)+"  : This Polygon has no Points !!!"
        else:
            status_text = "   " + myresource.PolyNames[self.poly_data.vertices] + " : n ="\
                + str(self.poly_data.vertices) + "   r =" + str(self.poly_data.scale) + \
                "   Angle =" + str(dangle)

        self.SetStatusText(status_text)

    ##### Internal Functions for Menu Processing
    #
    # ####       File Menu
    #
    def _on_new_poly(self, event):
        """Handles New polygon menu item."""
        NewPoly(self, -1, 'New polygon', self.poly_data)
        assert (config.default_dict["vert_max"] > self.poly_data.vertices
                     >= config.default_dict["vert_min"])
        self.Refresh()

    def _on_open(self, event):
        """Load New Polygon data from a file"""
        # --- Initialize Open File Dialog
        filters = 'All files (*.*)|*|Wx Poly files (*.wxp)|*.wxp'
        dialog = wx.FileDialog ( None, message = 'Open something....',
            wildcard = filters, style = wx.OPEN | wx.MULTIPLE ,
            defaultDir=self.path)
        dialog.SetFilterIndex(1)
        icon1 = myicon.get_icon()
        dialog.SetIcon(icon1)
        # If ok was pressed read file and set Polygon data
        if dialog.ShowModal() == wx.ID_OK:
            # --- Open File and read data into a list
            #           try to catch posssible IO errors
            selection = dialog.GetPath()
            self.path = str(os.path.dirname(selection))
            data = []
            try:
                file_handle = open(selection, 'r')
                try:
                    for line in file_handle:
                        for val in line.split(','):
                            data.append(val)
                finally:
                    file_handle.close()
            except IOError:
                sys.stderr.write( "wxpoly: IO Read Error" + str( selection) +"\n")
            # --- Save Old data in case we have to restore it
            old_n =  self.poly_data.vertices
            old_scale =  self.poly_data.scale
            old_rotation =  self.poly_data.rotation
            # --- Set Ngon data to data read from file
            if data[0] == WX_POLY + "\n" and len(data) == 4:
                try:
                    #   Try to set Ngon data to new values
                    #           Incorrect values will raise ValueError
                    self.poly_data.__init__(int(data[1]),
                                            180*float(data[3])/math.pi,
                                            int(data[2]))

                except ValueError:
                    #   Invalid data type-- restore Ngon to old values
                    sys.stderr.write( "wxpoly: Corrupt or invalid file" + str( selection) + "\n")
                    self.poly_data.vertices = old_n
                    self.poly_data.scale = old_scale
                    self.poly_data.rotation = old_rotation
                    self. _on_file_error()
            else:
                #       File was not a wxpoly data file
                sys.stderr.write( "wxpoly: Invalid file" + str( selection) + "\n")
                self. _on_file_error()
        # some development tests to make sure polygon data is meaningful
        assert (config.default_dict["vert_max"] > self.poly_data.vertices
                     >= config.default_dict["vert_min"])
        assert (config.default_dict["scale_max"] > self.poly_data.scale
                     >= config.default_dict["scale_min"])
        # close dialog
        dialog.Destroy()
        self.Refresh()

    def _on_save(self, event):
        """SaveNew Polygon data to a file"""
        # --- Initialize Save File Dialog
        filters = 'All files (*.*)|*|Wx Poly files (*.wxp)|*.wxp'
        dialog = wx.FileDialog ( None, message = 'Save Polygon Data ....',
                     wildcard = filters, style = wx.SAVE | wx.OVERWRITE_PROMPT,
                     defaultFile = "New Poly.wxp", defaultDir=self.path)
        dialog.SetFilterIndex(1)
        icon1 = myicon.get_icon()
        dialog.SetIcon(icon1)
        # If ok was pressed  write Polygon data
        if dialog.ShowModal() == wx.ID_OK:
            selection = dialog.GetPath()
            #       Add extension if needed
            if selection[-4:] != ".wxp":
                selection += ".wxp"
            # --- Open File and write data
            #           try to catch posssible IO errors
            self.path = str(os.path.dirname(selection))
            poly_data = str(self.poly_data.vertices) + ", " + str(self.poly_data.scale) + ", "\
                                + str(self.poly_data.rotation)
            try:
                file_handle = open ( selection, 'w' )
                try:
                    file_handle.write (WX_POLY + "\n" )
                    file_handle.write (poly_data )
                finally:
                    file_handle.close()
            except IOError:
                sys.stderr.write( "wxpoly: IO Write Error" + str( selection) +"\n")
        # close dialog
        dialog.Destroy()

    def _on_export(self, event):
        """Export current Polygon as an bitmap image. """
        # Export dialog has to be in seperate function (?)
        # so dialog is closed before we refresh
        # the onpaint event catches an export flag
        # to call save bitmap AFTER screen has been drawn
        # avoids saving a bitmap with dialog box damage
        self._on_export_dialog()
        self.Refresh()

    def _on_quit(self, event):
        """Exit Program"""
        self.Close()
     #
     # ####      Edit Menu
     #
    def _on_new_n(self, event):
        """Handles New n menu item."""
        SetDialog(self, -1, 'Set N', [self.poly_data, "N"])
        assert (config.default_dict["vert_max"] > self.poly_data.vertices
                    >= config.default_dict["vert_min"])
        self.Refresh()

    def _on_new_radius(self, event):
        """Handles New Radius menu item."""
        SetDialog(self, -1, 'Set N', [self.poly_data, "Radius"])
        assert (config.default_dict["scale_max"] > self.poly_data.scale
                    >= config.default_dict["scale_min"])
        self.Refresh()

    def _on_new_rotation(self, event):
        """Handles New Angle menu item."""
        SetDialog(self, -1, 'Set N', [self.poly_data, "Angle"])
        if self.poly_data.rotation > 2 * math.pi:
            self.poly_data.rotation = self.poly_data.rotation % (2 * math.pi)
        self.Refresh()

    def _on_new_pref(self, event):
        """Calls set new graphical polygon preferences."""
        NewPref(self, -1, 'New polygon', self.view)
        self.Refresh()
      #
      # ####     View Menu
      #
    def _show_center(self, event):
        """Toggles _show_center Viewer preference."""
        self.view.toggle_visiblity("Center")
        self.Refresh()

    def _show_sides(self, event):
        """Toggles _show_sides Viewer preference."""
        self.view.toggle_visiblity("Sides")
        self.Refresh()

    def _show_diags(self, event):
        """Toggles _show_diags Viewer preference."""
        self.view.toggle_visiblity("Diagonals")
        self.Refresh()

    def _show_vertices(self, event):
        """Toggles _show_vertices Viewer preference."""
        self.view.toggle_visiblity("Vertices")
        self.Refresh()

    def _show_circ(self, event):
        """Toggles _show_circ Viewer preference."""
        self.view.toggle_visiblity("Circumscribe")
        self.Refresh()

    def _show_ins(self, event):
        """Toggles ShowIns Viewer preference."""
        self.view.toggle_visiblity("Inscribe")
        self.Refresh()

    def _show_axis(self, event):
        """Toggles _show_axis Viewer preference."""
        self.view.toggle_visiblity("Axis")
        self.Refresh()
    #
    # ####  Polygon Menu
    #
    def _on_new_rnd(self, event):
        """Sets polygon Data to random values handles Wicca menu item."""
        self.poly_data.vertices = random.randint(config.default_dict["vert_min"], \
            config.default_dict["vert_max"])
        self.poly_data.rotation = math.pi * random.randint(0, 359)/180
        self.Refresh()

    #      _on_next also mouse event left button
    def _on_next(self, event):
        """Increments N and redraws polygon menu item."""
        self.poly_data.vertices = self.poly_data.vertices +1
        if self.poly_data.vertices > config.default_dict["vert_max"]:
            self.poly_data.vertices = config.default_dict["vert_min"]
        self.Refresh()

    #      _on_prev_ also mouse event right button
    def _on_prev(self, event):
        """Decrements N and redraws polygon menu item."""
        self.poly_data.vertices = self.poly_data.vertices - 1
        if self.poly_data.vertices < config.default_dict["vert_min"]:
            self.poly_data.vertices = config.default_dict["vert_max"]
        self.Refresh()

    def _on_wicca(self, event):
        """Sets polygon Data to defaults handles Wicca menu item."""
        self.poly_data.vertices = config.default_dict["vert_default"]
        self.poly_data.rotation = math.pi * config.default_dict["rotation_default"]/180
        self.Refresh()
    #
    # ####  Help Menu
    #
    def _on_about(self, event):
        """ Display on about WIndow"""

        MyAbout(self, -1, 'On Polygon Generator')

    def _on_help(self, event):
        """Display help screen."""
        dialog = wx.MessageDialog( self, "wxpoly3 py by Rbt Y-Lee\n\n"
                "Command line Options\n\n"
                "\t-n, --number  	number of polygon vertices\n"
                "\t-s, --scale       	polygon scale\n"
                "\t-a, --angle     	Rotational Angle for polygon\n"
                "\t-h, --help          prints this screen\n"
                "\t--version           prints program version number\n"
                "\nNo Turn left unstoned","Polygon Generator Manual", \
                 wx.OK | wx.ICON_QUESTION)
        dialog.ShowModal()
        dialog.Destroy()

    ##### Dialogs used by File
    #
    # ---  invalid or corrupt file Error Dialog
    def _on_file_error(self):
        """Dialog Window for invalid or corrupt file"""
         # ---  Initialize File Error dialog
        dialog = wx.MessageDialog( self, "wxpoly3.py by Rbt Y-Lee\n\n"
                "\n           WTF\n\n"
                "This File is corrupt\n\n"
                "Sorry, maybe next time ;)","What The Fuck", \
                 wx.OK | wx.ICON_EXCLAMATION )
        dialog.ShowModal()
        # close dialog
        dialog.Destroy()
    #
    # --- Display Export Dialog
    #
    def _on_export_dialog(self):
        """Export current Polygon as an bitmap image

        """
        # ---  Initialize Export dialog
        filters = 'All files (*.*)|*|Image files (*.bmp)|*.bmp'
        dialog = wx.FileDialog ( None, message = 'Save as bitmap....',
            wildcard = filters, style = wx.SAVE | wx.OVERWRITE_PROMPT ,
            defaultFile = "poly.bmp", defaultDir=self.path)
        icon1 = myicon.get_icon()
        dialog.SetIcon(icon1)
        dialog.SetFilterIndex(1)
        # set export flag and if ok was pressed set filename and path
        if dialog.ShowModal() == wx.ID_OK:
            self.selection = dialog.GetPath()
            self.path = str(os.path.dirname(self.selection))
            self.EXPORT_FLAG = True
        else :
            self.EXPORT_FLAG = False
        # close dialog
        dialog.Destroy()

    ##### Internal Functions for development
    #
    # --- Not Implemented Dialog
    def _not_implemented(self, event):
        """Dialog Window for Not Imlemented"""
        dialog = wx.MessageDialog( self, "wxpoly3.py by Rbt Y-Lee\n\n"
                "\n                     WTF\n\n"
                "This Function is not implemented yet\n\n"
                "Sorry, maybe next time ;)","What The Fuck", \
                 wx.OK | wx.ICON_EXCLAMATION )
        dialog.ShowModal()
        dialog.Destroy()

#### function to save polygon image as bmp
#
def savebmp( self):
    """Save image as bitmap."""
    if self.selection[-4:] != ".bmp":
        self.selection += ".bmp"
    context = wx.ClientDC( self )
    memory = wx.MemoryDC( )
    width, height = self.GetClientSizeTuple()
    bitmap = wx.EmptyBitmap( width, height, -1)
    memory.SelectObject( bitmap )
    memory.Blit(0, 0, width, height, context, 0, 0)
    memory.SelectObject( wx.NullBitmap)
    try:
        bitmap.SaveFile( self.selection, wx.BITMAP_TYPE_BMP )
    except IOError:
        sys.stderr.write( "wxpoly: save bitmap" + str( self.selection) + "\n")

# Someone is launching this directly
if __name__ == "__main__":

    # Initialize data
    n = 5
    rotation = 0
    scale = 200
    pn = os.path.dirname(sys.argv[0])
    pathtest = str(os.path.abspath(pn))
    poly_data_ = gpoly.Basic(n, rotation, scale)
    pref = show.Preference()
    for a in pref:
        print pref[a["name"]]['ink']

