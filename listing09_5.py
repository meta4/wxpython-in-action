import wx

app = wx.PySimpleApp()
progressMax = 10
dialog = wx.ProgressDialog("A Progress Box",
                           "I'm trying to think, but nut'n's hap'ning",
                           progressMax,
                           style = \
                            wx.PD_CAN_ABORT |
                           wx.PD_ELAPSED_TIME |
                           wx.PD_REMAINING_TIME |
                           wx.PD_AUTO_HIDE)
keepGoing = True
count = 0
while keepGoing and count < progressMax:
    count += 1
    wx.Sleep(1)
    keepGoing = dialog.Update(count)
dialog.Destroy()
