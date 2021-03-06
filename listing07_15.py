import wx

class ComboBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Combo Box Example", size=(350, 300))
        panel = wx.Panel(self, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four',
                      'five', 'six', 'seven', 'eight']
        wx.StaticText(panel, -1, "Select One:", (15, 15))
        wx.ComboBox(panel, -1, "pick 1", ( 15, 30), (100, -1), #wx.DefaultSize,
                    sampleList, wx.CB_DROPDOWN)
        wx.ComboBox(panel, -1, "pick 1", (150, 30), (100, -1), # wx.DefaultSize,
                    sampleList, wx.CB_SIMPLE)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    ComboBoxFrame().Show()
    app.MainLoop()


