# setpoly      Module of wxpoly.py program
#
#                  Dialog window classes for user input of polygon data
#
#                   NewPoly( self, parent, win_id, title, poly_data)
#                   SetDialog(self, parent, win_id, title, poly_data, field)
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

""" Dialog window classes for user input of polygon data
        Used in wxPoly project

                   NewPoly(self, parent, win_id, title, poly_data)
                   SetDialog(self, parent, win_id, title, poly_data, field)
                   NewPref(self,  parent, win_id, title, poly_pref)

"""


__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####Import Modules
#
# --- General
import math
import random
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
    import myicon
    import config
    import myresource
    import gpoly
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()


#### New Polygon dialog window
#
#
class NewPoly( wx.Dialog):
    """Opens a Dialog window allowing the user to reset basic polygon data,
        specifically using wx.SpinCtrls for n, rotation and radius."""
    def __init__(self, parent, win_id, title, poly_data):
        wx.Dialog.__init__(self, parent, win_id, title, size=(235, 230))
        icon1 = myicon.get_icon()
        self.parent = parent
        self.SetIcon(icon1)
        self.poly_data = poly_data
        wx.StaticBox(self, -1, 'Polyon data', (5, 5), size=(240, 170))

        wx.StaticText(self, -1, 'N', (30, 55))
        self.sn = wx.SpinCtrl(self, -1, str(poly_data.vertices), (92, 50),
                    (60, -1), min=config.default_dict["vert_min"],
                     max=config.default_dict["vert_max"])
        wx.StaticText(self, -1, 'radius', (30, 90))
        self.sr = wx.SpinCtrl(self, -1, str(poly_data.scale), (92, 85),
                    (60, -1), min=config.default_dict["scale_min"],
                     max=config.default_dict["scale_max"])

        wx.StaticText(self, -1, 'angle', (30, 125))
        dangle = round((poly_data.rotation*180)/math.pi)
        self.sa = wx.SpinCtrl(self, -1, str(dangle), (92, 120), (60, -1),
                    min=0, max=359)

        wx.Button(self, 1, 'Ok', (92, 185), (60, -1))
        wx.Button(self, 2, 'Wicca', (10, 185), (60, -1))
        wx.Button(self, 3, 'Rnd', (175, 185), (60, -1))

        self.Bind(wx.EVT_BUTTON, self.on_close, id=1)
        self.Bind(wx.EVT_BUTTON, self.on_wicca, id=2)
        self.Bind(wx.EVT_BUTTON, self.on_rnd, id=3)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def on_close(self, event):
        """Close dialog after setting data."""
        poly_data = gpoly.Basic(self.sn.GetValue(), self.sa.GetValue(),
                         self.sr.GetValue())
        self.parent.poly_data = poly_data
        self.Close()

    def on_wicca(self, event):
        """Set data to default."""
        self.poly_data.vertices = 5
        self.poly_data.rotation = math.pi*0.5
        self.poly_data.scale = 200
        self.sn.SetValue(self.poly_data.vertices)
        self.sa.SetValue(90)
        self.sr.SetValue(self.poly_data.scale)

    def on_rnd(self, event):
        """Set data to random values."""
        vert_min = config.default_dict["vert_min"]
        vert_max = config.default_dict["vert_max"]
        self.poly_data.vertices = random.randint(vert_min, vert_max)
        self.poly_data.rotation = math.pi*random.randint(0, 359)/180
        self.poly_data.scale = 200
        self.Close()

#### New Polygon dialog window
#
#

