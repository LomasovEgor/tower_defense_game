import random
import colors
import config as cfg
from abc import ABC


class Block(ABC):
    def __init__(self, x: int, y: int):
        self.width = cfg.bk_WIDTH
        self.height = cfg.bk_HEIGHT
        self.color = None
        self.pos_x = x
        self.pos_y = y
        self.is_selected = False
        self.selected_color = None

    def update(self):
        if self.is_selected:
            self.color = colors.SelectedCornflowerBlue
        else:
            self.color = colors.CornflowerBlue


class MapBlock(Block):
    def __init__(self, x, y):
        super(MapBlock, self).__init__(x, y)
        self.color = colors.CornflowerBlue
        self.color = colors.CornflowerBlue
        self.selected_color = colors.SelectedCornflowerBlue


class PathBlock(Block):
    def __init__(self, x, y):
        super(PathBlock, self).__init__(x, y)
        self.color = colors.Azure


class EnterBlock(Block):
    def __init__(self, x, y):
        super(EnterBlock, self).__init__(x, y)
        self.color = colors.GREEN


class ExitBlock(Block):
    def __init__(self, x, y):
        super(ExitBlock, self).__init__(x, y)
        self.color = colors.RED
