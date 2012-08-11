import wx
import math
import random

class RadarGraph(wx.Window):
    def __init__(self, parent, title, labels):
        wx.Window.__init__(self, parent)
        self.title  = title
        self.labels = labels
        self.data   = [0.0] * len(labels)
        self.titleFont = wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.labelFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)

        self.InitBuffer()

        self.Bind(wx.EVT_SIZE,  self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnSize(self, evt):
        self.InitBuffer() # New buffer when the window changes size

    def OnPaint(self, evt):
        #buffered DC object automatically blits self.buffer to a
        #wx.PaintDC when the device context is destroyed
        dc = wx.BufferedPaintDC(self, self.buffer)

    def InitBuffer(self):
        "Create a new buffer"
        w, h = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(w, h)
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)

    def GetData(self):
        return self.data

    def SetData(self, newData):
        assert len(newData) == len(self.data)
        self.data = newData[:]
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.DrawGraph(dc)

    def PolarToCartesian(self, radius, angle, cx, cy):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return (cx+x, cy+y)

    def DrawGraph(self, dc):
        spacer = 10
        scaledmax = 150

        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dw, dh = dc.GetSize()

        dc.SetFont(self.titleFont)
        tw, th = dc.GetTextExtent(self.title)
        dc.DrawText(self.title, (dw-tw)/2, spacer) # draw title

        # compute plot center point
        th = th + spacer
        cx = dw / 2
        cy = (dh - th) / 2 + th
        
        # calculate scale factor
        mindim = min(cx, (dh-th)/2)
        scale = mindim/scaledmax

        dc.SetFont(self.labelFont)
        nvals = len(self.labels)
        angles = [i*360/nvals for i in range(nvals)]
        for val, label, angle in zip(self.data, self.labels, angles):
            x, y = self.PolarToCartesian(125*scale, angle, cx, cy)
            dc.DrawText(label, x, y)

        redThresh    = 95
        yellowThresh = 70
        maxval = max(self.data)
        if   redThresh    < maxval: c = "red"
        elif yellowThresh < maxval: c = "yellow"
        else:                       c = "forest green"

        dc.SetBrush(wx.Brush(c))
        dc.SetPen(wx.Pen("navy", 2))
        dc.DrawPolygon(
            [self.PolarToCartesian(val*scale, angle, cx, cy) 
             for val, angle in zip(self.data, angles)])

        # Draw target type axes
        dc.SetPen(wx.Pen('black', 1, wx.DOT))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawCircle(cx, cy,  25 * scale)
        dc.DrawCircle(cx, cy,  50 * scale)
        dc.DrawCircle(cx, cy,  75 * scale)
        dc.DrawCircle(cx, cy, 100 * scale)
        dc.SetPen(wx.Pen('red', 2, wx.SOLID))
        dc.DrawCircle(cx, cy, redThresh * scale)
        dc.SetPen(wx.Pen('yellow', 2, wx.SOLID))
        dc.DrawCircle(cx, cy, yellowThresh * scale)
        dc.SetPen(wx.Pen("black", 2))
        dc.DrawLine(cx-110*scale, cy, cx+110*scale, cy)
        dc.DrawLine(cx, cy-110*scale, cx, cy+110*scale)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          title="Double Buffered Drawing",
                          size=(480, 480))
        self.plot = RadarGraph(self, "Sample 'Radar' Plot",
                               'A B C D E F G H I J K L M N O P Q R S T'.split())

        # create start data
        data = [random.randint(0,25) for i in self.plot.GetData()]
#        data = [50 for i in self.plot.GetData()]
        self.plot.SetData(data)

        # Create a timer to update the data values
        self.Bind(wx.EVT_TIMER, self.OnTimeout)
        self.timer = wx.Timer(self)
        self.timer.Start(10)

    def OnTimeout(self, evt):
        # simulate positive & negative growth in each category
        data = []
        for d in self.plot.GetData():
            val = d + random.uniform(-2.5, 2.5)
            val = max(val,   0)
            val = min(val, 110)
            data.append(val)
        self.plot.SetData(data)

app = wx.PySimpleApp()
frm = TestFrame().Show()
app.MainLoop()
