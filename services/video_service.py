import wx

from casting.menu import Menu
from casting.button import Button

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
        self.button = Button
        self.Menu = Menu

        """Centers the app on the screen"""
        self.Centre()
        self.initial_menu(wx.EVT_BUTTON)

        """Calls the function to make the initial screen"""
        self.choose_screen()

    """Created a file menu that only have the quit option"""
    def initial_menu(self, event):
        self.Menu.initial_menu(self)
        
    """Creates a menu with all of the options for players"""
    def player_menu(self, event):
        self.Menu.player_menu(self)

        # """Calls the button class to draw the dice rolling options"""
        # self.button.diceButtons(self)

    """Creates a menu with all of the options for players"""
    def DM_menu(self, event):
        self.Menu.DM_menu(self)

    """Creates the buttons that """
    def choose_screen(self):
        self.button.choose_screen(self)

    """Closes the app when called"""
    def OnQuit(self, e):
        self.Close(True)