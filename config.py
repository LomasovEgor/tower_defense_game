import colors

# block
bk_WIDTH = 60
bk_HEIGHT = 60
bk_COLOR = colors.GREEN

# map
map_block_WIDTH = 12
map_block_HEIGHT = 12
map_pad_x = 100
map_pad_y = 100

map_WIDTH = map_block_WIDTH * bk_WIDTH + map_pad_x
map_HEIGHT = map_block_HEIGHT * bk_HEIGHT + map_pad_y

map_zeroes = (map_pad_x, map_pad_y)

# window
win_WIDTH = map_WIDTH + 160
win_HEIGHT = map_HEIGHT + 80
FPS = 120

bg_COLOR = colors.WHITE
