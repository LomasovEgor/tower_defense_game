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
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# MAP = Map.generate_map(map_pattern.pattern_10x10, 10, 10)
MAP = Map.generate_map(map_pattern.pattern_12x12, 12, 12)

# Цикл игры
index = 0
running = True

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
    MAP[index].is_selected = False
    MAP[index].update()

    index = Map.calculate_block_index(mouse_pos[1], mouse_pos[0])
    MAP[index].is_selected = True
    MAP[index].update()

    for block in MAP:
        pg.draw.rect(screen, block.color, (block.pos_x, block.pos_y, block.height-1, block.width-1))
    pg.display.flip()
    # Рендеринг
    # screen.fill(colors.BLACK)
    # После отрисовки всего, переворачиваем экран


pg.quit()
