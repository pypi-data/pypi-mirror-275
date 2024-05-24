import os

class Screen:
    def __init__(self):
        self.width, self.height = self.get_terminal_size()

    def get_terminal_size(self):
        size = os.get_terminal_size()
        return size.columns, size.lines

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCenter(self):
        center_x = self.width // 2
        center_y = self.height // 2
        return center_x, center_y