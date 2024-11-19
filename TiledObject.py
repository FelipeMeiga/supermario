import pygame

class TiledObject:
    def __init__(self, screen, tile, pos, show_hitbox=False):
        self.screen = screen
        self.tile = tile
        self.pos = pygame.Vector2(pos)
        self.hitbox = self.tile.get_rect(topleft=self.pos)
        self.show_hitbox = show_hitbox

    def place(self, camera):
        screen_pos = self.pos - pygame.Vector2(camera.camera.topleft)
        self.screen.blit(self.tile, screen_pos)
        if self.show_hitbox:
            hitbox_screen_pos = self.hitbox.move(-camera.camera.left, -camera.camera.top)
            pygame.draw.rect(self.screen, (0, 255, 0), hitbox_screen_pos, 1)

    def check_collision(self, other_rect):
        return self.hitbox.colliderect(other_rect)
