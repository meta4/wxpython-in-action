#!/usr/bin/env python

import wx
import images # TODO: What is the images library?

def build_menu_bar():
    def build_file_menu():
        fm = wx.Menu()
        return fm

    def build_edit_menu():
        em = wx.Menu()
        em.Append(wx.NewId(), "&Copy", "Copy in status bar")
        em.Append(wx.NewId(), "C&ut", "")
        em.Append(wx.NewId(), "Paste", "")
        em.AppendSeparator()
        em.Append(wx.NewId(), "&Options...", "Display Options")
        return em

    menuBar = wx.MenuBar()
    menuBar.Append(build_file_menu(), "&File")
    menuBar.Append(build_edit_menu(), "&Edit")
    return menuBar
        

class ToolbarFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar   = self.CreateToolBar()
        toolbar.AddSimpleTool(wx.NewId(),
                              images.getNewBitmap(),
                              "New",
                              "Long help for 'New'")
        toolbar.Realize()
        self.SetMenuBar(build_menu_bar())


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
