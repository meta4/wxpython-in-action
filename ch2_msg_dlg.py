#!/usr/bin/env python

import wx

def yes_no_dlg():
    app = wx.PySimpleApp()
    dlg = wx.MessageDialog(None,
                           'Is this the coolest thing ever?',
                           'MessageDialog',
                           wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
    result = dlg.ShowModal()
    dlg.Destroy()
    if result == wx.ID_YES:
        print "Totaly! Coolest thing evar!!"
    elif result == wx.ID_NO:
        print "Yeah, I meant LAMEST thing ever."
    elif result == wx.ID_CANCEL:
        print "I don't care about your answer anyway."

def ok_cancel_dlg():
    app = wx.PySimpleApp()
    dlg = wx.MessageDialog(None,
                           'Conquer the World?',
                           'Should we...',
                           wx.OK | wx.CANCEL | wx.ICON_QUESTION)
    result = dlg.ShowModal()
    dlg.Destroy()
    if result == wx.ID_CANCEL:
        print "World Conquest aborted."
    elif result == wx.ID_OK:
        print "Dude! you're pure evil!"

def text_entry_dlg():
    app = wx.PySimpleApp()
    dlg = wx.TextEntryDialog(
        None,
        "Who is buried in Grants tomb?",
        "A Question",
        "Cary Grant")
    if dlg.ShowModal() == wx.ID_OK:
        print "I can't believe you thought %s was burried in Grant's tomb" % \
            dlg.GetValue()
                             
def list_choser_dlg():
    app = wx.PySimpleApp()
    dlg = wx.SingleChoiceDialog(
        None,
        "What Version of Python are you using?",
        "Single Choice",
        ['1.5.2', '2.0', '2.1.3', '2.2', '2.3.1'] )
    if dlg.ShowModal() == wx.ID_OK:
        print "Really?  you are sure you are using %s" % \
            dlg.GetStringSelection()
    else:
        print "Did you know that was a trick question?"

# yes_no_dlg()
# ok_cancel_dlg()
# text_entry_dlg()
list_choser_dlg()
