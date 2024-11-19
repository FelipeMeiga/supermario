import pygame
import os

class Player:
    def __init__(self, screen, image_folder, pos=(100, 100), speed=5, frame_size=(32, 32), animation_speed=10, show_hitbox=False):
        self.screen = screen
        self.image_folder = image_folder
        self.pos = pygame.Vector2(pos)
        self.base_speed = speed
        self.frame_size = frame_size
        self.animation_speed = animation_speed
        self.gravity = 0.43
        self.jump_strength = 12
        self.vel_y = 0
        self.vel_x = 0
        self.max_speed = 4
        self.acceleration = 0.12
        self.is_jumping = False
        self.frames = self.load_frames()
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, frame_size[0]-5, frame_size[1])
        self.animation_counter = 0
        self.is_moving = False
        self.facing_right = True
        self.show_hitbox = show_hitbox

    def load_frames(self):
        frames = []
        for filename in sorted(os.listdir(self.image_folder)):
            if filename.endswith(".png"):
                img = pygame.image.load(os.path.join(self.image_folder, filename)).convert_alpha()
                img = pygame.transform.scale(img, self.frame_size)
                frames.append(img)
        return frames

    def move(self, keys, obstacles):
        self.is_moving = False
        next_pos = self.pos.copy()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = max(self.vel_x - self.acceleration, -self.max_speed)
            self.facing_right = False
            self.is_moving = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = min(self.vel_x + self.acceleration, self.max_speed)
            self.facing_right = True
            self.is_moving = True
        else:
            if self.vel_x > 0:
                self.vel_x = max(self.vel_x - self.acceleration, 0)
            elif self.vel_x < 0:
                self.vel_x = min(self.vel_x + self.acceleration, 0)

        next_pos.x += self.vel_x
        self.hitbox.topleft = (next_pos.x, self.pos.y)
        if not any(obstacle.check_collision(self.hitbox) for obstacle in obstacles):
            self.pos.x = next_pos.x

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vel_y = -self.jump_strength
            self.is_jumping = True

        self.vel_y += self.gravity
        next_pos.y += self.vel_y
        self.hitbox.topleft = (self.pos.x, next_pos.y)

        if not any(obstacle.check_collision(self.hitbox) for obstacle in obstacles):
            self.pos.y = next_pos.y
        else:
            if self.vel_y > 0:
                self.vel_y = 0
                self.is_jumping = False
            elif self.vel_y < 0:
                self.vel_y = 0

        self.rect.topleft = self.pos
        self.hitbox.topleft = self.rect.topleft

    def animate(self):
        if self.is_moving:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.animation_counter = 0
            self.image = self.frames[self.current_frame]
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.frames[0]
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, camera): 
        screen_pos = self.rect.move(-camera.camera.left, -camera.camera.top)
        self.screen.blit(self.image, screen_pos)
        if self.show_hitbox:
            hitbox_screen_pos = self.hitbox.move(-camera.camera.left, -camera.camera.top)
            pygame.draw.rect(self.screen, (0, 255, 0), hitbox_screen_pos, 1)

    def update(self, keys, obstacles, camera):
        self.move(keys, obstacles)
        self.animate()
        self.draw(camera)
        
