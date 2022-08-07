import config
from block import Block, MapBlock, PathBlock, ExitBlock, EnterBlock
from loguru import logger


class Map:
    def __init__(self):
        self.blocks_list
        self.min_coords
        self.max_coords
        pass

    @staticmethod
    def generate_map(pattern: tuple, rows, columns) -> list[Block]:
        blocks_list = []
        index = 0
        step_x = config.bk_WIDTH
        step_y = config.bk_HEIGHT
        coords = [0, -step_y + config.map_pad_y]
        for _ in range(rows):
            coords[1] += step_y
            coords[0] = -step_x + config.map_pad_x
            for _ in range(columns):
                coords[0] += step_x
                if pattern[index] == 0:
                    block = MapBlock(*coords)
                elif pattern[index] == 1:
                    block = PathBlock(*coords)
                elif pattern[index] == 8:
                    block = EnterBlock(*coords)
                elif pattern[index] == 9:
                    block = ExitBlock(*coords)
                else:
                    block = MapBlock(*coords)
                index += 1
                blocks_list.append(block)
        return blocks_list

    @staticmethod
    def calculate_block_index(x, y) -> int:
        if Map.is_coords_on_map(x, y):
            x -= config.map_pad_x
            y -= config.map_pad_y
            row = x // config.bk_WIDTH
            column = y // config.bk_HEIGHT
            index = column * config.map_block_WIDTH + row
            return index
        else:
            return config.map_block_HEIGHT * config.map_block_WIDTH

    @staticmethod
    def is_coords_on_map(x, y) -> bool:
        min_coords = (config.map_pad_x, config.map_pad_y)
        max_coords = (config.map_WIDTH, config.map_HEIGHT)
        if min_coords[0] < x < max_coords[0] and min_coords[1] < y < max_coords[1]:
            return True
        else:
            return False

