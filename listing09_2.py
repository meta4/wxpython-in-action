"""Realy simple yes/no Dialog example.

Uses 2 versions of the yes/no dialog.

BUT!  The two versions do not return the same kind of answer!
"""

import wx

def Evaluate_answer(ans):
    if ans == wx.ID_YES :
        print 'first kind of "yes"', ans
    elif ans == wx.YES:
        print 'second kind of "yes"', ans
    else:
        print "no", ans
    dlg.Destroy()
    

if __name__ == "__main__":
    app = wx.PySimpleApp()

    dlg = wx.MessageDialog(None, "Is this exlpanation OK?", 'A Message Box',
                           wx.YES_NO | wx.ICON_QUESTION)
    retCode = dlg.ShowModal()
    Evaluate_answer(retCode)

    retCode = wx.MessageBox("Is this way easier?", "Via Function",
                            wx.YES_NO | wx.ICON_QUESTION)
    Evaluate_answer(retCode)

