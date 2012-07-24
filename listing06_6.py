"""This example adds a open and close dialog option to the sketch app.

And associated functionality
"""

import cPickle
import os
import wx
from SketchWindow import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        self.title = "Sketch Frame"
        wx.Frame.__init__(self, parent, -1, self.title,
                          size=(800, 600))
        self.filename = ""
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()
        self.createToolBar()

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
        

    def menuConfig(self):
        return [("&File", (
                    ("&New",     "New sketch file",      self.OnNew ),
                    ("&Open",    "Open sketch file",     self.OnOpen),
                    ("&Save",    "Save sketch file",     self.OnSave),
                    ("Save &as", "Save new sketch file", self.OnSaveAs),
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

    def toolbarData(self):
        return (("New",  "new.bmp",  "Create new sketch",    self.OnNew),
                ("", "", "", ""),
                ("Open", "open.bmp", "Open existing sketch", self.OnOpen),
                ("Save", "save.bmp", "Save existing sketch", self.OnSave))

    def toolbarColorData(self):
        return("Black", "Red", "Green", "Blue")

    def createToolBar(self):
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)
        toolbar.AddSeparator()
        for each in self.toolbarColorData():
            self.createColorTool(toolbar, each)
        toolbar.Realize()

    def createSimpleTool(self, toolbar, label, filename, help, handler):
        if not label:
            toolbar.AddSeparator()
            return
        bmp = wx.Image(filename, wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        tool = toolbar.AddSimpleTool(-1, bmp, label, help)
        self.Bind(wx.EVT_MENU, handler, tool)

    def createColorTool(self, toolbar, color):
        bmp = self.MakeBitmap(color)
        newId = wx.NewId()
        tool = toolbar.AddRadioTool(-1, bmp, shortHelp=color)
        self.Bind(wx.EVT_MENU, self.OnColor, tool)

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def SaveFile(self):
        if self.filename:
            data = self.sketch.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()

    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                self.sketch.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a sketch file."
                              % self.filename, "oops!",
                              style = wx.OK | wx.ICON_EXCLAMATION)

    wildcard = "Sketch files (*.sketch)|*.sketch|All Files (*.*)|*.*"

    def OnSketchMotion(self, event):
        self.updateStatusBar(event.GetPositionTuple())
        event.Skip() # Pass the event on so SketchFrame can handle it too

    def OnNew(self, event): pass

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, "Open sketch file...",
                            os.getcwd(),
                            style=wx.OPEN,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + ' -- ' + self.filename)
        dlg.Destroy()

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, "Save sketch as...",
                            os.getcwd(),
                            style=wx.SAVE | wx.OVERWRITE_PROMPT,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:
                filename = filename + '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + ' == ' + self.filename)
        dlg.Destroy()
    
    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        if not item:
            toolbar = self.GetToolBar()
            item = toolbar.FindById(itemId)
            color = item.GetShortHelp()
        else:
            color = str(item.GetLabel())
        print "New colour: %s" % color
        self.sketch.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == "__main__":
#    app = wx.PySimpleApp()
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