class SetDialog(wx.Dialog):
    """Opens a Dialog window allowing the user to reset the polygon data
        specicifed in field."""

    def __init__(self, parent, win_id, title, poly_list):
        wx.Dialog.__init__(self, parent, win_id, title, size=(235, 130))
        self.parent = parent
        self.poly_data = poly_list[0]
        self.field = poly_list[1]
        icon1 = myicon.get_icon()
        self.SetIcon(icon1)
        if self.field == "N":
            wx.StaticBox(self, -1, 'Set N', (5, 5), size=(240, 80))
            wx.StaticText(self, -1, 'N', (30, 40))
            self.sn = wx.SpinCtrl(self, -1, str( self.poly_data.vertices ),
                    (92, 35), (60, -1), min=config.default_dict["vert_min"],
                     max=config.default_dict["vert_max"])
        elif self.field =="Radius":
            wx.StaticBox(self, -1, 'Set Radius', (5, 5), size=(240, 80))
            wx.StaticText(self, -1, 'Radius', (30, 40))
            self.sr = wx.SpinCtrl(self, -1, str(self.poly_data.scale),
                    (92, 35), (60, -1), min=config.default_dict["scale_min"],
                     max=config.default_dict["scale_max"])
        elif self.field == "Angle":
            wx.StaticBox(self, -1, 'Set Angle', (5, 5), size=(240, 80))
            wx.StaticText(self, -1, 'Angle', (30, 40))
            dangle = round((self.poly_data.rotation * 180)/math.pi)
            self.sa = wx.SpinCtrl(self, -1, str(dangle), (92, 35), (60, -1),
                     min=0, max=359)

        wx.Button(self, 1, 'Ok', (92, 95), (60, -1))
        wx.Button(self, 2, 'Wicca', (10, 95), (60, -1))
        wx.Button(self, 3, 'Rnd', (175, 95), (60, -1))

        self.Bind(wx.EVT_BUTTON, self.on_close, id=1)
        self.Bind(wx.EVT_BUTTON, self.on_wicca, id=2)
        self.Bind(wx.EVT_BUTTON, self.on_rnd, id=3)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def on_close(self, event):
        """Close dialog after setting data."""
        if self.field == "N":
            self.parent.poly_data.vertices =  self.sn.GetValue()
        elif self.field =="Radius":
            self.parent.poly_data.scale = self.sr.GetValue()
        elif self.field == "Angle":
            self.parent.poly_data.rotation = (math.pi*self.sa.GetValue())/180
        self.Close()

    def on_wicca(self, event):
        """Set data to default."""
        if self.field == "N":
            self.poly_data.vertices = config.default_dict["vert_default"]
            self.sn.SetValue(self.poly_data.vertices)
        elif self.field =="Radius":
            self.poly_data.scale = config.default_dict["scale_default"]
            self.sr.SetValue(self.poly_data.scale)
        elif self.field == "Angle":
            angle = config.default_dict["rotation_default"]
            self.poly_data.rotation = math.pi*angle/180
            self.sa.SetValue(90)

    def on_rnd(self, event):
        """Set data to random value."""
        if self.field == "N":
            vert_min = config.default_dict["vert_min"]
            vert_max = config.default_dict["vert_max"]
            self.poly_data.vertices = random.randint(vert_min, vert_max)
            self.sn.SetValue(self.poly_data.vertices)
        elif self.field =="Radius":
            scale_min = config.default_dict["scale_min"]
            scale_max = config.default_dict["scale_max"]
            self.poly_data.scale = random.randint(scale_min, scale_max)
            self.sr.SetValue(self.poly_data.scale)
        elif self.field == "Angle":
            self.poly_data.rotation = math.pi*random.randint(0, 359)/180
            dangle = round((self.poly_data.rotation * 180)/math.pi)
            self.sa.SetValue(dangle)


