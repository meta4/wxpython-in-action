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

def dist(x1, y1, x2, y2):
    from math import sqrt
    x = x2 - x1
    y = y2 - y1
    return sqrt(x*x + y*y)

def alphaWasher(img, n):
    "Image must be n x n square"
    img.InitAlpha()
    coords = [(x,y) for x in range(n) for y in range(n)
              if dist(x,y, n/2, n/2) < n/4 or n/2 < dist(x,y, n/2, n/2)]
    for x, y in coords:
        img.SetAlpha(x,y,0)
    coords = [(x,y) for x in range(n) for y in range(n)
              if n/4 < dist(x,y, n/2, n/2) < n/3.9]
    print "l = %d" % len(coords)
    for x, y in coords: img.SetAlpha(x,y,0xAA)
    coords = [(x,y) for x in range(n) for y in range(n)
              if n/2 < dist(x,y, n/2, n/2) < n/1.99]
    print "l = %d" % len(coords)
    for x, y in coords: img.SetAlpha(x,y,0xAA)

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
        img = makeGradient(nrows=150, ncols=150)
        img = alphaWasher(img, 150)
        self.addImageAndScaledImage(img)
        self.panel.SetSizerAndFit(self.fgs)
        self.Fit()

    def addImageAndScaledImage(self, img_full):
        for img in [img_full, scaleImg(img_full, 1.5)]:
            sBmp = wx.StaticBitmap(self.panel, -1, wx.BitmapFromImage(img))
            self.fgs.Add(sBmp)

app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
