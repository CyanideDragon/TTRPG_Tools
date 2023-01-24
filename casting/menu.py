import wx

import constants
from casting.actor import Actor
from shared.point import Point
from shared.color import Color

class Menu(wx.Frame):
    
    def __init__(self):
        super().__init__()
        self.menuBar = wx.MenuBar()
        """create the drop down menus""" 
        self.fileMenu = wx.Menu()

        """Creats a quit function in the file menu"""
        
        self.player_menu()


    def player_menu(self):
        """Creates and adds menu items"""
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()
        self.item = wx.MenuItem(self.fileMenu, 0, '&Check', helpString ="Check Help")
        self.menuBar.Insert(0, self.actionMenu, '&Actions')
        self.menuBar.Insert(1, self.abilitiesMenu, '&Abilities')
        self.menuBar.Insert(1, self.statsMenu, '&Stats')

        self.fileQuit = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileQuit)
        self.fileMenu.Append(self.fileQuit)

        """Adds to the character menu"""
        characters = wx.Menu()
        characters.Append(wx.ID_ANY, 'Larry')
        characters.Append(wx.ID_ANY, 'Curly')
        characters.Append(wx.ID_ANY, 'Moe')
        self.fileMenu.AppendMenu(wx.ID_ANY, '&Characters', characters)

        """Draws the menu Bar"""
        self.SetMenuBar(self.menuBar)
        self.Show(True)
        

    def OnQuit(self, e):
        self.Close(True)