"""This example adds a nice status bar to a SketchWindow frame"""

import wx
from SketchWindow import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                          size=(800, 600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def OnSketchMotion(self, event):
        statuses = [
            "Pos: %s" % str(event.GetPositionTuple()),
            "current Pts: %s" % len(self.sketch.curLine),
            "Line Count: %s" % len(self.sketch.lines) ]
            
        for i, status in enumerate(statuses):
            self.statusbar.SetStatusText(status, i)
        event.Skip() # Pass the event on so SketchFrame can handle it too

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
