from abc import ABC

import loguru
import pygame.image

import config
from block import Block
from trigger import Trigger
from enemy import Enemy
import pygame as pg


class Tower(Block):
    def __init__(self, x: int, y: int, attack_radius: int, attack_damage: int, attack_rate: float, image: str):
        super(Tower, self).__init__(x, y)
        self.attack_radius = attack_radius * config.map_block_HEIGHT
        self.attack_damage = attack_damage
        self.attack_rate = attack_rate
        self.trigger = Trigger(self.get_center(), self.attack_radius, self.attack_radius)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def define_targets(self, enemies: list[Enemy]) -> list:
        targets = self.trigger.check_collisions([enemy.collision_model for enemy in enemies])
        loguru.logger.info(targets)
        return targets

    def fire(self, target: Enemy):
        pass

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)

    def build(self):
        pass

    def upgrade(self):
        pass
