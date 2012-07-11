
import wx

def runframe(frame):
    """Short hand function to test sample wxPython frames"""
    app = wx.PySimpleApp()
    frame = frame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

