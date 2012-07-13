"""This example adds a nice status bar and a menu to a SketchWindow
frame"""

import wx
from SketchWindow import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                          size=(800, 600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def updateStatusBar(self, posTuple):
        statuses = [
            "Pos: %s"         % str(posTuple),
            "current Pts: %s" % len(self.sketch.curLine),
            "Line Count: %s"  % len(self.sketch.lines) ]
        for i, status in enumerate(statuses):
            self.statusbar.SetStatusText(status, i)
        

    def OnSketchMotion(self, event):
        self.updateStatusBar(event.GetPositionTuple())
        event.Skip() # Pass the event on so SketchFrame can handle it too

    def menuConfig(self):
        return [("&File", (
                    ("&New",  "New sketch file",  self.OnNew ),
                    ("&Open", "Open sketch file", self.OnOpen),
                    ("&Save", "Save sketch file", self.OnSave),
                    ("", "", ""),
                    ("&Color", (
                            ("&Black", "", self.OnColor, wx.ITEM_RADIO),
                            ("&Red",   "", self.OnColor, wx.ITEM_RADIO),
                            ("&Green", "", self.OnColor, wx.ITEM_RADIO),
                            ("&Blue",  "", self.OnColor, wx.ITEM_RADIO))),
                    ("", "", ""),
                    ("&Quit", "Quit", self.OnCloseWindow)))]

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for menu in self.menuConfig():
            label = menu[0]
            items = menu[1]
            menuBar.Append(self.createMenu(items), label)
        self.SetMenuBar(menuBar)

    def createMenu(self, items):
        menu = wx.Menu()
        for item in items:
            if len(item) == 2:
                label    = item[0]
                subItems = item[1]
                subMenu = self.createMenu(subItems)
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *item)
        return menu

    def createMenuItem(self, menu, label, status, handler,
                       kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self, event): pass
    def OnOpen(self, event): pass
    def OnSave(self, event): pass
    
    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = str(item.GetLabel())
        print "New colour: %s" % color
        self.sketch.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
