#!/usr/bin/python

# wxpoly    Version 2
#
#               myabout Module
#
#               This module handles displaying the About Window for wxpoly
#                       implemented using wx.Html
#
#              This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

"""myabout module: About window for wxpoly."""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

#### Import Modules
#
# --- General
import sys
try:
    import wx
    import wx.html as html
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()
#
# ---   My modules
try:
    import myicon
    from myresource import page
except ImportError:
    print "Import Error: wxpoly is not properly installed."
    sys.exit()


#### HTML based On About window
#

class MyAbout(wx.Dialog):
    """Displays wxpoly About Window using Html to format text and display images. """

    def __init__(self, parent, win_id, title):
        """Initializes the wxploy About Window. """

        # Magic numbers for On about
        self.HTML_PAGE = 0

        wx.Dialog.__init__(self, parent, win_id, title, size=(400, 620))
        icon1 = myicon.get_icon()

        self.SetIcon(icon1)
        panel = wx.Panel(self, -1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.htmlwin = html.HtmlWindow(panel, -1, style=wx.NO_BORDER)
        self.htmlwin.SetStandardFonts()
        self.htmlwin.SetPage(page[self.HTML_PAGE])

        vbox.Add((-1, 10), 0)
        vbox.Add(self.htmlwin, 1, wx.EXPAND | wx.ALL, 9)

        button_ok = wx.Button(panel, 1, 'Ok')
        button_credit = wx.Button(panel, 2, 'Credits')
        self.Bind(wx.EVT_BUTTON, self.on_close, id=1)
        self.Bind(wx.EVT_BUTTON, self.on_credit, id=2)

        hbox.Add((100, -1), 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox.Add(button_credit, flag=wx.TOP | wx.BOTTOM | wx.LEFT, border=10)
        hbox.Add(button_ok, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show(True)

    def on_credit(self, event):
        """Toggles wxpoly About page to display. """
        self.HTML_PAGE = (self.HTML_PAGE +1) %2
        self.htmlwin.SetPage(page[self.HTML_PAGE])
        self.Update()
        event.Skip()
    def on_close(self, event):
        """Closes wxpoly About Window. """
        event.Skip()
        self.Close()


if __name__ == "__main__":
    # Someone is launching this directly
    app = wx.App()
    MyAbout(None, -1, 'On Polygon Generator')
    app.MainLoop()

