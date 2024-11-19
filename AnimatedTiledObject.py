import pygame
from TiledObject import TiledObject

class AnimatedTiledObject(TiledObject):
    def __init__(self, screen, frames, pos, sound, animation_speed=10, show_hitbox=False):
        first_frame = frames[0].convert_alpha()
        super().__init__(screen, first_frame, pos, show_hitbox)

        self.frames = frames
        self.current_frame = 0
        self.animation_speed = animation_speed
        self.animation_counter = 0
        self.animating = False
        self.active = True

        self.original_y = pos[1]
        self.shake_offset = 0
        self.shaking = False
        self.shake_direction = -1
        self.shake_speed = 2
        self.max_shake_offset = -10

        self.is_playing = False
        self.sound = sound

    def animate(self):
        if self.animating:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.current_frame = len(self.frames) - 1
                    self.animating = False
                self.tile = self.frames[self.current_frame]
                self.animation_counter = 0

        if self.shaking:
            self.shake_offset += self.shake_direction * self.shake_speed
            self.pos = (self.pos[0], self.original_y + self.shake_offset)
            self.hitbox.topleft = self.pos

            if self.shake_offset <= self.max_shake_offset:
                self.shake_direction = 1
            elif self.shake_offset >= 0:
                self.pos = (self.pos[0], self.original_y)
                self.hitbox.topleft = self.pos
                self.shaking = False
                self.shake_offset = 0
                self.shake_direction = -1

    def play_sound(self):
        if self.is_playing:
            self.sound.play()
            self.is_playing = False

    def place(self, camera):
        self.animate()
        self.play_sound()

        screen_pos = pygame.Vector2(self.pos) - pygame.Vector2(camera.camera.topleft)
        self.screen.blit(self.tile, screen_pos)

        if self.show_hitbox:
            hitbox_screen_pos = self.hitbox.move(-camera.camera.left, -camera.camera.top)
            pygame.draw.rect(self.screen, (0, 255, 0), hitbox_screen_pos, 1)

    def check_collision(self, other_rect):
        bottom_hitbox = pygame.Rect(self.hitbox.left, self.hitbox.bottom - 5, self.hitbox.width, 5)
        if self.active and bottom_hitbox.colliderect(other_rect):
            self.animating = True
            self.shaking = True
            self.active = True
            self.is_playing = True
            return True
        return False
