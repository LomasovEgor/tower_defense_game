import pygame as pg
from point import Point
from abc import ABC


class Menu(ABC):
    def __init__(self, width: int, height: int, color: tuple[int, int, int]):
        self.surface = pg.Surface((width, height))
        self.color = color

    def draw(self, surface: pg.Surface, position: Point):
        self.surface.fill(self.color)
        surface.blit(self.surface, (position.x, position.y))


class TurretMenu(Menu):
    def __init__(self, width: int, height: int, color: tuple[int, int, int]):
        super(TurretMenu, self).__init__(width, height, color)
        self.turrets = []

    def _generate_menu(self):
        pass

    def draw(self, surface: pg.Surface, position: Point):
        super(TurretMenu, self).draw(surface, position)
        self._generate_menu()
