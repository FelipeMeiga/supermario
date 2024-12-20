import pygame as pg

from classes.Consts import *
from classes.Text import Text

class MainMenu(object):
    def __init__(self):
        self.mainImage = pg.image.load('images/super_mario_bros.png')

        self.toStartText = Text('Press ENTER to start', 16, (WINDOW_W - WINDOW_W * 0.72, WINDOW_H - WINDOW_H * 0.4))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
