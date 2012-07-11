#!/usr/bin/env python

import wx
import sys

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print "3. Frame __init__"
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print "1. App __init__"
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print "2. OnInit" # Writing to stdout
        self.frame = Frame(parent=None, id=-1, title='startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr, "7. A pretend error message"
        return True

    def OnExit(self):
        print "5. OnExit"

if __name__ == '__main__':
    app = App(redirect=True) # redirection starts here
    print "4. Before MainLoop"
    app.MainLoop()
    print "6. After MainLoop"
