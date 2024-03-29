from shared.color import Color
from shared.point import Point

class Actor:

#Most of this stuff was just copied over from another project, please make adjustments as needed.

    def __init__(self):
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

    def get_font_type(self):
        return self._font_type

    def get_font_weight(self):
        return self._font_weight
    
    def get_image(self):
        return self._image

    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_text(self, text):
        self._text = text

    def set_font_type(self, font_type):
        self._font_type = font_type

    def set_font_weight(self, font_weight):
        self._font_weight = font_weight

    def set_image(self, image):
        self._image = image