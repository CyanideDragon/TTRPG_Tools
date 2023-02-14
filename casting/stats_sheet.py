import wx
class StatSheet():

    
    
    def __getModifier__(self, stat: int) -> str:
        modifier : int = (stat // 2) - 5
        if modifier > 0:
            return f"+{modifier}"
        else:
            return f"{modifier}"

    def __init__(self):
        self.hp : int = 0
        self.temp_hp : int = 0
        self.armor_class : int = 0
        self.init : int = 0
        self.speed : int = 0
        self.str : int = 0
        self.dex : int = 0
        self.con : int = 0
        self.int : int = 0
        self.wis : int = 0
        self.cha : int = 0
        # self.parent = parent

    def __create_box__(window, xPos:int, yPos: int, width: int, height: int):
        position = wx.Point(xPos, yPos)
        size = wx.Size(width, height)
        stats = wx.StaticBox(window, wx.ID_ANY, label="", pos=position, size=size)
        
    
    def display_sheet(self, window):
        
        SCREENWIDTH : int = wx.DisplaySize()[0]
        SCREENHEIGHT : int = wx.DisplaySize()[1]
        stats = StatSheet
        stats.__create_box__(window=window, xPos=(SCREENWIDTH // 3) * 2, yPos=10,
            width=(SCREENWIDTH // 3) - 25, height=SCREENHEIGHT - 120)
        

    



