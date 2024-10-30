import pygame
from TiledObject import TiledObject

class AnimatedTiledObject(TiledObject):
    def __init__(self, screen, frames, pos, animation_speed=5, show_hitbox=False):
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
        self.max_shake_offset = -20

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

    def place(self):
        self.animate()
        super().place()

    def check_collision(self, other_rect):
        if self.active and super().check_collision(other_rect):
            self.animating = True
            self.shaking = True
            self.active = True
            return True
        return False
