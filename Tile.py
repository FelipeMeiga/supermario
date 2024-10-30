import pygame

class Tile:
    def __init__(self, tileset_image, tile_width, tile_height):
        self.tileset_image = pygame.image.load(tileset_image).convert_alpha()
        self.tile_width = tile_width
        self.tile_height = tile_height

    def get_tile(self, x, y, zoom_factor=1):
        tile_rect = pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)
        tile_image = self.tileset_image.subsurface(tile_rect)

        scaled_tile = pygame.transform.scale(
            tile_image,
            (self.tile_width * zoom_factor, self.tile_height * zoom_factor)
        )
        return scaled_tile
