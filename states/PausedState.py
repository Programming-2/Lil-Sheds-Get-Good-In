import pygame
from states.State import State


class PausedState(State):

    def __init__(self, name, handler, img):
        super().__init__(name)

        self.img = img
        self.handler = handler

    def update(self, screen):
        pressed = False

        screen.blit(self.img, [381, 214])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        if (383 < pygame.mouse.get_pos()[0] < 678 and pressed) and (346 < pygame.mouse.get_pos()[1] < 441 and pressed):
            # Resume
            self.handler.getStateManager().setCurrentState("GameState")

        if (383 < pygame.mouse.get_pos()[0] < 678 and pressed) and (441 < pygame.mouse.get_pos()[1] < 541 and pressed):
            # TODO Make it restart game
            self.handler.getStateManager().setCurrentState("MainMenuState")

        if (383 < pygame.mouse.get_pos()[0] < 678 and pressed) and (541 < pygame.mouse.get_pos()[1] < 641 and pressed):
            # Quit
            self.handler.getStateManager().setCurrentState("MainMenuState")
