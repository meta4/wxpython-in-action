"""An example that uses static text controls.

With Lots of options exercised.

Mon Jul 23, 2012 - 04:45 - PW
"""

import wx

def plain(win, str, pos):
    return wx.StaticText(win, -1, str, pos)

def reverse(win, str, pos, size=(-1,-1)):
    txt_ctrl = wx.StaticText(win, -1, str, pos, size)
    txt_ctrl.SetForegroundColour('white')
    txt_ctrl.SetBackgroundColour('black')

def centerReverse(win, str, pos, size):
    txt_ctrl = wx.StaticText(win, -1, str, pos, size, wx.ALIGN_CENTER)
    txt_ctrl.SetForegroundColour('white')
    txt_ctrl.SetBackgroundColour('black')

def right(win, str, pos, size=(-1,-1)):
    txt_ctrl = wx.StaticText(win, -1, str, pos, size, wx.ALIGN_RIGHT)
    txt_ctrl.SetForegroundColour('white')
    txt_ctrl.SetBackgroundColour('black')

def fancy(win, str, pos, size=(-1, -1)):
    txt_ctrl = wx.StaticText(win, -1, str, pos, size, style=wx.ST_NO_AUTORESIZE)
    font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
    txt_ctrl.SetFont(font)
    txt_ctrl.SetForegroundColour('red')
    txt_ctrl.SetBackgroundColour('light blue')

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Static Text Example",
                          size=(400, 300))
        panel = wx.Panel(self, -1)

        plain(         panel, "Plain text",     (100,  10))
        reverse(       panel, "Reverse Colors", (100,  30), (160, -1))
        centerReverse( panel, "align center",   (100,  50), (160, -1))
        right(         panel, "align right",    (100,  70), (160, -1))
        fancy(         panel, "Fancy font",     (100, 100), (160, 30))
        plain(panel,
              "Text can\nbe split\n"
              "over multiple lines\n\nEven blank ones",
              (20,150))
        right(panel,
              "Multi-line text\ncan also\n"
              "be right aligned\n\neven with a blank",
              (220, 150))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    StaticTextFrame().Show()
    app.MainLoop()
