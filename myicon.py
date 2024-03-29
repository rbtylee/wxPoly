# myicon.py icon data for wxpoly
#
#             This program is free software. It comes without any warranty, to
#              the extent permitted by applicable law. You can redistribute it
#              and/or modify it under the terms of the Do What The Fuck You Want
#              To Public License, Version 2, as published by Sam Hocevar. See
#              http://sam.zoy.org/wtfpl/COPYING for more details.

"""myicon module: stores icon for wxpoly."""

__author__ = "Rbt Y-Lee"
__copyright__ = "Copyright (C) 2008 Rbt Y-Lee"

####    Import Modules
#
# ---   General
import sys
import cStringIO, zlib
try:
    from wx import ImageFromStream, BitmapFromImage
    from wx import EmptyIcon
except ImportError:
    print "Error: wxpoly requires wxPython, which doesn't seem to be installed."
    print "Get it from http://www.wxpython.org"
    sys.exit()


def get_data():
    """Returns data for icon."""
    return zlib.decompress(
'x\xda\x01\xbd\x0bB\xf4\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x0btIDATh\x81\xed\x99[\x8c]Wy\xc7\x7fk\x9f\xfbe\xae\
\xb6\xc7\xb1\x1d\x1c;\xb6\x93\x1a\x0b\x13\xa0q\xa3^\x12JB\x81<\xd0J\x08!\x94\
\x07Z\xa9\xadxH\xd3\x96\x87\x16U\x14\xa9\xa8R\x1f\xf2@y\xa8\xea\xd2\x87Vi\
\x89\xa8\xd2K\x14Z\xa2\x80\n$U!\t\x10\x10r\x081\x8e\xe3x\xc6\xe3\xcbxng\xcee\
\xef\xbd\xd6\xfa\xbe>\xac\xb5\xcf\x9c\x99L.\xbePUj\x96\xb44[{\xf6\xb7\xcf\
\xff\xff]\xfe\xeb[k\xc3[\xe3\xad\xf1\xff{\x98k\xb0\xdbl\xab\x9b\xfe^\x89\xed\
\x95\xd8\xbf\xeaeW\xf2\xac\x01\x928\x8bk}\x839j\x9fl\xf1\x8e\xd1g%\xce\xad\
\xec\xaf\x9a@\x01|\x0c(\x033\xc0o\x02;\x81\x9f\x02}\xe0\'\xc0\xcb\xc0\x1a`\
\x81.\xe0G\xc0L\x00m\xe0mq~$\xde\xfb>P\x01\x9e\x01~\x00\xac\x00\xbdh\xebFH]5\
\x81$\x02\xaf\x00\xef\xfb\xf8\xee\xf6o\x1f\x19\xab\xbc\xff\xdd\x135\xf6\xd6\
\xcb\xb4\xca\t=\'\x9cM\x1d\xcf\xadf|{)\x9d\xfd\xea\xc2\xe0Q\xe0\x11`.\x82\
\xac\x00?w\xdf\x9e\xf6\xc7\x8fM\xd6\xdes\xa8U\x99\xd9\xca\xf6\xa9\xc5t\xf9k\
\x97\x07_\x06\xbe\x18\x89,\x00y$\xf3\x9a\xd1x=\x02\t\xb0\x1d\xb8\xf9\xfe}\
\xe3\x9f\xbew\xa6\xf9\xeb\x87\xdb\xd57\xe0\x0b/ts\xbe\xf8Jg\xe5\xd1\x8b\xfd\
\xe3\xc0\xb7>\xb5\x7f\xe2\xb7\xee\xd9\xd1\xf8\xd8\x9b\xb5\xfd\xab3\x1d\xfe\
\xe3R\xffw\x80o\x01\x97\x80\x8c\x10\x8d"\x9ao\x8a@\x01\xfe\xc8\x17\x8el\xfb\
\xf2\x87w\xb6f\x8a\x7f\x8c\xef\x9d\xa4y\xf3\x0e\xaa\xbb\xa70\x93Mt\xa5O>\xbf\
L\xff\xf4\x02\x9d\xb3+\xc3\x17\xfc\xfb\xc5\xde\xf9U\'\xbb\xee\xdb3\xc6\x96\
\xb6\x13\xd1vn\x91\xde\xe9\x05:s\xab\xc3\xe7\xbetn\x8d?=\xb9\xf2{\xc0\x7f\
\x02\xe7\x81\xc1k\x91\xd8\x8a@\x02\x8c\x03\xef\xfd\xfb\xa3\xdb\x1f\xbas[c\
\xcc\x18\xc3\xe4\xcd\xd3\x8c\xdfq\x90dfr\xf8\xa0\x8a\xdf`\xa8\x0bkt\x9e9\xc5\
\xca\xe9\xa5\r\xf7\'o\x9ef\xfc\x17\x0ebv\x8ca\x92R\xb0\x13\r3s`=na\x95\xce\
\x8f\xe6\xe8\xcc\x06\'|\xedr\x9fO\x9eX\xfc\x0b\xe0\x1fFHX6\xd5Di\x13\xf8\xa2\
Xo\xfb\xcb\xb7O?\xf4k;\x9a\xd3\x00\xbb\xee:H\xfb\xce\xb7c\xda\x8du\xe0\xaa13\
#\x10\x11L\xbdB\xfd\xc0N\x1a\xcd\x84\xf6MSqn\xa3\xf5K\xb7`\x9a\xb5\xf0z\x11\
\xc8\x1dd\x16\xed\xe70\xc8\x91\xfe\x00D\xa9N5\xa8VJ\xf4/w9\xd0\xac\xb0\xbd\
\x96\xfc\xca7\x17\xd3e\xe0% e\xa3BmI\xa0\x04\xec\xfe\xfd}\xe3\x7f\xf2\x89\
\x1b\xc7\x8e\x15\xe0\xeb\xb7\xed\x8f.V\xd4\xfb\x11\x91\x8b\xe0\xbd\x82\x17\
\xb0\x02\xceQ\x9enS\x9ajQ\x9e\x1e\xa3\xbcm,\xdc\xb7\x1e\xedg0\xc8!\xcd\xd1\
\x81E{\x03\xa4\x9f!\x9d\x01\xd2\xcdp\xbd\x9c$1\x94\xab\t\xe9r\xca\xd1\xb1\
\x1a\x17s\xbf\xe3\xf9\xae}\x01\xb8@(h?J\xa0\xbc)u\xda\xc0\xdd\xf7\xce4\x7f\
\x03\r\xa1\xaf\xbfs\xff\xf0qUY\x07\xee}\x04\xeeQ\'\xc3\x94P\xf1\xe0\x04\x95\
\xf5T5\x89A}\xb0U\xe7\x83\x8d\xf5h\xea\x90A\x8e\xcf,\x9a9\xbc\r\xf7\x8d@\xad\
]%]\xcb\xb8ow\xeb\xf0?\x9d\xef\xfd\x01\xf0"A\x95\x8a4\xd2\xcd\x04\x0c\xb0\
\xf3\xc33\x8d\x07\x0e6\xca\x15Ue\xe2\xe7\xf7A\xccs\xf51\xdfM)x\xdb{\xb0\x82:\
\x87f\x1e\xc9\xf2\x00*s\xe1\xcd2d\x8d\x89+\x89\x02xE\xf3\x00X2\x87\xe4\x0e?\
\xc8\xf1\x99 V\x10\xf1\xa8@\x92$\xa8W\x0e\xd7\xcb\xdc5]\xfb\xc5\'\x97\xb2[\
\x81%\xd6U\xc9\x00Z\x1e\x01\x9f\x00\xef\xbcs\xba\xb1\x07`|\xcf\x04\xc9\x8eI\
\x90\x91b\x15\x05\xb1`\x1d\x9a\xe5\x01xj\x91\xd4!\x99\r$\xbc\xa0NQ\xd6\x15\
\xc2$\x065\x8a\x11P\xaf\xa8\xf5\xe1\xf94\xc7\xa7\x0e\x9f{\xc4y\xbc\x07\xbc I\
\xb0LJ\t\xe2\x85\xf7N\xd7yr);DX\xec*\x91\x84\x8cF\xa0 p\xd7-\xad\xf2\x94\x8a\
\xd2\xde7\x1d\xbc\x0c`\xf3\x10\xb1\xcc\xa2V\x91X\x80\x92\xfb\xe8=\x8b\xe4\
\x82F \xeaG\x84"1\x185\xd1_\x02N\x91\xdc\xe23\x1f\xec\x9c\xe22\x8b\xf8\x10e5\
\x06\x8c!\xa9$`\x12\xc4+\xb7\x855d\n\xa8E\xcc\xc36ds\r\x1c\xb8\xa9V\x06\x85\
\xca\xce6\x9af\xe0\x1cd1g\x9dG\xad\x0b^\x1fX\\\xe6\xf1\xfd\x0c\x9f\x0bb]\x00\
!\x82J\xac\x15\x03\x06\x13\xa2\xa8\x12\xbdo\xf1NQ\xeb\xf0\x99\xe0\x9dC\x9c \
\xaa\xa8\x8f\x84\x13Cyz"\x10\x1a8\xf6V\x12\x80\xf7\x01\xffH\x10\x9a\xa4\x00\
\xbd9\x02\xd3\xad\x92AE\x83^\xaf\xa5`s$\x0b^\xd5\xcc\xa1\xb9\xc3g\x16\x9f\n\
\xbe\x9f\xe32\x87w\x1e\xf1\x8a\x8a\xa2Cy\x8dd\x14\x10A\xa2R\x89\xf5\x88\xf5x\
\x17\xaf\xbd\x06[\x15\xd4\x84tKJ\tI\xbb\x8c\xf1\x15tq@\xbb\x9c\x14\x18\x0b\
\xf0\xc3\x8evs\x11\x1f\xeb:\xa1\x95\x18\xec\xc5\x0e\xa5f\x05\xb5\x16\xcd5\
\xe4\xbc\xf5\xf8\xd4\xe33\x87\xcb\x1c.\r\xe0\xbd\x8b@U\xd1"]DQ\x11\xc4\x83D\
\xa5R\'\x81l\x1e\xa2\xe1\xd5\x87zQ\x10ULb0\x06D\x94d`I\xdau\x00\xd6\x9c\x00\
\xbc2\n|s\x04\x8a\xf1\xf8+\xa9\xfb\xd0\xe1F\x85t\xbeCcW+\xe6|\x8e\xa6A\xe6|\
\xe6\xf1\xa9\xc5\xe5\x82\xcb]\x00/\x8a\xc6\xceX\x8d\t\xf8\x05T\x14\x89\xd1\
\xf16\xd4\x8f\xb7\x1e\xf1\xd1\xc6\x85\xa8a\x0cB(r\x93@\x82F\xb57\xa8*g\xac\
\x02\x9cac+\xb1AF\x8b\xb6\xf5o\x9e[\xcb?t\xb8Q\xa6{~\x85\xdaD\x05\xc9\xa3b\
\xe4\x82\xa4\x0e\x9fyl\xeap\xd1\xf3\x12=\xadQ+\x0b\x02\xea|\xf8\x9f\x97\x90\
\xe36N\'8/\xa8*Z\xd4\xba\nAk\xa3{\r\x98v\x15\x1dX\x8c1\xfc\xa0\x9bAX\x07\x1c\
\xebm\xfa\xb0p\x8b!\xc0\xdc\xd3+\xd9\x1c\x18z\xcb\x19\xd9\xe2\x00\xdfs\xb8\
\x81\xc3us\xec \'\xef\xe7\xd8\xcca3\x17\x8a8\xf7\xb8\\qV\xf1\xce\xaf\xd7\x88\
\x13l\xee\xb1V\xc8S\x1f\xae\x0b\xf0\xa2\xa1\xa0\xa5\xa8\x9b\x98\xc319\xca;Z$\
\x13ud\xa9\x8fI\x0c\xdfY\xc9;\xc0,a\x11s[\x11\xd0\xc8l\xe5\x89\xcb\xe9\xe7\
\x7f<\xb0\x00\xac\xcewpY\x1e\x08\xe4\x0e[x?\x82/\xee9\x1b\x16$\xb1\x82uq\xa6\
!\xdd\\\xeaC\x04|\x8cFQ\xb4\xb2\xbe\xe92\xc3\x84\x80\xa4U\xa1ql\x0fF\x80\xcc\
\xf1|\xe6\xf9\xc6R\xfa8a\xb3\x94E\x12\xc3~h\x94\x80\x10\xba\xbe\'\x8e\xcfu1\
\x06\xd2\xb5\x9c\xee\xe2\x00\x9f;l\x1eA;\xc1\xe5\x82\xcf=\xde\xc5\x9c\xb6\
\xe1\x9e\xcd\x8a\x1a\xf1\xe1\xbe\x93P\x03N\xd6IHL\x1f\x88\x9e7Aq\r\x94ZU\xda\
w\xef\x07\x0c\xf6\xd4"F\x94\xbf\x9d\xef\x01<\x0c\xac\x12\x1a\xba\rm\xf5h3WTx\
\xfdT\xdf=;U/}\xe4h\xab\x8a\x8d\xd1\x10\x0f>w\x88S\xbc\xf7x+\x88\x06\x95Q\
\x18J\xe80-b\x9a\xc8\xf0:\x02/|g\x8a\xb41\x98\x92\xa1\xb2\xbdA\xf3\x8e=@B\
\xfa\xd4\x19\x12+<\xbc\x92\xf1w\xe7z\x9f\x06N\x12\xda\x88"\n[\x12("\x91\x02\
\xcbO.e{o\x1d\xab\x1e>\xd8\xa8`3\x8fj\x08\xbdw!\xd7\xbd\x0f\xb5\xa72\xaa\xfb\
\x8c\x10 \x82f\x1d\xbc\xb0\x01\xbdI\x0c\xa6b\xa8\xeei\xd3|\xd7.\x18x\xec\x0f\
/\x90(<\xd1w|\xe6\xd4\xea\x83\xc0\x7f\x11\xb6\x97\x1d\xc2\xfe\xbbH!\xb6"P\
\x9c\x128\xe0\xb9\xc7/\x0f\x8e\x1c\x9d\xa8\xee\xdbW+#N\x02\xf8\x08jHWY_\x03F\
<\x1fV\xe4x\x1d\rT\x15ST\xaa\x01S-Q\xdf;N\xe3\xb6\x1b\x90\x0b}\xec+\xab\x98\
\xcc\xf3\xa5\x8e\xe5\xb3/\xad~\x9e\xb0#\xbb@\xd8#\xaf\xb1q\x8f\xbc%\x81Qh\
\x19\xf0\xf4W\x16\x06\xf6\xf6\xa9\xda\xb1]\x95\x04\x13\x1a\x03L\xa3B2\xd9@z6\
nlB\xaa\x10\xa3DL\x95a\x84\n\xef\x14KPb(\xb5\xca\xd4nlS?2\x83\x9b]\xc3_\xeca\
R\xc7c=\xc7\xe7Nw\xfe,z~\x1eX\x8e\xe0\xd3\xcd\xe0\xb7"0JDc\xc8.=zi\xf02\xe5\
\xe4W\x0f5\xcb4\x92$\xf4\xec\xcd*\xc9d\x1d\xe9\xa4\xb1]\x88\xca\xa2:L\x17\
\xdd\x10\xaa\xe0v\x93\x18JcU\xaa;[Tn\xdd\x86{q\x05w\xb1\xc7\xf9\x81\xe3\xe1U\
;xr%\xfb\xc2\\\xea\x9f\x05\xce\x8ex~\xb4x7\x8c\xd7"\x00\xeb\x87L+\xc0\xa5\
\xef\xae\xe6\'\xdb\xd5\xd2\x07\xdeV+\xd3N\x0c\xd2\xcd1\xd5\x12I\xab\x8a\xf4\
\xf2\xf5\xbc\x8f\x9e\x7f\xf5\x01\x82\xc1\x94 \x19\xabR?0I\xf5\x96i\xec\x89Ed\
a\xc0\xbc(\x8f\xf5\xdc\xfc_\xcfv?3\x97\xfa\x13\xc09\xe0r\x04_l\xe8\xaf\xf8X\
\xa5h\xf0*@\x03\xd8\x03\x1cz\xf7x\xf5_?w\xd3\x18\xfbJ\x06\xf1\x82\xd9\xd6DU\
\xc9\xe7:h\x94J\x86j\xa3\xeb\xbeO\x0cI\xbbB\xe3\xd6i\xca7\x8e\x93}\xef\x02\
\xba\x9a\xf1M\xa7\x9c\xcc\xe5\xc4\xf1\xd9\xee\x83\x11\xf8<A2{l!\x9b\x9b\xc7\
\xebE\xa0\x18\xc5"7\x00z\xe73\xffo\x0f_\x1a\x1c\xd8\xd7\xae\xee\xbd\xa5VB\
\xba\x19\xa6^\xa6\xd4\xac\xe0\x875\xb1\x9e\xef\xc6\xc4\xb4i\x95\xa9\x1f\x9a\
\xa2\xb2\x7f\x92\xec\xd9\x0b,\xae\xa4<\x91)\x8f-\xe7?}\xf4\xd2\xe0\xb3\x9b\
\xc0wG\xc0\xbf\xee\x11\xe3\x9b!P\x90\x90\xf8\xd2\x0e\xf0\x9d\xaf/\xa5MSI\x8e\
\xde\xde\xaa\xa0=K\xd2\xaa\x924\xcbH\xdf\r\x81c\x0cI\xc9PjWh\xbc\xeb\x06*\
\xbb\xc7\xc9\x9f9Ow5\xe3\x91\x81\xf0\xe0l\xf7\xebs\xa9\xffsB\xa1\x9e\x1b\x01\
\x9f\xf1\x06\'rWC\xa0\x88\x84\'\x14\xf7\x8f\xbf\xdb\xc9\x07\'\x9d\xde\xf1\
\xc1\xf1*\xd2\xcfI\xda5\x92F\x19\x1dx(\x16\xa8\x99&\x8d\xf7\xec\xa2<\xd5$\
\xfd\xef9\xcetr\x1e\xe9;\x8e\x9f\xeb\x1d\x07\x1e"\xac\xfe\x97\xa2cz\x04\x9d\
\xdf\xd0\xb0]\x0f\x02\x05\tFH\xf4\x80\x17_\x1e\xb8\x17f\x95#\xf7\x8cU\'\xa5o\
)O50\xb5\x12XOu\xf7\x18\xf5w\xec$I\x12\xd2\xa7\xe7\x99\xed;\x1e8\xdb\xe5\x1b\
\xcb\xd9\x03\xc0S\xc0E\x82\xf7\x8bE*g]<\xde\xd4\xb8\x12\x02\x05\x89\xd1c\xf0\
\x14X<\xd9w\'\xce\xc3;\xee\x19\xafn\xf3\xfd\x9c\xf2T\x83\xf2T\x93\xea\xeeq\
\x0c\t\xd9s\xf3\xfc\xa8\xe7\xf8\xe8\xc9\x95\xc5U\xa7\x9f\x02\x9e\'\xa8L\xa1\
\xf1\xa3\xe0\xdf\xf0H\xfdZ\x08\x8c\x0ea=\x9d\xfa?\xe9\xb9\xd3\xf3\xca\xe1\
\xf7O\xd4\xb7k\xe6)O4 u\xb8\x93\x97\xf9\xca\x9a\xe5\xfeS\xab\x8b\xc0\x1f\x12\
\xfa\x9aE6.P\xaf\xab4?+\x02\x05\t\x19!q\xe2\x94\xd3\x8f\xde;]\x87n\x06\xbd\
\x9cs^\xf9\xe3\x97V\xe9y\xfd]\xc27\x84%\xc2\xdaR\x14\xeb\x96\x0b\xd4\xff\x16\
\x81\xd1\x94\xea\x01\xbd\x97\xfa\xee\xc5F\xadt\xef\xed\x135\x92R\xc2\'O\xae\
\xac\x9e\xea\xbb\xfb\t+\xeb\x02\xc1\xf3\xa3Js\xd5\xe0\xe1\xda\t\xc0F\x12)\
\xb0\xf6\xed\x95\xec\xec/oo\xdc\xfd\xd5\xa5\x94\x7f\xbe\xd0\xff#\xe04AmF=\
\x7f\xcd\xe0\xe1\xfa\x10\x80\x8d\xdf\xb4z\x80\xac:\x99\xfca\'\xff\x97\x8b\
\xb9<\xc3\xd6\x1a\x7f\xcd\xe0\xe1\xea\xbfR\xbe\xd6\xbb\x8a\xd6\xe3\x06\xa0I \
\x94\x10\x14\xa7\xcfu\xc8\xf9\xad~\xf4z\x8e\x82D\x19\xa8\xb2\x1ea\xcb\x16\
\x1b\xf2\xeb\xf5\x83\xd7{l\xfe\x8c\n\xaf\xfe|z]\x7f\xecg5FO\xd1\xae;\xf0\xb7\
\xc6\xff\x95\xf1?L\x9e\xff\xa2\xe6\n\x82a\x00\x00\x00\x00IEND\xaeB`\x82hi\
\xd5(' )

def get_bitmap():
    """Creates a bitmap from an image."""
    return BitmapFromImage(get_image())

def get_image():
    """Returns image from icon data."""
    stream = cStringIO.StringIO(get_data())
    return ImageFromStream(stream)

def get_icon():
    """Gets Icon for use with wxpoly."""
    icon = EmptyIcon()
    icon.CopyFromBitmap(get_bitmap())
    return icon

