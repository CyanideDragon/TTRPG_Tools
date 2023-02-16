import wx
from PIL import Image

class Map:
    def __init__(self):
        pass

    def display_map(self):
        image_file = 'TTRPG_Tools\casting\map.png'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (5,5))
        #map = wx.StaticBox(self, wx.ID_ANY, size=(100,100), pos=(5,5))