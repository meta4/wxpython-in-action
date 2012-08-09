import wx
from listing11_01 import BlockWindow


class TestFrame(wx.Frame):
    def __init__(self, lables, col_sizes, row_sizes):
        wx.Frame.__init__(self, None, -1, "Resizing Flex Grid Sizer")
        sizer = wx.FlexGridSizer(rows=3, cols=3)#, hgap=5, vgap=5)

        for label in labels:
            bw = BlockWindow(self, label=label)
            if label == "five": bw.SetMinSize((150,50))
            sizer.Add(bw, 0,
                      flag=wx.GROW | wx.ALL, 
                      border = 5)

        for col, size in zip(range(len(col_sizes)), col_sizes):
            sizer.AddGrowableCol(col, size)

        for row, size in zip(range(len(row_sizes)), row_sizes):
            sizer.AddGrowableRow(row, size)

        self.SetSizer(sizer)
        self.Fit()

app = wx.PySimpleApp()

labels = "one two three four five six seven eight nine".split()
col_sizes = [1,2,1] # re-size proportions
row_sizes = [1,5,1]
TestFrame(labels, col_sizes, row_sizes).Show()
app.MainLoop()

