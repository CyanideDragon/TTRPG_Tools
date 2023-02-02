import wx

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color

class Button(wx.Button):
    def __init__(self):
        super(Button, self).__init__()
        self.diceButtons()

    def diceButtons(self):
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.d20_button = wx.Button(self, label='D20', pos=(200,200), size=(50,50))
        self.d20_button.SetFont(font)
        #d20_image = wx.Bitmap('d20button.png')
        #self.d20_button.SetBitmap(d20_image)
        mainSizer.Add(self.d20_button, 0, wx.Center, 0)        
        