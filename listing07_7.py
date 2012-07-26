import wx

class SliderFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Slider Example', size=(350, 375))
        panel = wx.Panel(self, -1)
        self.count = 0
        slider = wx.Slider(panel, -1, 25, 1, 100, pos=(75,10),
                           size=(250, -1),
                           style= wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider.SetTickFreq(5, 1)
        slider = wx.Slider(panel, -1, 25, 1, 100, pos=(10, 80),
                           size=(-1, 250),
                           style= wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider.SetTickFreq(20, 1)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    SliderFrame().Show()
    app.MainLoop()

