import pygame

from states.State import State
from utils.Colors import colors


class Tetris(State):
    def __init__(self, name, handler):
        super().__init__(name)
        self.handler = handler

    def resetState(self):
        pass

    def update(self, screen):
        screen.fill(colors.get("BLACK"))
