import wx

class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Button Example", size=(300, 100))
        panel = wx.Panel(self, -1)
        self.createButton(panel)
        self.clickCount = 0

    def createButton(self, panel):
        self.button = wx.Button(panel, -1, "Hello", pos=(50, 20), size=(100,23))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        

    def OnClick(self, event):
        self.clickCount = self.clickCount + 1
        if self.clickCount % 10 == 0:
            label = "OI! (%d)" % self.clickCount
        else:
            label = "Click (%d)" % self.clickCount
        self.button.SetLabel(label)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    ButtonFrame().Show()
    app.MainLoop()


