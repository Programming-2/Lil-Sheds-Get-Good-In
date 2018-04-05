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

        if (0 < pygame.mouse.get_pos()[0] < 565 and pressed) and (745 < pygame.mouse.get_pos()[1] < 800 and pressed):
            self.handler.getStateManager().setCurrentState("MainMenuState")
        # if (565 < pygame.mouse.get_pos()[0] < 1100 and pressed) and (745 < pygame.mouse.get_pos[1] < 800 and pressed):
            # Controller Screen needs to go here
