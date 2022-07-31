# Pygame шаблон - скелет для нового проекта Pygame
from loguru import logger
import pygame as pg
import random

import config
import colors
from map import Map
import map_pattern


# Создаем игру и окно
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((config.win_WIDTH, config.win_HEIGHT))
pg.display.set_caption("Tower defence")
clock = pg.time.Clock()

MAP = Map.generate_map(map_pattern.pattern_12x12, 12, 12)

# Цикл игры
index = 0
running = True
prev_index = 0

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

    mouse_pos = pg.mouse.get_pos()

    index = Map.calculate_block_index(mouse_pos[1], mouse_pos[0])
    MAP[prev_index].is_selected = False
    MAP[prev_index].update()
    if index < len(MAP):
        MAP[index].is_selected = True
        MAP[index].update()
        prev_index = index

    # заполнение поля
    for block in MAP:
        pg.draw.rect(screen, block.color, (block.pos_x, block.pos_y, block.height-1, block.width-1))

    # переворачиваем экран
    pg.display.flip()


pg.quit()
