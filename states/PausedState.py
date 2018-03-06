import pygame
from states.State import State


class PausedState(State):

    def __init__(self, name, handler):
        super().__init__(name)

        self.handler = handler

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        if (812 < pygame.mouse.get_pos()[0] < 1080 and pressed) and (26 < pygame.mouse.get_pos()[1] < 190 and pressed):
            # Resume
            self.handler.getStateManager().setCurrentState("GameState")

        if (812 < pygame.mouse.get_pos()[0] < 1080 and pressed) and (26 < pygame.mouse.get_pos()[1] < 190 and pressed):
            # TODO Make it restart game
            self.handler.getStateManager().setCurrentState("MainMenuState")

        if (812 < pygame.mouse.get_pos()[0] < 1080 and pressed) and (26 < pygame.mouse.get_pos()[1] < 190 and pressed):
            # Quit
            self.handler.getStateManager().setCurrentState("MainMenuState")
