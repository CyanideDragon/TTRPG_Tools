import wx

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color

class Menu(wx.Frame):
    def __init__(self):
        self.menuBar = wx.MenuBar()
        """create the drop down menus""" 
        self.fileMenu = wx.Menu()

        """Creats a quit function in the file menu"""
        self.fileQuit = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileQuit)
        self.fileMenu.Append(self.fileQuit)
        self.player_menu(self)


    def player_menu(self):
        """Creates and adds menu items"""
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()
        self.item = wx.MenuItem(self.fileMenu, 0, '&Check', helpString ="Check Help")
        self.menuBar.Insert(1, self.actionMenu, '&Actions')
        self.menuBar.Insert(1, self.abilitiesMenu, '&Abilities')
        self.menuBar.Insert(1, self.statsMenu, '&Stats')

        """Adds to the character menu"""
        characters = wx.Menu()
        characters.Append(wx.ID_ANY, 'Larry')
        characters.Append(wx.ID_ANY, 'Curly')
        characters.Append(wx.ID_ANY, 'Moe')
        self.fileMenu.AppendMenu(wx.ID_ANY, '&Characters', characters)

        """Draws the nemu Bar"""
        self.SetMenuBar(self.menuBar)

    def OnQuit(self, e):
        self.Close()