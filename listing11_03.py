import wx
from listing11_01 import BlockWindow

panels = [("one",   wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT),
          ("two",   wx.ALIGN_CENTER),
          ("three", wx.ALIGN_LEFT),
          ("four",  wx.ALIGN_RIGHT),
          ("five",  0),
          ("six",   wx.EXPAND),
          ("seven", wx.EXPAND),
          ("eight", wx.SHAPED),
          ("nine",  0)]

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "GridSizer Resizing")
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        for panel in panels:
            (label, flag) = panel
            bw = BlockWindow(self, label=label)
            sizer.Add(bw, 0, flag)
        self.SetSizer(sizer)
        self.Fit()

app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
