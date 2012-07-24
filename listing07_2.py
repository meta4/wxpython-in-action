import wx

def plain_txt(win, str):
    return wx.StaticText(win, -1, str)

def basic_input(win, str, size):
    ctrl = wx.TextCtrl(win, -1, str, size=size)
    ctrl.SetInsertionPoint(0)
    return ctrl

def pwd_input(win, str, size):
    ctrl = wx.TextCtrl(win, -1, str, size=size, style=wx.TE_PASSWORD)
    ctrl.SetInsertionPoint(0)
    return ctrl

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(300, 100))
        panel = wx.Panel(self, -1)

        basicLabel = plain_txt(  panel, "Basic Control:")
        basicText  = basic_input(panel, "I've entered some text!", (175, -1))
        pwdLabel   = plain_txt(  panel, "Password:")
        pwdText    = pwd_input(  panel, "Password", (175, -1))
        
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basicLabel, basicText, pwdLabel, pwdText])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    TextFrame().Show()
    app.MainLoop()
