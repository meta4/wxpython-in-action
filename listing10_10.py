import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Fancier Menu Example")
        p = wx.Panel(self)
        menu = wx.Menu()

        bmp = wx.Bitmap("open.png", wx.BITMAP_TYPE_PNG)
        item =  wx.MenuItem(menu, -1, "Has Open Bitmap")
        item.SetBitmap(bmp)
        menu.AppendItem(item)

        if 'wxMSW' in wx.PlatformInfo:
            font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
            font.SetWeight(wx.BOLD)
            item = wx.MenuItem(menu, -1, "Has Bold Font")
            item.SetFont(font)
            menu.AppendItem(item)

            item = wx.MenuItem(menu, -1, "HasRedText")
            item.SetTextColour('red')
            menu.AppendItem(item)

        menu.AppendSeparator()
        exit = menu.Append(-1, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def OnExit(self, event):
        self.Close()

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.MainLoop()
