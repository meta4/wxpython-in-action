import wx

class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Bitmap Button Example',
                          size=(200, 150))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("button_bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = \
            self.bmpButton(panel, bmp,
                           callback=self.OnClick,
                           pos=(10,20))
        self.button.SetDefault()
        self.button2 = \
            self.bmpButton(panel, bmp,
                           callback=self.OnClick,
                           pos=(100,20),
                           style=0)

    def bmpButton(self, win, bmp, pos, callback, style=wx.BU_AUTODRAW):
        ctrl = wx.BitmapButton(win, -1, bmp, pos, style=style)
        self.Bind(wx.EVT_BUTTON, callback, ctrl)
        return ctrl

    def OnClick(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    BitmapButtonFrame().Show()
    app.MainLoop()

