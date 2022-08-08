# Pygame шаблон - скелет для нового проекта Pygame
from loguru import logger
import pygame as pg
import random
import copy
from mouse import Mouse

import config
import colors
from map import Map
import map_pattern
from enemy import Enemy
from point import Point
from move_queue import MoveQueue
from menu import Menu


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

test_enemy = Enemy(Point(246, 734), (255, 0, 0), 20, 20)
test_enemy1 = Enemy(Point(246, 734), (230, 20, 20), 20, 20)
test_enemy_path = MoveQueue()
test_enemy_path.append_point(246, 734)
test_enemy_path.append_point(248, 252)
test_enemy_path.append_point(369, 251)
test_enemy_path.append_point(369, 553)
test_enemy_path.append_point(488, 552)
test_enemy_path.append_point(487, 249)
test_enemy_path.append_point(728, 248)
test_enemy_path.append_point(728, 670)
test_enemy.move_points = test_enemy_path
test_enemy1.move_points = copy.deepcopy(test_enemy_path)
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
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                logger.info(f'test_enemy_path.append_point{Mouse.get_pos()}')

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

    if pg.mouse.get_pressed()[0] and Mouse.is_on_map():
        menu = Menu(100, 100, colors.GREEN)
        mouse_pos = Mouse.get_pos()
        menu.draw(screen, Point(mouse_pos[0], mouse_pos[1]))

    # переворачиваем экран
    pg.display.flip()


pg.quit()
