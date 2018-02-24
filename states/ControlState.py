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

        # TODO latch control so states doesnt flip back and forth

        if (7 < pygame.mouse.get_pos()[0] < 1024 and pygame.mouse.get_pressed()[0]) and (591 < pygame.mouse.get_pos()[1] < 725 and pygame.mouse.get_pressed()[0]):
            self.handler.getStateManager().setCurrentState("MainMenuState")
