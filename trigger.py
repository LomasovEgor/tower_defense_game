from point import Point
import pygame as pg


class Trigger:
    def __init__(self, point: Point, height: int, width: int):
        self.collision_model = pg.Rect(point.x, point.y, width, height)

    def check_collision(self, rect: pg.Rect) -> bool:
        return self.collision_model.colliderect(rect)
