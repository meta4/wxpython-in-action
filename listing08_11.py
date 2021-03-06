import wx
import vippi_image

class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Shaped Window",
                          style=wx.FRAME_SHAPED | wx.SIMPLE_BORDER |
                              wx.FRAME_NO_TASKBAR)

        self.hasShape = False
        self.bmp = vippi_image.getVippiBitmap()
        self.SetClientSize((self.bmp.GetWidth(), self.bmp.GetHeight()))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)
        self.SetWindowShape()
        self.Bind(wx.EVT_LEFT_DCLICK,   self.OnDoubleClick)
        self.Bind(wx.EVT_LEFT_DOWN,     self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,       self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,        self.OnMouseMove)
        self.Bind(wx.EVT_RIGHT_UP,      self.OnExit)
        self.Bind(wx.EVT_PAINT,         self.OnPaint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def SetWindowShape(self, EVT=None):
        r = wx.RegionFromBitmap(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnDoubleClick(self, evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape = False
        else:
            self.SetWindowShape()

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def OnExit(self, evt):
        self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    ShapedFrame().Show()
    app.MainLoop()

