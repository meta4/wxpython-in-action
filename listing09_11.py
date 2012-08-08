import wx
import wx.wizard

class TitledPage(wx.wizard.WizardPageSimple):
    def __init__(self, parent, title):
        wx.wizard.WizardPageSimple.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        titleText = wx.StaticText(self, -1, title)
        titleText.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.sizer.Add(titleText, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        self.sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)

    def add(self, content):
        self.sizer.Add(content)

    def add_text(self, str):
        self.add(wx.StaticText(self, -1, str))

def chain_wizard_pages(pages):
    for (p1, p2) in zip( pages[:-1], pages[1:]):
        wx.wizard.WizardPageSimple_Chain(p1, p2)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    wizard = wx.wizard.Wizard(None, -1, "Simple Wizard")
    titles = ["Welcome", "You're doing great!", "Keep going.", "All done!"]
    pages = [TitledPage(wizard, title) for title in titles]

    pages[0].add_text('Testing the Wizard')
    pages[3].add_text('This is the last page')
    pages[3].add_text('Press "Finish" to SUCCEED')
    pages[3].add_text('Press "Cancel" to FAIL')
    pages[3].add_text('Press "Back" to postpone the decision')

    # need more data driven wizard construction.

    chain_wizard_pages(pages)
    wizard.FitToPage(pages[0])
    if wizard.RunWizard(pages[0]): print"Success!"
