from os import environ

import pygame as pg
from pygame.locals import *

from classes.Consts import *
from classes.Map import Map
from classes.MenuManager import MenuManager
from classes.Sound import Sound

class Core(object):
    def __init__(self):
        environ['SDL_VIDEO_CENTERED'] = '1'
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()
        pg.display.set_caption('Mario')
        pg.display.set_mode((WINDOW_W, WINDOW_H))

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.clock = pg.time.Clock()

        self.oWorld = Map('1-1')
        self.oSound = Sound()
        self.oMM = MenuManager(self)

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False
        self.keyReset = False

    def main_loop(self):
        while self.run:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def input(self):
        if self.get_mm().currentGameState == 'Game':
            self.input_player()
        else:
            self.input_menu()

    def input_player(self):
        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RIGHT or e.key == K_d:
                    self.keyR = True
                elif e.key == K_LEFT or e.key == K_a:
                    self.keyL = True
                elif e.key == K_DOWN or e.key == K_s:
                    self.keyD = True
                elif e.key == K_UP or e.key == K_w or e.key == K_SPACE:
                    self.keyU = True
                elif e.key == K_LSHIFT:
                    self.keyShift = True
                elif e.key == K_r:
                    self.keyReset = True
                    self.oWorld.reset(1)

            elif e.type == KEYUP:
                if e.key == K_RIGHT or e.key == K_d:
                    self.keyR = False
                elif e.key == K_LEFT or e.key == K_a:
                    self.keyL = False
                elif e.key == K_DOWN or e.key == K_s:
                    self.keyD = False
                elif e.key == K_UP or e.key == K_w or e.key == K_SPACE:
                    self.keyU = False
                elif e.key == K_LSHIFT:
                    self.keyShift = False
                elif e.key == K_r:
                    self.keyReset = False

    def input_menu(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.get_mm().start_loading()

    def update(self):
        self.get_mm().update(self)

    def render(self):
        self.get_mm().render(self)

    def get_map(self):
        return self.oWorld

    def get_mm(self):
        return self.oMM

    def get_sound(self):
        return self.oSound
