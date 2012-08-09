"""Example using GridBagSizer.

I'm using wx.Button instead of the Block Window.  The Block window
does not re-paint properly, and I'm not going to spend the time now to
figure out why.
"""

import wx

class TestFrame(wx.Frame):
    def __init__(self, lables):
        wx.Frame.__init__(self, None, -1, "GridBagSizer Test")
        sizer = wx.GridBagSizer()

        for col in range(3):
            for row in range(3):
                bw = wx.Button(self, label=labels[row*3+col])
                sizer.Add(bw, pos=(row, col),
                          flag=wx.GROW | wx.ALL, 
                          border=2,
                          )

        bw = wx.Button(self, label="Span 3 rows")
        sizer.Add(bw, pos=(0,3), span=(3,1), flag=wx.GROW | wx.ALL, border=2)
        bw = wx.Button(self, label="\nSpan all columns\n\nLine 4 of text\n\n")
        sizer.Add(bw, pos=(3,0), span=(1,4), flag=wx.GROW | wx.ALL, border=2)
        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)

        self.SetSizer(sizer)
        self.Fit()

app = wx.PySimpleApp()

labels = "one two three four five six seven eight nine".split()
TestFrame(labels).Show()
app.MainLoop()
