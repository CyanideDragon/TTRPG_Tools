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
        
        d100_button = wx.Button(self, label='D100', pos=(5,665), size=(50,50))
        d100_button.SetFont(font)

        d20_button = wx.Button(self, label='D20', pos=(55,665), size=(50,50))
        d20_button.SetFont(font)

        d12_button = wx.Button(self, label='D12', pos=(105,665), size=(50,50))
        d12_button.SetFont(font)

        d10_button = wx.Button(self, label='D10', pos=(155,665), size=(50,50))
        d10_button.SetFont(font)

        d8_button = wx.Button(self, label='D8', pos=(205,665), size=(50,50))
        d8_button.SetFont(font)

        d6_button = wx.Button(self, label='D6', pos=(255,665), size=(50,50))
        d6_button.SetFont(font)

        d4_button = wx.Button(self, label='D4', pos=(305,665), size=(50,50))
        d4_button.SetFont(font)

        """Adds the editable textboxes for dice roll numbers"""
        text_100 = wx.TextCtrl(self, size=(20,25), pos=(20,715))
        text_100.SetValue('0')

        text_20 = wx.TextCtrl(self, size=(20,25), pos=(70,715))
        text_20.SetValue('0')

        text_12 = wx.TextCtrl(self, size=(20,25), pos=(120,715))
        text_12.SetValue('0')

        text_10 = wx.TextCtrl(self, size=(20,25), pos=(170,715))
        text_10.SetValue('0')

        text_8 = wx.TextCtrl(self, size=(20,25), pos=(220,715))
        text_8.SetValue('0')

        text_6 = wx.TextCtrl(self, size=(20,25), pos=(270,715))
        text_6.SetValue('0')

        text_4 = wx.TextCtrl(self, size=(20,25), pos=(320,715))
        text_4.SetValue('0')

        """Creates the buttons to add dice"""
        plus_100_Button = wx.Button(self, label='+', pos=(40,715), size=(15,25))
        plus_100_Button.Bind(wx.EVT_BUTTON, lambda event: text_100.SetValue(str(int(text_100.GetValue()) + 1)))
        
        plus_20_Button = wx.Button(self, label='+', pos=(90,715), size=(15,25))
        plus_20_Button.Bind(wx.EVT_BUTTON, lambda event: text_20.SetValue(str(int(text_20.GetValue()) + 1)))

        plus_12_Button = wx.Button(self, label='+', pos=(140,715), size=(15,25))
        plus_12_Button.Bind(wx.EVT_BUTTON, lambda event: text_12.SetValue(str(int(text_12.GetValue()) + 1)))

        plus_10_Button = wx.Button(self, label='+', pos=(190,715), size=(15,25))
        plus_10_Button.Bind(wx.EVT_BUTTON, lambda event: text_10.SetValue(str(int(text_10.GetValue()) + 1)))

        plus_8_Button = wx.Button(self, label='+', pos=(240,715), size=(15,25))
        plus_8_Button.Bind(wx.EVT_BUTTON, lambda event: text_8.SetValue(str(int(text_8.GetValue()) + 1)))

        plus_6_Button = wx.Button(self, label='+', pos=(290,715), size=(15,25))
        plus_6_Button.Bind(wx.EVT_BUTTON, lambda event: text_6.SetValue(str(int(text_6.GetValue()) + 1)))

        plus_4_Button = wx.Button(self, label='+', pos=(340,715), size=(15,25))
        plus_4_Button.Bind(wx.EVT_BUTTON, lambda event: text_4.SetValue(str(int(text_4.GetValue()) + 1)))

        """Creats the buttons to subtract dice"""
        minus_100_Button = wx.Button(self, label='-', pos=(5,715), size=(15,25))
        minus_100_Button.Bind(wx.EVT_BUTTON, lambda event: text_100.SetValue(str(int(text_100.GetValue()) - 1)))
        
        minus_20_Button = wx.Button(self, label='-', pos=(55,715), size=(15,25))
        minus_20_Button.Bind(wx.EVT_BUTTON, lambda event: text_20.SetValue(str(int(text_20.GetValue()) - 1)))
        
        minus_12_Button = wx.Button(self, label='-', pos=(105,715), size=(15,25))
        minus_12_Button.Bind(wx.EVT_BUTTON, lambda event: text_12.SetValue(str(int(text_12.GetValue()) - 1)))
        
        minus_10_Button = wx.Button(self, label='-', pos=(155,715), size=(15,25))
        minus_10_Button.Bind(wx.EVT_BUTTON, lambda event: text_10.SetValue(str(int(text_10.GetValue()) - 1)))
        
        minus_8_Button = wx.Button(self, label='-', pos=(205,715), size=(15,25))
        minus_8_Button.Bind(wx.EVT_BUTTON, lambda event: text_8.SetValue(str(int(text_8.GetValue()) - 1)))
        
        minus_6_Button = wx.Button(self, label='-', pos=(255,715), size=(15,25))
        minus_6_Button.Bind(wx.EVT_BUTTON, lambda event: text_6.SetValue(str(int(text_6.GetValue()) - 1)))
        
        minus_4_Button = wx.Button(self, label='-', pos=(305,715), size=(15,25))
        minus_4_Button.Bind(wx.EVT_BUTTON, lambda event: text_4.SetValue(str(int(text_4.GetValue()) - 1)))
        
        """Adding buttons to hold the totals of the rolls"""
        total_100_Button = wx.Button(self, label='total', pos=(5,740), size=(50,25))
        total_20_Button = wx.Button(self, label='total', pos=(55,740), size=(50,25))
        total_12_Button = wx.Button(self, label='total', pos=(105,740), size=(50,25))
        total_10_Button = wx.Button(self, label='total', pos=(155,740), size=(50,25))
        total_8_Button = wx.Button(self, label='total', pos=(205,740), size=(50,25))
        total_6_Button = wx.Button(self, label='total', pos=(255,740), size=(50,25))
        total_4_Button = wx.Button(self, label='total', pos=(305,740), size=(50,25))

        """Roll dice on click"""
        button = Button
        d100_button.Bind(wx.EVT_BUTTON, lambda event: total_100_Button.SetLabel(button.onRollDice(self, 100, int(text_100.GetValue()))))
        d20_button.Bind(wx.EVT_BUTTON, lambda event: total_20_Button.SetLabel(button.onRollDice(self, 20, int(text_20.GetValue()))))
        d12_button.Bind(wx.EVT_BUTTON, lambda event: total_12_Button.SetLabel(button.onRollDice(self, 12, int(text_12.GetValue()))))
        d10_button.Bind(wx.EVT_BUTTON, lambda event: total_10_Button.SetLabel(button.onRollDice(self, 10, int(text_10.GetValue()))))
        d8_button.Bind(wx.EVT_BUTTON, lambda event: total_8_Button.SetLabel(button.onRollDice(self, 8, int(text_8.GetValue()))))
        d6_button.Bind(wx.EVT_BUTTON, lambda event: total_6_Button.SetLabel(button.onRollDice(self, 6, int(text_6.GetValue()))))
        d4_button.Bind(wx.EVT_BUTTON, lambda event: total_4_Button.SetLabel(button.onRollDice(self, 4, int(text_4.GetValue()))))

    def onRollDice(self, dice_size, dice_amount):
        """Check if no dice are being rolled"""
        if dice_amount <= 0:
            return str(0)

        """Get the random number from the Roll Dice class"""
        roller = DiceRollAction()
        total = [0, 0, 0]
        
        while dice_amount > 0:
            temp = roller.execute(dice_size)
            total[0] += temp[0]
            total[2] += temp[2]
            dice_amount -= 1
        
        return str(total[2])      
         