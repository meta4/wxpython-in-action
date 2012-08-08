"""Basic Modal Dialog Example.

But, it doesn't show up on my machine here at work. I can press tab to
switch between the OK & CANCEL buttons and press enter to select it,
but the dialog is invisible.  (maybe it's off the screen.)

"""

import wx

class SubclassDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, 'Dialog Subclass', size=(300, 1))
        okButton = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        okButton.SetDefault()
        cancelButton = wx.Button(self, wx.ID_CANCEL, "CANCEL", pos=(115, 15))
        print "made it"
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    dialog = SubclassDialog()
    print "showing it"
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print "OK"
    else:
        print "CANCEL"
    dialog.Destroy()
