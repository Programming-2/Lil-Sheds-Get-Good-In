import pygame
from states.State import State


class ControlState(State):

    def __init__(self, name, handler, testControlScreen):
        super().__init__(name)
        self.handler = handler
        self.testControlScreen = testControlScreen

    def update(self, screen):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)

        screen.blit(self.testControlScreen, [0, 0])

        # TODO add code to go back to main menu
