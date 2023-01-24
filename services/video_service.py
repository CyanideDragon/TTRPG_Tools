import wx

from casting.menu import Menu

class VideoService(wx.App):
    def __init__(self):
        # makes a frame around the app using the class
        wx.App.__init__(self)
        # self.frame = Frame(None, title='Sudoku')
        # self.frame.Show(True)

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

        # self.call()
        self.Centre()
        self.player_menu()
        # self.menu.player_menu()
        
    # def call(self):
    #     self.Centre()
    #     self.menu = Menu()
    #     self.menu.player_menu()

    def player_menu(self):
        """Creates and adds menu items"""
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.characterMenu = wx.Menu()
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()
        self.item = wx.MenuItem(self.fileMenu, 0, '&Check', helpString ="Check Help")
        self.menuBar.Append(self.fileMenu, '&File')
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

        self.fileQuit = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') 
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileQuit)
        self.fileMenu.Append(self.fileQuit)

        """Draws the menu Bar"""
        self.SetMenuBar(self.menuBar)
        self.Show(True)
        

    def OnQuit(self, e):
        self.Close(True)