import wx


if __name__ == '__main__':
    app = wx.PySimpleApp()
    f = wx.Frame(None, -1, "A Frame",
                 style=wx.DEFAULT_FRAME_STYLE,
                 size=(200,100))
    f.Show()
    app.MainLoop()

