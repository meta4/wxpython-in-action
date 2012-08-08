import wx
import os

app = wx.PySimpleApp()
dia = wx.DirDialog(
    None,
    message = "Choose a directory",
    style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON,
    defaultPath=os.getcwd())
if dia.ShowModal() == wx.ID_OK: print dia.GetPath()
dia.Destroy()
