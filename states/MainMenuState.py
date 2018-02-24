import pygame
from states.State import State


class MainMenuState(State):

    def __init__(self, name, mainMenu, handler):
        super().__init__(name)
        self.menuImage = mainMenu
        self.handler = handler

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.menuImage, [0, 0])

        if (14 < pygame.mouse.get_pos()[0] < 323 and pressed) and (590 < pygame.mouse.get_pos()[1] < 740 and pressed):
            self.handler.getStateManager().setCurrentState("GameState")

        if (715 < pygame.mouse.get_pos()[0] < 1024 and pressed) and (591 < pygame.mouse.get_pos()[1] < 725 and pressed):
            self.handler.getStateManager().setCurrentState("ControlState")
