import wx
import numpy
from PIL import Image

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color
from casting.menu import Menu
from scripting.dice_roll_action import DiceRollAction

class ActionBar:
    def __init__(self):
        super(wx.Panel, self).__init__()

    def create_bar(self):
        """Creates the action bar border"""
        action_bar = wx.Panel(self, wx.ID_ANY, size=(625,108), pos=(375, 658))
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        longsword = wx.Button(action_bar, label='Longsword', size=(75,50))
        shortsword = wx.Button(action_bar, label='Shortsword', size=(50,50))
        
        # action_bar.Add(main_sizer)
        main_sizer.Add(longsword, 1, wx.Left, 0)
        main_sizer.Add(shortsword, 0, wx.Right, 0)