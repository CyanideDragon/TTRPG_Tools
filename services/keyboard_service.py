import wx

class KeyboardService:
    def __init__(self):
        self.keys = {}

    def is_key_up(self, key):
        wx.EVT_KEY_UP()

    def is_key_down(self, key):
        wx.EVT_KEY_DOWN()

    def is_key_held(self, key):
        pass