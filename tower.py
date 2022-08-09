from abc import ABC
import config
from block import Block


class Tower(Block):
    def __init__(self, x: int, y: int, attack_radius: int, attack_damage: int, attack_rate: float):
        super(Tower, self).__init__(x, y)
        self.attack_radius = attack_radius * (config.bk_HEIGHT + config.map_block_WIDTH) / 2
        self.attack_damage = attack_damage
        self.attack_rate = attack_rate

    def fire(self):
        pass

    def build(self):
        pass

    def upgrade(self):
        pass
