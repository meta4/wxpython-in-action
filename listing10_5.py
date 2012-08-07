import wx

ID_SIMPLE = wx.NewId()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Enable/Disable Menu Example")

        p = wx.Panel(self)
        self.btn = wx.Button(p, -1, "Disable item", (20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnToggleItem, self.btn)

        menu = wx.Menu()
        menu.Append(ID_SIMPLE, "Simple menu item")
        self.Bind(wx.EVT_MENU, self.OnSimple, id=ID_SIMPLE)

        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self, event):
        wx.MessageBox("Simple menu item selected")

    def OnExit(self, event): 
        self.Close()

    def OnToggleItem(self, event):
        menubar = self.GetMenuBar()
        initialy_enabled = menubar.IsEnabled(ID_SIMPLE)
        menubar.Enable(ID_SIMPLE, not initialy_enabled)
        if initialy_enabled:
            label = "Enable Item"
        else:
            label = "Disable Item"
        self.btn.SetLabel(label)

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.MainLoop()
