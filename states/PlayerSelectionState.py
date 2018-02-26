import pygame
from states.State import State


class PlayerSelectionState(State):

    def __init__(self, name):
        super().__init__(name)

    def update(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
