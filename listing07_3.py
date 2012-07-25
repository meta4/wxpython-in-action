import wx

def plain_txt(win, str):
    return wx.StaticText(win, -1, str)

def mline_txt(win, str, size):
    ctrl  = wx.TextCtrl(win, -1, str, size=size, style=wx.TE_MULTILINE)
    ctrl.SetInsertionPoint(0)
    return ctrl

def rich_txt(win, str, size):
    style = wx.TE_MULTILINE | wx.TE_RICH2
    ctrl  = wx.TextCtrl(win, -1, str, size=size, style=style)
    ctrl.SetInsertionPoint(0)
    return ctrl

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, 'Multiline Text Entry Example', size=(300, 250))
        panel = wx.Panel(self, -1)
        multiLabel = plain_txt(panel, "Multi-line")
        multiText  = mline_txt(
            panel,
            "Here is a looooooooooooooooooong line "
            "of text set in the contrell.\n\n"
            "See that it i wrapped, and that "
            "this line is after a blank line",
            size=(200, 100))
        richLabel = plain_txt(panel, "Rich Text")
        richText  = rich_txt(
            panel,
            "If supported by the native control, "
            "this is reversed, and this is a different font.",
            size=(200, 100))
        richText.SetStyle(44, 52, wx.TextAttr("white", "black"))
        points = richText.GetFont().GetPointSize()
        f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        richText.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColor, f))

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText, richLabel, richText])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    TextFrame().Show()
    app.MainLoop()


