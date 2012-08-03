import wx
import os

def build_wildcard(args):
    strs = ["%s (%s)|%s" % (k,v,v) for k,v in args]
    result = "|".join(strs)    
    return result

app = wx.PySimpleApp()
filter_options= [
    ("Python source code", "*.py" ),
    ("Compiled Python",    "*.pyc"),
    ("All files",          "*.*"  )]
wc = build_wildcard(filter_options)
# wildcard = \
#     "Python source (*.py)|*.py|" \
#     "Compiled Python (*.pyc)|*.pyc|" \
#     "All files (*.*)|*.*"
# print wc
# print wildcard
dialog = wx.FileDialog(None,
                       "Chose a file", os.getcwd(),
                       defaultFile = "", 
                       wildcard = wc,
                       style = wx.OPEN)
if dialog.ShowModal() == wx.ID_OK:
    print dialog.GetPath()
    print "File Type: %s" % filter_options[dialog.GetFilterIndex()][0]
dialog.Destroy()
