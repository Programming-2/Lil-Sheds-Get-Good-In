import pygame
from states.State import State


class ControlState(State):

    def __init__(self, name, handler, testControlScreen):
        super().__init__(name)
        self.handler = handler
        self.testControlScreen = testControlScreen

    def resetState(self):
        pass

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.testControlScreen, [0, 0])

        if (812 < pygame.mouse.get_pos()[0] < 1080 and pressed) and (26 < pygame.mouse.get_pos()[1] < 190 and pressed):
            self.handler.getStateManager().setCurrentState("MainMenuState")
