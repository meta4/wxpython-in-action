
import wx

class SubclassFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Frame Subclass', size=(300, 100),
                          style=wx.CAPTION \
                              | wx.SYSTEM_MENU \
                              | wx.MINIMIZE_BOX \
                              | wx.CLOSE_BOX,
                          # style=wx.FRAME_TOOL_WINDOW \
                          #     | wx.CAPTION \
                          #     | wx.SYSTEM_MENU,
                          pos=(200,200))
        panel = wx.Panel(self, -1, size=(300,100))
        button = wx.Button(panel, -1, "Close Me", pos=(15,15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

    def OnCloseMe(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    SubclassFrame().Show()
    app.MainLoop()
