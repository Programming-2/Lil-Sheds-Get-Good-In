import pygame
from states.State import State


class ControlState(State):

    def __init__(self, name, handler):
        super().__init__(name)
        self.handler = handler

    def update(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
