import wx

from casting.menu import Menu
from casting.button import Button
from casting.stats_sheet import StatSheet
from scripting.dice_roll_action import DiceRollAction

"""Initiates the App"""
class VideoService(wx.App):
    def __init__(self):
        wx.App.__init__(self)

class Frame(wx.Frame):
    def __init__(self, parent, title):
        """accesses the parent, in this case none as it is the frame; 
        sets the title to the one passed it
        sets the size in pixels (width, heigth); 
        draws the maximize box; draws the minimize box; 
        gives the ability for the user to resize the window; 
        gives a simple system menu;
        gives the space for the above window functions; 
        draws the close window box"""
        super(Frame, self).__init__(parent,  
        title=title,                         
        size=(960, 540),                     
        style=wx.MAXIMIZE_BOX | 
        wx.MINIMIZE_BOX | 
        wx.RESIZE_BORDER | 
        wx.SYSTEM_MENU | 
        wx.CAPTION | 
        wx.CLOSE_BOX)

        """Creates the button and menu classes"""
        
        self.Menu = Menu

        """Centers the app on the screen"""
        self.Centre()
        self.initial_menu()

        """Calls the function to make the initial screen"""
        self.choose_screen()

    """Created a file menu that only have the quit option"""
    def initial_menu(self):
        self.Menu.initial_menu(self)
        
    """Creates a menu with all of the options for players"""
    def player_menu(self, event):
        self.Menu.player_menu(self)
        button = Button
        button.diceButtons(self)
        stat_sheet = StatSheet()
        stat_sheet.display_sheet(self)
      
    """Creates a menu with all of the options for players"""
    def DM_menu(self, event):
        self.Menu.DM_menu(self)

    """Creates the buttons that """
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

    """Closes the app when called"""
    def OnQuit(self, e):
        self.Close(True)