from .blocks import BLOCK_SIZE, pick_block
from .screenSettings import WIDTH, HEIGHT
from .perlinNoise import *
from pygame import Rect

map_array = []

MAP_AMP = 0.1
MAP_TEMP_AMP = MAP_AMP * 0.5

chunks = {}
CHUNK_SIZE = 1 # blocks per chunk
VISIBLE_CHUNKS_X = WIDTH // (BLOCK_SIZE * CHUNK_SIZE) + 2
VISIBLE_CHUNKS_Y = HEIGHT // (BLOCK_SIZE * CHUNK_SIZE) + 2

for x in range(WIDTH):
    map_array.append([])
    for y in range(HEIGHT):
        height_noise = get_perlin_noise(x, y, MAP_AMP)
        height_noise = expand_noise(height_noise, 100, 0)

        temp_noise = get_perlin_noise(x, y, MAP_TEMP_AMP)
        temp_noise = expand_noise(temp_noise, 100, 0)

        block_chosen = pick_block(height_noise, temp_noise)

        map_array[x].append(block_chosen)

map_tiles_rects = []

for x in range(WIDTH // BLOCK_SIZE):
    for y in range(HEIGHT // BLOCK_SIZE):
        for _ in map_array:
            rect = Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            color = map_array[x][y]['color']
            map_tiles_rects.append([color, rect])

def generate_chunk(chunk_x, chunk_y):
    chunk_rects = []
    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            # Get global position in chunks (in blocks [tiles])
            world_x = chunk_x * CHUNK_SIZE + x
            world_y = chunk_y * CHUNK_SIZE + y

            if world_x >= WIDTH or world_y >= HEIGHT:
                continue

            block = map_array[world_x][world_y]
            rect = Rect(world_x * BLOCK_SIZE, world_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            chunk_rects.append([block['color'], rect])
        return chunk_rects
