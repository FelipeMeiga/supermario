import pygame
from Tile import Tile
from TiledObject import TiledObject
from Player import Player
from AnimatedTiledObject import AnimatedTiledObject
import os

pygame.init()

screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

zoom_factor = 1
tile_size = 32 * zoom_factor
atlas = Tile("./images/tiles.png", 32, 32)
show_hitbox = False

ground_tile = atlas.get_tile(0, 0, zoom_factor)
ground_objs = [TiledObject(screen, ground_tile, (i * tile_size, screen_height - 2*tile_size), show_hitbox=show_hitbox)
               for i in range(int(screen_width / tile_size) + 1)]
ground_objs2 = [TiledObject(screen, ground_tile, (i * tile_size, screen_height - tile_size), show_hitbox=show_hitbox)
               for i in range(int(screen_width / tile_size) + 1)]

player = Player(screen, "./images/player_images", frame_size=(48, 48), animation_speed=10, show_hitbox=show_hitbox)

block_tile = atlas.get_tile(2, 0, zoom_factor)

block_obj4 = TiledObject(screen, block_tile, (200 + 150, 420 - 100), show_hitbox=show_hitbox)
block_obj5 = TiledObject(screen, block_tile, (600, 600-3*tile_size), show_hitbox=show_hitbox)
block_obj7 = TiledObject(screen, block_tile, (600, 600-4*tile_size), show_hitbox=show_hitbox)
block_obj6 = TiledObject(screen, block_tile, (264 + 150, 420 - 100), show_hitbox=show_hitbox)

item_block_tiles = [atlas.get_tile(3, 0, zoom_factor), atlas.get_tile(4, 0, zoom_factor),
                    atlas.get_tile(5, 0, zoom_factor), atlas.get_tile(6, 0, zoom_factor)]

# testando objetos animados
item_block_obj = AnimatedTiledObject(screen, item_block_tiles, (232 + 150, 420 - 100), animation_speed=5, show_hitbox=show_hitbox)

obstacles = ground_objs + [item_block_obj, block_obj4, block_obj5, block_obj6, block_obj7]
animated_objs = [item_block_obj]

pygame.mixer.init()
pygame.mixer.music.load('./sound/overworld.wav')
pygame.mixer.music.play(loops=-1)

def game_status():
    os.system("clear")
    print("Global information:")
    print(f'\t-screen: width {screen_width}, height {screen_height}')
    print(f'\t-zoom_factor: {zoom_factor}')
    print(f'\t-show_hitbox: {"true" if show_hitbox == True else "false"}')
    print("\n", 50*"=")
    print("Player information:")
    print(f'\t-position:  {round(player.pos.x, 1)}X{5 * " "}{round(player.pos.y, 1)}Y')
    print(f'\t-is_jumping: {"true" if player.is_jumping == True else "false"}')
    print(f'\t-velocity: {round(player.vel_x, 1)}X{5 * " "}{round(player.vel_y, 1)}Y')
    print(f'\t-facing_direction: {"right" if player.facing_right == True else "left"}')
    print(f'\t-is_moving: {"true" if player.is_moving == True else "false"}')
    print("\n", 50*"=")
    print("Item block information:")
    print(f'\t-is_animating: {"true" if item_block_obj.animating == True else "false"}')

    
running = True
while running:
    #game_status()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100, 100, 230))

    for obj in obstacles:
        obj.place()
        
    for obj in ground_objs2:
        obj.place()

    player.update(keys, obstacles)

    pygame.display.flip()
    clock.tick(100)

pygame.mixer.music.stop()

os.system("clear")
pygame.quit()
