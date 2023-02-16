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
        """Creates the action bar with nothing in it"""
        action_bar = wx.StaticBox(self, wx.ID_ANY, size=(625,108), pos=(375, 658))

    