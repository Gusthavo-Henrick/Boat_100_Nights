# TODO:
# Create 2 perlin noises
    # First we need the map generation, next the temperature of the map

from perlinNoise import *
from blocks import *

import pygame as pg

WIDTH = 300
HEIGHT = 300

BLACK: tuple[int, int, int] = (0, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Map generation - Perlin noise', "a")

clock = pg.time.Clock()

map_array = []

MAP_AMP = 0.05

for x in range(WIDTH):
    map_array.append([])
    for y in range(HEIGHT):
        layer_perlin_noise = get_perlin_noise(x, y, MAP_AMP)
        layer_perlin_noise = expand_noise(layer_perlin_noise, 100, 0)

        block_chosen = pick_block(layer_perlin_noise)
        
        map_array[x].append(block_chosen)

map_tiles_rects = []

for x in range(WIDTH // BLOCK_SIZE):
    for y in range(HEIGHT // BLOCK_SIZE):
        for _ in map_array:
            rect = pg.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            color = map_array[x][y]['color']
            map_tiles_rects.append([color, rect])

def draw_map():
    screen.fill(BLACK)

    for rect in map_tiles_rects:
        pg.draw.rect(screen, rect[0], rect[1])

    pg.display.flip()

running = True
draw_map()
while running:
    clock.tick(30)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False

        elif ev.type == pg.KEYDOWN:
            draw_map()

pg.quit()