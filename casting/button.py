import wx
import numpy
from PIL import Image

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color
from casting.menu import Menu

class Button(wx.Button):
    def __init__(self):
        super(Button, self).__init__()
        self.diceButtons()

    def diceButtons(self):
        """Creates the custom, d100, d20, d12, d10, d8, d6, and d4 buttons"""
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.d100_button = wx.Button(self, label='D100', pos=(5,425), size=(50,50))
        self.d100_button.SetFont(font)

        self.d20_button = wx.Button(self, label='D20', pos=(55,425), size=(50,50))
        self.d20_button.SetFont(font)

        self.d12_button = wx.Button(self, label='D12', pos=(105,425), size=(50,50))
        self.d12_button.SetFont(font)

        self.d10_button = wx.Button(self, label='D10', pos=(155,425), size=(50,50))
        self.d10_button.SetFont(font)

        self.d8_button = wx.Button(self, label='D8', pos=(205,425), size=(50,50))
        self.d8_button.SetFont(font)

        self.d6_button = wx.Button(self, label='D6', pos=(255,425), size=(50,50))
        self.d6_button.SetFont(font)

        self.d4_button = wx.Button(self, label='D4', pos=(305,425), size=(50,50))
        self.d4_button.SetFont(font)

        mainSizer.Add(self.d100_button, 0, wx.Center, 0)
        mainSizer.Add(self.d20_button, 0, wx.Center, 0)
        mainSizer.Add(self.d12_button, 0, wx.Center, 0)
        mainSizer.Add(self.d10_button, 0, wx.Center, 0)
        mainSizer.Add(self.d8_button, 0, wx.Center, 0)
        mainSizer.Add(self.d6_button, 0, wx.Center, 0)
        mainSizer.Add(self.d4_button, 0, wx.Center, 0)

        # img = Image.open('images/d20button.png')
        # d20_bitmap = wx.Bitmap(img)
        # #d20_image = wx.BitmapFromImage(d20_bitmap)
        # self.d20_button.SetBitmap(d20_bitmap)

        # img = wx.Image('d20button.png')
        # img = wx.Image.Rescale(img, 50, 50)
        # img = wx.IMAGE_QUALITY_HIGH
        # self.d20_button.SetBitmap(wx.Bitmap(img, wx.BITMAP_TYPE_PNG))

        mainSizer.Add(self.d20_button, 0, wx.Center, 0)    

    def choose_screen(self):
        """Creates the DM / Player select buttons"""
        font = wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL)

        """Creates the DM / Player select buttons"""
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.player_button = wx.Button(self, label='Player', pos=(600,150), size=(200,200))
        self.DM_button = wx.Button(self, label='Dungeon\nMaster', pos=(160,150), size=(200,200))
        self.player_button.SetFont(font)
        self.DM_button.SetFont(font)
        main_sizer.Add(self.DM_button, 1, wx.Left, 0)
        main_sizer.Add(self.player_button, 2, wx.Right, 0)

        """Makes it so the buttons will react when clicked"""
        self.Bind(wx.EVT_BUTTON, self.player_menu, self.player_button)
        self.Bind(wx.EVT_BUTTON, self.DM_menu, self.DM_button)   
        