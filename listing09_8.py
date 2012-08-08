import wx

app = wx.PySimpleApp()
dia = wx.FontDialog(None, wx.FontData())
if dia.ShowModal() == wx.ID_OK:
    data = dia.GetFontData()
    font   = data.GetChosenFont()
    colour = data.GetColour()

    print 'you selected: "%s", %d points' % (
        font.GetFaceName(), font.GetPointSize())
dia.Destroy()
