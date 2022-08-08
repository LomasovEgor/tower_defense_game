import pygame as pg
from point import Point
from move_queue import MoveQueue


class Enemy:
    def __init__(self, spawn_pont: Point, color: tuple[int, int, int], height: int, width: int):
        self.pos = spawn_pont
        self.color = color
        self.height = height
        self.width = width
        self.speed = Point(0, 0)
        self.move_points = MoveQueue()

    def set_move_points(self, move_points: MoveQueue):
        self.move_points = move_points

    def move(self):
        destination = self.move_points.get_first()
        if destination is not None:
            if abs(destination.x - self.pos.x) <= self.speed.x and abs(self.pos.y - destination.y) <= self.speed.y:
                self.pos.x, self.pos.y = destination.x, destination.y
                self.move_points.delete_first()
            if abs(destination.x - self.pos.x) > self.speed.x:
                if self.pos.x < destination.x:
                    self.pos.x += self.speed.x
                elif self.pos.x > destination.x:
                    self.pos.x -= self.speed.x
            if abs(self.pos.y - destination.y) > self.speed.y:
                if self.pos.y < destination.y:
                    self.pos.y += self.speed.y
                elif self.pos.y > destination.y:
                    self.pos.y -= self.speed.y

    def death(self):
        pass

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.height, self.width))

    def spawn(self, screen: pg.Surface):
        self.draw(screen)

    def on_death(self):
        pass
