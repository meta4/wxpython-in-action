import wx


class ScrollbarFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Scrollbar Example', size = (300,200))
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, 600, 400)
        self.button1 = self.make_button("Scroll Me",
                                        pos=(50, 20),
                                        callback=self.OnClickTop)
        self.button2 = self.make_button("Scroll Back",
                                        pos=(500, 350),
                                        callback=self.OnClickBottom)

    def make_button(self, label, pos, callback):
        button = wx.Button(self.scroll, -1, label, pos=pos)
        self.Bind(wx.EVT_BUTTON, callback, button)
        return button

    def OnClickTop(self, event):
        self.scroll.Scroll(600, 400)

    def OnClickBottom(self, event):
        self.scroll.Scroll(1,1)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    ScrollbarFrame().Show()
    app.MainLoop()
