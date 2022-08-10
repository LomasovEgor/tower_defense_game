import config as cfg
from abc import ABC
from point import Point
import pygame as pg


class Block(ABC):
    def __init__(self, x: int, y: int):
        self.width = cfg.bk_WIDTH
        self.height = cfg.bk_HEIGHT
        self.pos = Point(x, y)
        self.is_selected = False

    def get_center(self) -> Point:
        center_x = self.pos.x + self.width // 2
        center_y = self.pos.y + self.height // 2
        return Point(center_x, center_y)

    def update(self):
        pass

    def draw(self, screen: pg.Surface):
        pass
