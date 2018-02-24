import pygame
from states.State import State


class ControlState(State):

    def __init__(self, name, handler, testControlScreen):
        super().__init__(name)
        self.handler = handler
        self.testControlScreen = testControlScreen

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.testControlScreen, [0, 0])

        if (715 < pygame.mouse.get_pos()[0] < 1024 and pressed) and (591 < pygame.mouse.get_pos()[1] < 725 and pressed):
            self.handler.getStateManager().setCurrentState("MainMenuState")
