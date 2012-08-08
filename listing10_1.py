"""really simple menu that does nothing but show up"""

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Simple Menu Example")
        p = wx.Panel(self)
        menuBar = wx.MenuBar()
        menuBar.Append(wx.Menu(), "Left Menu")
        menuBar.Append(wx.Menu(), "Middle Menu")
        menuBar.Append(wx.Menu(), "Right Menu")
        self.SetMenuBar(menuBar)

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()

app.MainLoop()
