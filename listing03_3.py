#!/usr/bin/env python

from random import choice

from runframe import runframe
import wx

class MouseEventFrame(wx.Frame):
    

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent ,id, 'Frame With Button',
                          size=(300, 100))
        self.colors = [ 'Green', 'Red', 'Blue', 'Yellow' ]
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel,
                                label="Not Over",
                                pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)


    def OnButtonClick(self, event):
        new_color = choice(self.colors)
        self.panel.SetBackgroundColour(new_color)
        self.panel.Refresh()

    def OnEnterWindow(self, event):
        self.button.SetLabel("OverMe!")
        event.Skip()

    def OnLeaveWindow(self, event):
        self.button.SetLabel("Not Over")
        event.Skip()
        
            
            
if __name__ == '__main__':
    runframe(MouseEventFrame)
