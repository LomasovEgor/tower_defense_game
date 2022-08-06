from map import Map
import pygame as pg


class Mouse:
    def __init__(self):
        pass

    @staticmethod
    def get_pos():
        return pg.mouse.get_pos()

    @staticmethod
    def is_on_map() -> bool:
        x, y = pg.mouse.get_pos()
        return Map.is_coords_on_map(x, y)