#### New Preference dialog window
#
#
class NewPref(wx.Dialog):
    """Opens a Dialog window allowing the user to set the the colors used
        to display the indivwin_idual polygon objects."""

    def __init__(self, parent, win_id, title, poly_pref):
        wx.Dialog.__init__(self, parent, win_id, title, size=(320, 370))
        icon1 = myicon.get_icon()
        self.parent = parent
        self.SetIcon(icon1)
        wx.StaticBox(self, -1, 'Color Preferences', (5, 5), size=(310, 310))
        # ----  Center Preferences Choice control
        self._ink_choice = []
        wx.StaticText(self, -1, 'Center', (25, 55))
        self._ink_choice.append(wx.Choice( self, -1, (125, 50), choices=myresource.color_names))
        # --- Vertices Preferences Choice control
        wx.StaticText(self, -1, 'Vertices', (25, 90))
        self._ink_choice.append(wx.Choice( self, -1, (125, 85), choices=myresource.color_names))
        # --- Swin_ides Preferences Choice control
        wx.StaticText(self, -1, 'Sides', (25, 125))
        self._ink_choice.append(wx.Choice( self, -1, (125, 120), choices=myresource.color_names))
        # --- Diagonals Preferences Choice control
        wx.StaticText(self, -1, 'Diagonals', (25, 160))
        self._ink_choice.append(wx.Choice( self, -1, (125, 155), choices=myresource.color_names))
        # --- Circumscribe Circle Choice control
        wx.StaticText(self, -1, 'Circumscribe', (25, 195))
        self._ink_choice.append(wx.Choice( self, -1, (125, 190), choices=myresource.color_names))
        # --- Inscribe Circle Preferences Choice control
        wx.StaticText(self, -1, 'Inscribe', (25, 230))
        self._ink_choice.append(wx.Choice( self, -1, (125, 225), choices=myresource.color_names))
        # --- Axis Preferences Choice control
        wx.StaticText(self, -1, 'Axis', (25, 265))
        self._ink_choice.append(wx.Choice( self, -1, (125, 260), choices=myresource.color_names))
        # --- Set all choice controls to current Preferences
        self.set_choice_ctrls()
        # --- Restore and Ok buttons
        wx.Button(self, 1, 'Ok', (130, 330), (70, -1))
        wx.Button(self, 2, 'Cancel', (240, 330), (70, -1))
        wx.Button(self, 3, 'Restore', (15, 330), (70, -1))
        self.Bind(wx.EVT_BUTTON, self.on_close, id=1)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, id=2)
        self.Bind(wx.EVT_BUTTON, self.on_restore, id=3)
        self.Centre()
        self.ShowModal()
        self.Destroy()

    def on_close(self, event):
        """Close dialog after setting data."""
        self.parent.view['Center']['ink'] = self._ink_choice[0].GetStringSelection()
        self.parent.view['Vertices']['ink'] = self._ink_choice[1].GetStringSelection()
        self.parent.view['Sides']['ink'] = self._ink_choice[2].GetStringSelection()
        self.parent.view['Diagonals']['ink'] = self._ink_choice[3].GetStringSelection()
        self.parent.view['Circumscribe']['ink'] = self._ink_choice[4].GetStringSelection()
        self.parent.view['Inscribe']['ink'] = self._ink_choice[5].GetStringSelection()
        self.parent.view['Axis']['ink'] = self._ink_choice[6].GetStringSelection()
        self.Close()

    def on_restore(self, event):
        """Set data to default."""
        self.parent.view.restore_default()
        self.set_choice_ctrls()
        self.parent.Refresh()

    def on_cancel(self, event):
        """Close dialog but don't change polygon data"""
        self.Close()

    def  initialize_choices(self):
        """initialize all choices."""



    def set_choice_ctrls(self):
        """Sets selection initialitally displayed in wx.SpinCtrls."""
        # ----  Center Preferences Choice control
        ink = self.parent.view['Center']['ink']
        color = self._ink_choice[0].FindString (ink)
        self._ink_choice[0].SetSelection (color)
        # --- Vertices Preferences Choice control
        ink = self.parent.view['Vertices']['ink']
        color = self._ink_choice[1].FindString (ink)
        self._ink_choice[1].SetSelection (color)
        # --- Sides Preferences Choice control
        ink = self.parent.view['Sides']['ink']
        color = self._ink_choice[2].FindString (ink)
        self._ink_choice[2].SetSelection (color)
        # --- Diagonals Preferences Choice control
        ink = self.parent.view['Diagonals']['ink']
        color = self._ink_choice[3].FindString (ink)
        self._ink_choice[3].SetSelection (color)
        # --- Circumscribe Circle Choice control
        ink = self.parent.view['Circumscribe']['ink']
        color = self._ink_choice[4].FindString (ink)
        self._ink_choice[4].SetSelection (color)
        # --- Inscribe Circle Preferences Choice control
        ink = self.parent.view['Inscribe']['ink']
        color = self._ink_choice[5].FindString (ink)
        self._ink_choice[5].SetSelection (color)
        # --- Axis Preferences Choice control
        ink = self.parent.view['Axis']['ink']
        color = self._ink_choice[6].FindString (ink)
        self._ink_choice[6].SetSelection (color)

#if __name__ == "__main__":
    # Someone is launching this directly

