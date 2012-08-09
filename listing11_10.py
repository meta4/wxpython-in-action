import wx

labels = "one two three four five six seven eight nine".split()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "StaticBoxSizer Test")
        self.panel = wx.Panel(self)

        box1 = self.MakeStaticBoxSizer("Box 1", labels[0:3])
        box2 = self.MakeStaticBoxSizer("Box 2", labels[3:6])
        box3 = self.MakeStaticBoxSizer("Box 3", labels[6:9])

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(box1, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(box2, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(box3, 1, wx.ALL | wx.EXPAND, 10)
        
        self.panel.SetSizer(sizer)
        sizer.Fit(self)

    def MakeStaticBoxSizer(self, boxLabel, itemLabels):
        box = wx.StaticBox(self.panel, -1, boxLabel)
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        for label in itemLabels:
            b = wx.Button(self.panel, label=label)
            sizer.Add(b, 1, wx.ALL | wx.EXPAND, 2)
        return sizer

app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
