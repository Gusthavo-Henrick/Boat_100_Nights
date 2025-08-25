from .blocks import *
import pygame as pg
from .mapGeneration import *
from .chars import *
from .screenSettings import *

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Map generation - Perlin noise')

clock = pg.time.Clock()

def draw_visible_chunks(offset_x_px, offset_y_px):
    screen.fill(BLACK)
    CHUNK_PX = BLOCK_SIZE * CHUNK_SIZE
    start_chunk_x = offset_x_px // CHUNK_PX
    start_chunk_y = offset_y_px // CHUNK_PX

    for cx in range(start_chunk_x, start_chunk_x + VISIBLE_CHUNKS_X):
        for cy in range(start_chunk_y, start_chunk_y + VISIBLE_CHUNKS_Y):
            if (cx, cy) not in chunks:
                chunks[(cx, cy)] = generate_chunk(cx, cy)

            for color, world_rect in chunks[(cx, cy)]:
                view_rect = world_rect.move(-offset_x_px, -offset_y_px)

                if view_rect.right < 0 or view_rect.bottom < 0 or view_rect.left > WIDTH or view_rect.top > HEIGHT:
                    continue

                pg.draw.rect(screen, color, view_rect)


    pg.display.flip()

running = True
player = Player("Gustha")
while running:
    clock.tick(30)

    if pg.key.get_pressed() == pg.K_w:
        if player.y > 0:
            player.move(y=-1)
    if pg.key.get_pressed() == pg.K_s:
        if player.y < HEIGHT:
            player.move(y=1)

    if pg.key.get_pressed() == pg.K_a:
        if player.x > 0:
            player.move(x=-1)
    if pg.key.get_pressed() == pg.K_d:
        if player.x < WIDTH:
            player.move(x=1)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False

    draw_visible_chunks(player.x, player.y)

pg.quit()
