import wx

class PanelFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel_type = kwargs.get('panel', wx.Panel)
        self.panel = panel_type(self)
    

filenames = ["image.%s" % ext for ext in "bmp gif jpg png".split()]

def makeGradient(nrows=100, ncols=100):
    import array
    img = wx.EmptyImage(ncols,nrows)
    a = array.array('B', img.GetData())
    for row in range(nrows):
        for col in range(ncols):
            colp = int(float(col) / ncols * 0xFF)
            rowp = int(float(row) / nrows * 0xFF)
            red   = rowp
            green = colp
            blue  = 0xFF - rowp
            i = (row * ncols + col) * 3
            a[i + 0] = red
            a[i + 1] = green
            a[i + 2] = blue
    img.SetData(a.tostring())
    return img

def scaleImg(img, n):
    new_width  = img.GetWidth()  * n
    new_height = img.GetHeight() * n
    return img.Scale(new_width, new_height)

class TestFrame(PanelFrame):
    def __init__(self):
        PanelFrame.__init__(self, None, title="Loading Images")
        self.fgs = wx.FlexGridSizer(cols=2, hgap=10, vgap=10)
        for name in filenames:
            img = wx.Image(name, wx.BITMAP_TYPE_ANY)
            self.addImageAndScaledImage(img)
        img = makeGradient(nrows=100, ncols=200)
        self.addImageAndScaledImage(img)
        self.panel.SetSizerAndFit(self.fgs)
        self.Fit()

    def addImageAndScaledImage(self, img_full):
        for img in [img_full, scaleImg(img_full, 3)]:
            sBmp = wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(img))
            self.fgs.Add(sBmp)

app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
