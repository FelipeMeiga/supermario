import pygame

class Camera:
    def __init__(self, width, height, screen_width, screen_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self, entity):
        return entity.hitbox.move(-self.camera.left, -self.camera.top)

    def update(self, target):
        x = target.rect.centerx - int(self.screen_width / 2)
        y = target.rect.centery - int(self.screen_height / 2)

        x = max(0, min(x, self.width - self.screen_width))
        y = max(0, min(y, self.height - self.screen_height))

        self.camera = pygame.Rect(x, y, self.width, self.height)
