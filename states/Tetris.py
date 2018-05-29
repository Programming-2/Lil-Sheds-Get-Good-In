import pygame

from states.State import State
from utils.Colors import colors


class Tetris(State):
    def __init__(self, name, handler):
        super().__init__(name)
        self.handler = handler

        self.rows = 22
        self.cols = 10

        self.pieces = [
            [[1, 1, 1],
             [0, 1, 0]],

            [[0, 2, 2],
             [2, 2, 0]],

            [[3, 3, 0],
             [0, 3, 3]],

            [[4, 0, 0],
             [4, 4, 4]],

            [[0, 0, 5],
             [5, 5, 5]],

            [[6, 6, 6, 6]],

            [[7, 7],
             [7, 7]]
        ]

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
