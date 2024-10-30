import pygame

class TiledObject:
    def __init__(self, screen, tile, pos, show_hitbox=False):
        self.screen = screen
        self.tile = tile
        self.pos = pos
        self.hitbox = self.tile.get_rect(topleft=self.pos)
        self.show_hitbox = show_hitbox

    def place(self):
        self.screen.blit(self.tile, self.pos)
        if self.show_hitbox:
            pygame.draw.rect(self.screen, (0, 255, 0), self.hitbox, 1)

    def check_collision(self, other_rect):
        return self.hitbox.colliderect(other_rect)
