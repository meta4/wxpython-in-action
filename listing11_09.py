"""Examples of box sizers

The text used inheritance in this example for each of the frames.  I
went hog wild with this idea, and refactored all their code.

I think my version makes the distinction between each example clearer.
"""

import wx

labels = "one two three four".split()

class BaseBoxSizerFrame(wx.Frame):
    title = "none"
    sizer_type = None # descendant classes set

    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title)
        sizer = wx.BoxSizer(self.sizer_type)
        for label in labels:
            b = self.myButton(label)
            sizer.Add(b, flag=wx.EXPAND)        
        self.addLastButtonsToSizer(sizer)
        self.SetSizer(sizer)
        self.Fit()

    def addLastButtonsToSizer(self, sizer):
        pass

    def myButton(self, label):
        return wx.Button(self, label=label, size=(150,30))

class VBoxSizerFrame(BaseBoxSizerFrame):
    title = "Vertical BoxSizer"
    sizer_type = wx.VERTICAL

class HBoxSizerFrame(BaseBoxSizerFrame):
    title = "Horizontal BoxSizer"
    sizer_type = wx.HORIZONTAL

class VBoxSizerStretchableFrame(VBoxSizerFrame):
    title = "Stretch BoxSizer"

    def addLastButtonsToSizer(self, sizer):
        'Add one button that takes all the free space'
        b = self.myButton("Gets all free space")
        sizer.Add(b, 1, wx.EXPAND)

class VBoxSizerMultiProportionalFrame(VBoxSizerFrame):
    title = "Proportional BoxSizer"

    def addLastButtonsToSizer(self, sizer):
        'Add two buttons. One takes 1/3 the free space; the other takes 2/3'
        buttons = [("Gets 1/3 free space", 1), ("Gets 2/3 free space", 2)]
        for label, proportion in buttons:
            b = self.myButton(label)
            sizer.Add(b, proportion, wx.EXPAND)

frameClasses = [
    VBoxSizerFrame,
    HBoxSizerFrame,
    VBoxSizerStretchableFrame,
    VBoxSizerMultiProportionalFrame,
    ]

app = wx.PySimpleApp()
for frameClass in frameClasses:
    frameClass().Show()
app.MainLoop()
