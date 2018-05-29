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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.handler.getStateManager().setCurrentState("MinigameMenu")
        screen.fill(colors.get("BLACK"))
