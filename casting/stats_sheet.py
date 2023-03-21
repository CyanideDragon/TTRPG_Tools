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
        self.player_name : str = "Player Name"
        # self.parent = parent



    def __create_box__(self, window, xPos:int, yPos: int, width: int, height: int):
        position = wx.Point(xPos, yPos)
        size = wx.Size(width, height)
        stats = wx.StaticBox(window, wx.ID_ANY, label="", pos=position, size=size)
        stats.SetLabelText(f"Player: {self.player_name}")
        hp = wx.StaticBox(stats, wx.ID_ANY, label="HP", pos=(round(width / 30.75), round(height / 48)), size=(round(width / 6.15), round(height / 19.2)))
        temp_hp = wx.StaticBox(stats, wx.ID_ANY, label="Temp HP", pos=(round(width / 4.7), round(height / 48)), size=(round(width / 6.15), round(height / 19.2)))
        armor_C = wx.StaticBox(stats, wx.ID_ANY, label="Armor Class", pos=(round(width / 4.7), round(height / 13.71)), size=(round(width / 6.15), round(height / 19.2)))
        initiative = wx.StaticBox(stats, wx.ID_ANY, label="Initiative", pos=(round(width / 30.75), round(height / 13.71)), size=(round(width / 6.15), round(height / 19.2)))
        speed = wx.StaticBox(stats, wx.ID_ANY, label="speed", pos=(round(width / 2.5625), round(height / 13.71)), size=(round(width / 6.5), round(height / 19.2)))
        strength = wx.StaticBox(stats, wx.ID_ANY, label="Strength", pos=(round(width / 30.75), round(height / (height / 220))), size=(round(width / 6.15), round(height / 19.2)))
        dexterity = wx.StaticBox(stats, wx.ID_ANY, label="Dexterity", pos=(round(width / 30.75), round(height / (height/270))), size=(round(width / 6.15), round(height / 19.2)))
        constitution = wx.StaticBox(stats, wx.ID_ANY, label="Constitution", pos=(round(width / 30.75), round(height / (height/320))), size=(round(width / 6.15), round(height / 19.2)))
        intelligence = wx.StaticBox(stats, wx.ID_ANY, label="Intelligence", pos=(round(width / 30.75), round(height / (height/ 370))), size=(round(width / 6.15), round(height / 19.2)))
        wisdom = wx.StaticBox(stats, wx.ID_ANY, label="Wisdom", pos=(round(width / 30.75), round(height / (height / 420))), size=(round(width / 6.15), round(height / 19.2)))
        charisma = wx.StaticBox(stats, wx.ID_ANY, label="Charisma", pos=(round(width / 30.75), round(height / (height / 470))), size=(round(width / 6.15), round(height / 19.2)))
        inventory = wx.StaticBox(stats, wx.ID_ANY, label="Inventory", pos=(0, round(height / (height / 550))), size=(round(width), round(height - (height / (height / 550)))))
        wx.StaticText(hp, label=f"{self.hp}", pos=(15, 15))
        wx.StaticText(temp_hp, label=f"{self.temp_hp}", pos=(15, 15))
        wx.StaticText(armor_C, label=f"{self.armor_class}", pos=(15, 15))
        wx.StaticText(initiative, label=f"{self.init}", pos=(15, 15))
        wx.StaticText(speed, label=f"{self.speed}", pos=(15, 15))
        wx.StaticText(strength, label=f"{self.str}", pos=(15, 15))
        wx.StaticText(dexterity, label=f"{self.dex}", pos=(15, 15))
        wx.StaticText(constitution, label=f"{self.con}", pos=(15, 15))
        wx.StaticText(intelligence, label=f"{self.int}", pos=(15, 15))
        wx.StaticText(wisdom, label=f"{self.wis}", pos=(15, 15))
        wx.StaticText(charisma, label=f"{self.cha}", pos=(15, 15))
        

        
        
        
    
    def display_sheet(self, window):
        
        SCREENWIDTH : int = wx.DisplaySize()[0]
        SCREENHEIGHT : int = wx.DisplaySize()[1]
        stats = StatSheet()
        stats.__create_box__(window=window, xPos=(SCREENWIDTH // 3) * 2, yPos=10,
            width=round((SCREENWIDTH // 3) - (SCREENWIDTH / 76.8)), height=round(SCREENHEIGHT - (SCREENHEIGHT / 9)))
        

    



