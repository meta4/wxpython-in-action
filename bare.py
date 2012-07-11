import wx

class App(wx.App):
    def OnInit(self):
        """Initialize the App Object
        
        Arguments:
        - `self`:
        """
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

app = App()
app.MainLoop()
