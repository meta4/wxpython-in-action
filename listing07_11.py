import wx

class RadioButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio Example', size=(200,140))
        self.panel = wx.Panel(self, -1)

        radioTextConfigs = [('Elmo',  10, wx.RB_GROUP),
                            ('Ernie', 40, 0),
                            ('Bert',  70, 0)]
        self.texts = {}
        for config in radioTextConfigs:
            self.buildOneRadioTextCtrl(*config)
        self.selectedText = self.texts['Elmo']
        self.selectedText.Enable(True)

    def buildOneRadioTextCtrl(self, label, ypos, style):
        radio = wx.RadioButton(self.panel, -1, label,  pos=(10, ypos), style=style)
        text  = wx.TextCtrl(   self.panel, -1, "",     pos=(70, ypos))
        self.texts[label] = text
        text.Enable(False)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, radio)

    def OnRadio(self, event):
        self.selectedText.Enable(False)  # Disable old text ctrl
        self.selectedText = \
            self.texts[event.GetEventObject().GetLabel()]# Get new ctrl
        self.selectedText.Enable(True)   # Enable new text ctrl


if __name__ == '__main__':
    app = wx.PySimpleApp()
    RadioButtonFrame().Show()
    app.MainLoop()

