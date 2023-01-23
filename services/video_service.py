import wx

from casting.menu import Menu

class VideoService(wx.App):
    def __init__(self):
        # makes a frame around the app using the class
        wx.App.__init__(self)
        self.frame = Frame(None, title='Sudoku')

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
        
        self.Centre()
        Menu()