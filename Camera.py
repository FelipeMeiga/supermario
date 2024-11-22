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
        target_x = target.rect.centerx - int(self.screen_width / 2)
        target_y = target.rect.centery - int(self.screen_height / 2)
        
        distance_x = target_x - self.camera.x
        distance_y = target_y - self.camera.y

        acceleration = 0.1

        self.camera.x += int(distance_x * acceleration)
        self.camera.y += int(distance_y * acceleration)

        self.camera.x = max(0, min(self.camera.x, self.width - self.screen_width))
        self.camera.y = max(0, min(self.camera.y, self.height - self.screen_height))

