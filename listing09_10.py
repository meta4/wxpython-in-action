import wx
import wx.lib.imagebrowser as imagebrowser

app = wx.PySimpleApp()
dia = imagebrowser.ImageDialog(None)
if dia.ShowModal() == wx.ID_OK:
    print "File : %s" % dia.GetFile()
dia.Destroy()
