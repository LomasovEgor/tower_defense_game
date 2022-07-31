import random
import colors
import config as cfg
from abc import ABC


class Block(ABC):
    def __init__(self, x: int, y: int):
        self.width = cfg.bk_WIDTH
        self.height = cfg.bk_HEIGHT
        self.pos_x = x
        self.pos_y = y
        self.is_selected = False
        self.color = None
        self.selected_color = None
        self.unselected_color = None

    def update(self):
        if self.is_selected:
            self.color = self.selected_color
        else:
            self.color = self.unselected_color


class MapBlock(Block):
    def __init__(self, x, y):
        super(MapBlock, self).__init__(x, y)
        self.color = colors.CornflowerBlue
        self.selected_color = colors.SelectedCornflowerBlue
        self.unselected_color = colors.CornflowerBlue


class PathBlock(Block):
    def __init__(self, x, y):
        super(PathBlock, self).__init__(x, y)
        self.color = colors.Azure
        self.selected_color = colors.SelectedAzure
        self.unselected_color = colors.Azure


class EnterBlock(Block):
    def __init__(self, x, y):
        super(EnterBlock, self).__init__(x, y)
        self.color = colors.GREEN
        self.selected_color = colors.SelectedGreen
        self.unselected_color = colors.GREEN


class ExitBlock(Block):
    def __init__(self, x, y):
        super(ExitBlock, self).__init__(x, y)
        self.color = colors.RED
        self.selected_color = colors.SelectedRed
        self.unselected_color = colors.RED
