import pygame as pg
from abc import ABC
import colors
from block import Block


class ColoredBlock(Block, ABC):
    def __init__(self, x, y):
        super(ColoredBlock, self).__init__(x, y)
        self.color = None
        self.selected_color = None
        self.unselected_color = None

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.height - 1, self.width - 1))

    def update(self):
        if self.is_selected:
            self.color = self.selected_color
        else:
            self.color = self.unselected_color


class MapBlock(ColoredBlock):
    def __init__(self, x, y):
        super(MapBlock, self).__init__(x, y)
        self.color = colors.CornflowerBlue
        self.selected_color = colors.SelectedCornflowerBlue
        self.unselected_color = colors.CornflowerBlue


class PathBlock(ColoredBlock):
    def __init__(self, x, y):
        super(PathBlock, self).__init__(x, y)
        self.color = colors.Azure
        self.selected_color = colors.SelectedAzure
        self.unselected_color = colors.Azure


class EnterBlock(ColoredBlock):
    def __init__(self, x, y):
        super(EnterBlock, self).__init__(x, y)
        self.color = colors.GREEN
        self.selected_color = colors.SelectedGreen
        self.unselected_color = colors.GREEN


class ExitBlock(ColoredBlock):
    def __init__(self, x, y):
        super(ExitBlock, self).__init__(x, y)
        self.color = colors.RED
        self.selected_color = colors.SelectedRed
        self.unselected_color = colors.RED
