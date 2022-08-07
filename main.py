# Pygame шаблон - скелет для нового проекта Pygame
from loguru import logger
import pygame as pg
import random
from mouse import Mouse

import config
import colors
from map import Map
import map_pattern
from enemy import Enemy
from point import Point
from move_queue import MoveQueue


# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((config.win_WIDTH, config.win_HEIGHT))
pg.display.set_caption("Tower defence")
clock = pg.time.Clock()

MAP = Map.generate_map(map_pattern.pattern_12x12, 12, 12)

index = 0
running = True
prev_index = 0

test_enemy = Enemy(Point(100, 100), (255, 0, 0), 20, 20)
test_enemy1 = Enemy(Point(150, 150), (230, 20, 20), 20, 20)
test_enemy_path = MoveQueue()
test_enemy_path.append_point(100, 100)
test_enemy_path.append_point(400, 400)
test_enemy_path.append_point(800, 400)
test_enemy_path.append_point(100, 100)
test_enemy.move_points = test_enemy_path
test_enemy1.move_points = test_enemy_path
test_enemy.speed.set_coords(1, 1)
test_enemy1.speed.set_coords(2, 2)

while running:
    # Держим цикл на правильной скорости
    clock.tick(config.FPS)
    # Ввод процесса (события)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    # Обновление
    screen.fill(colors.Lavender)

    mouse_pos = Mouse.get_pos()
    index = Map.calculate_block_index(mouse_pos[0], mouse_pos[1])

    MAP[prev_index].is_selected = False
    MAP[prev_index].update()

    if index < len(MAP):
        MAP[index].is_selected = True
        MAP[index].update()
        prev_index = index

    # заполнение поля
    for block in MAP:
        block.draw(screen)

    test_enemy.move()
    test_enemy.draw(screen)
    test_enemy1.move()
    test_enemy1.draw(screen)

    # переворачиваем экран
    pg.display.flip()


pg.quit()
