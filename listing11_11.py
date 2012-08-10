import wx

class TestFrame(wx.Frame): # inherit from PanelFrame
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '"Real World" sizer example')
        panel = wx.Panel(self)

        # 1st create controls
        topLbl = wx.StaticText(panel, -1, "Personal Information")
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        nameLbl = wx.StaticText(panel, -1, "Name:")
        name    = wx.TextCtrl(panel, -1, "")

        addrLbl = wx.StaticText(panel, -1, "Address:")
        addr1   = wx.TextCtrl(panel, -1, "")
        addr2   = wx.TextCtrl(panel, -1, "")

        cstLbl  = wx.StaticText(panel, -1, "City, State, Zip:")
        city    = wx.TextCtrl(panel, -1, "", size=(150,-1))
        state   = wx.TextCtrl(panel, -1, "", size=( 50,-1))
        zip     = wx.TextCtrl(panel, -1, "", size=( 70,-1))

        phoneLbl = wx.StaticText(panel, -1, "Phone:")
        phone    = wx.TextCtrl(panel, -1, "")

        emailLbl = wx.StaticText(panel, -1, "Email:")
        email    = wx.TextCtrl(panel, -1, "")

        saveBtn   = wx.Button(panel, -1, "Save")
        cancelBtn = wx.Button(panel, -1, "Cancel")

        # 2nd create layout

        # TopSizer is the top-level sizer
        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(topLbl, 0, wx.ALL, 5)
        topSizer.Add(wx.StaticLine(panel), 0,
                     wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        labelAlign = wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL
        # addrSizer - Grid that holds address info
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)

        addrSizer.Add(nameLbl, 0, labelAlign)
        addrSizer.Add(name,    0, wx.EXPAND)

        addrSizer.Add(addrLbl, 0, labelAlign)
        addrSizer.Add(addr1,   0, wx.EXPAND)
        addrSizer.Add((10,10)) # Empty Space in the label spot
        addrSizer.Add(addr2,   0, wx.EXPAND)

        # SubSizer for city, state, and zip fields
        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city,  1)
        cstSizer.Add(state, 0, wx.LEFT | wx.RIGHT, 5)
        cstSizer.Add(zip)

        # add SubSizer to addrSizer
        addrSizer.Add(cstLbl,   0, labelAlign)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        addrSizer.Add(phoneLbl, 0, labelAlign)
        addrSizer.Add(phone,    0, wx.EXPAND)

        addrSizer.Add(emailLbl, 0, labelAlign)
        addrSizer.Add(email,    0, wx.EXPAND)

        # add addrSizer to topSizer
        topSizer.Add(addrSizer, 0, wx.EXPAND | wx.ALL, 10)

        # create a button sizer with buttons in a row with resizable gaps
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(saveBtn)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(cancelBtn)
        btnSizer.Add((20,20), 1)
        
        # add btnSizer to main sizer
        topSizer.Add(btnSizer, 0, wx.EXPAND | wx.BOTTOM, 10)

        panel.SetSizer(topSizer)

        topSizer.Fit(self)
        topSizer.SetSizeHints(self) # prevent frame from getting to small

app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
