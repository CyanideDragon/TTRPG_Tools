import wx
from wx import Window
class StatSheet:
    
    def __getModifier__(self, stat: int) -> str:
        modifier : int = (stat // 2) - 5
        if modifier > 0:
            return f"+{modifier}"
        else:
            return f"{modifier}"

    def __init__(self, parent):
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

    def __create_box__(self, xPos:int, yPos: int, width: int, height: int):
        position = wx.Point(xPos, yPos)
        size = wx.Size(width, height)
        stats = wx.StaticBox(self, wx.ID_ANY, label="", pos=position, size=size)
    
    def display_sheet(self):
        SCREENWIDTH : int = 960
        SCREENHEIGHT : int = 450
        stats = StatSheet
        stats.__create_box__(self, (SCREENWIDTH // 3) * 2, 5,
            (SCREENWIDTH // 3) - 25, SCREENHEIGHT + 10)
        pass

    pass



