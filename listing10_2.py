import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Menu Example with Status Bar")
        p = wx.Panel(self)
        self.CreateStatusBar()

        menu = wx.Menu()
        simple = menu.Append(-1, "Simple menu item",
                              "This is some help text")
        menu.AppendSeparator()
        exit = menu.Append(-1, "Exit", "Exit the program")
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self, event): wx.MessageBox("Simple menu item selected!")
    def OnExit(self, event): self.Close()

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.MainLoop()
