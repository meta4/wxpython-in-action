import wx

about_txt = "Hover over buttons to see\ndifferent cursor types."

class CursorTestFrame(wx.Frame):

    buttonConfigs = [
        ("ARROW",          wx.CURSOR_ARROW),
        ("ARROWWAIT",      wx.CURSOR_ARROWWAIT),
        ("BLANK",          wx.CURSOR_BLANK),
        ("BULLSEYE",       wx.CURSOR_BULLSEYE),
        ("CROSS",          wx.CURSOR_CROSS),
        ("HAND",           wx.CURSOR_HAND),
        ("IBEAM",          wx.CURSOR_IBEAM),
        ("LEFT_BUTTON",    wx.CURSOR_LEFT_BUTTON),
        ("MAGNIFIER",      wx.CURSOR_MAGNIFIER),
        ("MIDDLE_BUTTON",  wx.CURSOR_MIDDLE_BUTTON),
        ("NO_ENTRY",       wx.CURSOR_NO_ENTRY),
        ("PAINT_BRUSH",    wx.CURSOR_PAINT_BRUSH),
        ("PENCIL",         wx.CURSOR_PENCIL),
        ("POINT_LEFT",     wx.CURSOR_POINT_LEFT),
        ("POINT_RIGHT",    wx.CURSOR_POINT_RIGHT),
        ("QUESTION_ARROW", wx.CURSOR_QUESTION_ARROW),
        ("RIGHT_ARROW",    wx.CURSOR_RIGHT_ARROW),
        ("RIGHT_BUTTON",   wx.CURSOR_RIGHT_BUTTON),
        ("SIZENS",         wx.CURSOR_SIZENS),
        ("SIZEWE",         wx.CURSOR_SIZEWE),
        ("SIZENESW",       wx.CURSOR_SIZENESW),
        ("SIZENWSE",       wx.CURSOR_SIZENWSE),
        ("SIZING",         wx.CURSOR_SIZING),
        ("SPRAYCAN",       wx.CURSOR_SPRAYCAN),
        ("WAIT",           wx.CURSOR_WAIT),
        ("WATCH",          wx.CURSOR_WATCH),
        ]

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "cursor example")
        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, about_txt,
                              style=wx.ALIGN_CENTER | wx.EXPAND,
                              size=(300, -1))
        label.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(label, 0, wx.EXPAND)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

        for label, cursorType in self.buttonConfigs:
            b = wx.Button(self, label=label, size=(300,30))
            b.SetCursor(wx.StockCursor(cursorType))
            sizer.Add(b, wx.EXPAND, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
            
app = wx.PySimpleApp()
CursorTestFrame().Show()
app.MainLoop()
