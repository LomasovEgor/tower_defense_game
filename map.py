import config
from block import Block, MapBlock, PathBlock, ExitBlock, EnterBlock
from loguru import logger


class Map:

    @staticmethod
    def generate_map(pattern: tuple, rows, columns) -> list[Block]:
        blocks_list = []
        index = 0
        step_x = config.bk_WIDTH
        step_y = config.bk_HEIGHT
        coords = [0, 0]
        for _ in range(rows):
            coords[1] += step_y
            coords[0] = 0
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
    def test_fill() -> list[Block]:
        blocks_list = []
        for y in range(0, config.map_HEIGHT_pixels, config.bk_HEIGHT):
            for x in range(0, config.map_WIDTH_pixels, config.bk_WIDTH):
                block = Block(x, y)
                blocks_list.append(block)
        return blocks_list

    @staticmethod
    def calculate_block_index(x, y) -> int:
        row = x // config.bk_WIDTH
        column = y // config.bk_HEIGHT
        index = row * config.map_WIDTH + column
        return index - 13
