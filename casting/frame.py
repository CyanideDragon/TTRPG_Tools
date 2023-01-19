# get wxPython
import wx

# a class for the frame
class Frame(wx.Frame):
    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, # accesses the parent, in this case none as it is the frame
        title=title,                        # sets the title to the one passed it
        size=(960, 540),                    # sets the size in pixels (width, heigth)
        style=wx.MAXIMIZE_BOX |             # draws the maximize box
        wx.MINIMIZE_BOX |                   # draws the minimize box
        wx.RESIZE_BORDER |                  # gives the ability for the user to resize the window
        wx.SYSTEM_MENU |                    # gives a simple system menu
        wx.CAPTION |	                    # gives the space for the above window functions
        wx.CLOSE_BOX)                       # draws the close window box
        
        self.InitUI()

    def InitUI(self):
        self.Centre()                       # Sets the app to fullscreen upon opening
        self.menu()

    def menu(self):
        #create the menu bar
        self.menuBar = wx.MenuBar()

        #create the drop down menus    
        self.fileMenu = wx.Menu()              
        self.actionMenu = wx.Menu()     
        self.abilitiesMenu = wx.Menu()
        self.statsMenu = wx.Menu()

        #sets the menu bar to be reaedy to accept the menus
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