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

    def initial_menu(self):
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.menuBar.Append(self.fileMenu, '&File')
        self.fileQuit = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileQuit)
        self.fileMenu.Append(self.fileQuit)
        
        self.SetMenuBar(self.menuBar)
        self.Show(True)

    def player_menu(self):
        """Hides the screen select buttons"""
        self.player_button.Hide()
        self.DM_button.Hide()

        """Creates and adds menu items"""
        self.characterMenu = wx.Menu()
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()
        self.menuBar.Insert(1, self.actionMenu, '&Actions')
        self.menuBar.Insert(1, self.abilitiesMenu, '&Abilities')
        self.menuBar.Insert(1, self.statsMenu, '&Stats')
        self.menuBar.Insert(1, self.characterMenu, '&Characters')

        """Adds to the character menu"""
        characters = wx.Menu()
        characters.Append(wx.ID_ANY, 'Larry')
        characters.Append(wx.ID_ANY, 'Curly')
        characters.Append(wx.ID_ANY, 'Moe')
        self.characterMenu.AppendMenu(wx.ID_ANY, '&Characters', characters)

        """Draws the menu Bar"""
        self.SetMenuBar(self.menuBar)
        self.Show(True)

        """Calls the button class to draw the dice rolling options"""
        self.button.diceButtons(self)

    def DM_menu(self):
        """Hides the screen select buttons"""
        self.player_button.Hide()
        self.DM_button.Hide()

        """Creates and adds menu items"""
        self.playerMenu = wx.Menu()
        self.NPCMenu = wx.Menu()     
        self.menuBar.Insert(1, self.playerMenu, '&Players')
        self.menuBar.Insert(2, self.NPCMenu, '&NPC\'s')

        """Adds Players and selections to them"""
        player1 = wx.Menu()
        player1.Append(wx.ID_ANY, 'Character Sheet')
        player1.Append(wx.ID_ANY, 'Spells Sheet')
        player1.Append(wx.ID_ANY, 'Background')
        self.playerMenu.AppendMenu(wx.ID_ANY, '&Jesse', player1)

        player2 = wx.Menu()
        player2.Append(wx.ID_ANY, 'Character Sheet')
        player2.Append(wx.ID_ANY, 'Spells Sheet')
        player2.Append(wx.ID_ANY, 'Background')
        self.playerMenu.AppendMenu(wx.ID_ANY, '&Jared', player2)

        player3 = wx.Menu()
        player3.Append(wx.ID_ANY, 'Character Sheet')
        player3.Append(wx.ID_ANY, 'Spells Sheet')
        player3.Append(wx.ID_ANY, 'Background')
        self.playerMenu.AppendMenu(wx.ID_ANY, '&Jensen', player3)

        player4= wx.Menu()
        player4.Append(wx.ID_ANY, 'Character Sheet')
        player4.Append(wx.ID_ANY, 'Spells Sheet')
        player4.Append(wx.ID_ANY, 'Background')
        self.playerMenu.AppendMenu(wx.ID_ANY, '&James', player4)

        """Adds to the NPC's Menu menu"""
        self.NPCMenu.Append(wx.ID_ANY, 'Strahd')

        """Draws the menu Bar"""
        self.SetMenuBar(self.menuBar)
        self.Show(True)