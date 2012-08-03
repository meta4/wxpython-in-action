import wx

app = wx.PySimpleApp()
dia = wx.ColourDialog(None)
dia.GetColourData().SetChooseFull(False) # does not work for me.
if dia.ShowModal() == wx.ID_OK:
    d = dia.GetColourData()
    print 'You selected: %s' % str(d.GetColour().Get())
dia.Destroy()
