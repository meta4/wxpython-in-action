import wx

def twoStepCreate(instance, preClass, preInitFunc, *args, **kwargs):
    pre = preClass()
    preInitFunc(pre)
    pre.Create(*args, **kwargs)
    instance.PostCreate(pre)

class HelpFrame(wx.Frame):
    def __init__(self,
                 parent,
                 id,
                 title,
                 pos=wx.DefaultPosition,
                 size=(300,100),
                 style=wx.DEFAULT_DIALOG_STYLE):
        twoStepCreate(self, wx.PreFrame, self.preInit, parent,
                      id, title, pos, size, style)

    def preInit(self, pre):
        pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    HelpFrame(None, -1, "A Help Frame").Show()
    app.MainLoop()


