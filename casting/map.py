import wx
from PIL import Image

class Map:
    def __init__(self):
        pass

    def display_map(self):
        """Creates the image for the map and displays it on the screen"""
        map_file = 'casting\map.png'
        map = wx.Image(map_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self, -1, map, (5,5))
        map_border = wx.StaticBox(self, wx.ID_ANY, size=(996,650), pos=(5,5))