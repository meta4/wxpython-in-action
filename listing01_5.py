import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame("Hello World", (50, 60), (450, 340))
        frame.Show()
        self.SetTopWindow(frame)
        return True

class MyFrame(wx.Frame):

    def __init__(self,title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)

        menuFile = wx.Menu()
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)

        menuBar.Append(menuFile, "&File")

        menuFile.Append(1, "&About...")
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)

        menuFile.AppendSeparator()

        menuFile.Append(2, "E&xit")
        self.Bind(wx.EVT_MENU, self.OnQuit,  id=2)

        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample",
                      "About Hello World",
                      wx.OK | wx.ICON_INFORMATION,
                      self)

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
