import wx
import numpy
from PIL import Image

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color
from casting.menu import Menu
from scripting.dice_roll_action import DiceRollAction

class Button(wx.Button):
    def __init__(self):
        super(Button, self).__init__()

    def diceButtons(self):
        """Creates the custom, d100, d20, d12, d10, d8, d6, and d4 buttons"""
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        d100_button = wx.Button(self, label='D100', pos=(5,400), size=(50,50))
        d100_button.SetFont(font)

        d20_button = wx.Button(self, label='D20', pos=(55,400), size=(50,50))
        d20_button.SetFont(font)

        d12_button = wx.Button(self, label='D12', pos=(105,400), size=(50,50))
        d12_button.SetFont(font)

        d10_button = wx.Button(self, label='D10', pos=(155,400), size=(50,50))
        d10_button.SetFont(font)

        d8_button = wx.Button(self, label='D8', pos=(205,400), size=(50,50))
        d8_button.SetFont(font)

        d6_button = wx.Button(self, label='D6', pos=(255,400), size=(50,50))
        d6_button.SetFont(font)

        d4_button = wx.Button(self, label='D4', pos=(305,400), size=(50,50))
        d4_button.SetFont(font)

        mainSizer.Add(d100_button, 0, wx.Center, 0)
        mainSizer.Add(d20_button, 0, wx.Center, 0)
        mainSizer.Add(d12_button, 0, wx.Center, 0)
        mainSizer.Add(d10_button, 0, wx.Center, 0)
        mainSizer.Add(d8_button, 0, wx.Center, 0)
        mainSizer.Add(d6_button, 0, wx.Center, 0)
        mainSizer.Add(d4_button, 0, wx.Center, 0)

        """Adding buttons to hold the totals of the rolls"""
        total_100_Button = wx.Button(self, label='total', pos=(5,450), size=(50,25))
        total_20_Button = wx.Button(self, label='total', pos=(55,450), size=(50,25))
        total_12_Button = wx.Button(self, label='total', pos=(105,450), size=(50,25))
        total_10_Button = wx.Button(self, label='total', pos=(155,450), size=(50,25))
        total_8_Button = wx.Button(self, label='total', pos=(205,450), size=(50,25))
        total_6_Button = wx.Button(self, label='total', pos=(255,450), size=(50,25))
        total_4_Button = wx.Button(self, label='total', pos=(305,450), size=(50,25))

        mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        mainsizer.Add(total_100_Button, 0, wx.Center, 0)
        mainsizer.Add(total_20_Button, 0, wx.Center, 0)
        mainsizer.Add(total_12_Button, 0, wx.Center, 0)
        mainsizer.Add(total_10_Button, 0, wx.Center, 0)
        mainsizer.Add(total_8_Button, 0, wx.Center, 0)
        mainsizer.Add(total_6_Button, 0, wx.Center, 0)
        mainsizer.Add(total_4_Button, 0, wx.Center, 0)

        """Roll dice on click"""
        button = Button
        d100_button.Bind(wx.EVT_BUTTON, total_100_Button.SetLabel(button.onRollDice(self, 100)))
        d20_button.Bind(wx.EVT_BUTTON, total_20_Button.SetLabel(button.onRollDice(self, 20)))
        d12_button.Bind(wx.EVT_BUTTON, total_12_Button.SetLabel(button.onRollDice(self, 12)))
        d10_button.Bind(wx.EVT_BUTTON, total_10_Button.SetLabel(button.onRollDice(self, 10)))
        d8_button.Bind(wx.EVT_BUTTON, total_8_Button.SetLabel(button.onRollDice(self, 8)))
        d6_button.Bind(wx.EVT_BUTTON, total_6_Button.SetLabel(button.onRollDice(self, 6)))
        d4_button.Bind(wx.EVT_BUTTON, total_4_Button.SetLabel(button.onRollDice(self, 4)))

    def onRollDice(self, num):
        """Get the random number from the Roll Dice class"""
        roller = DiceRollAction()
        total = roller.execute(num)
        # total_string = str(total[2])
        # total_Button = wx.Button(self, label=total_string, pos=(100,100), size=(50,50))
        # mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        # mainsizer.Add(total_Button, 0, wx.Center, 0) 
        return str(total[2])      
         