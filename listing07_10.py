import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Checkbox Example", size=(150, 200))
        panel = wx.Panel(self, -1)

        boxes = [('Alpha', 40),
                 ('Beta',  60),
                 ('Gamma', 80)]
        for label, ypos in boxes:
            wx.CheckBox(panel, -1, label, (35, ypos), (150, 20))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()

