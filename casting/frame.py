# get wxPython
import wx

# a class for the frame
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
        
        self.InitUI()

    def InitUI(self):
        """ Sets the app to fullscreen upon opening """
        self.Centre()
        self.menu()

    def menu(self):
        #create the menu bar
        self.menuBar = wx.MenuBar()

        #create the drop down menus    
        self.fileMenu = wx.Menu()              
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()

        """sets the menu bar to be reaedy to accept the menus"""
        self.item = wx.MenuItem(self.fileMenu, 0, '&Check', helpString ="Check Help") 
        
        # add menus
        self.menuBar.Append(self.fileMenu, '&File')
        self.menuBar.Insert(1, self.actionMenu, '&Actions')
        self.menuBar.Insert(1, self.abilitiesMenu, '&Abilities')
        self.menuBar.Insert(1, self.statsMenu, '&Stats')

        #adds a submenu into a menu selection
        characters = wx.Menu()
        characters.Append(wx.ID_ANY, 'Larry')
        characters.Append(wx.ID_ANY, 'Curly')
        characters.Append(wx.ID_ANY, 'Moe')
        self.fileMenu.AppendMenu(wx.ID_ANY, '&Characters', characters)

        self.fileQuit = wx.MenuItem(self.fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q') # Creats a quit function in the file menu
        self.Bind(wx.EVT_MENU, self.OnQuit, self.fileQuit) # kills the window when the quit button is click under the file menu
        self.fileMenu.Append(self.fileQuit) # adds item to dropdown menu


        # draws the menu bar
        self.SetMenuBar(self.menuBar)           

    # kills window 
    def OnQuit(self, e):
        self.Close()

def main():
    # makes the code run as an app
    app = wx.App()
        
    # makes a frame around the app using the class                      
    frame = Frame(None, title='TTRPG Tools')
    frame.Show(True)

    # keeps the app running and updating the GUI
    app.MainLoop()

main()