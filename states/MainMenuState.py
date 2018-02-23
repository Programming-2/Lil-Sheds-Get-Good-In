import pygame
from states.State import State


class MainMenuState(State):

    def __init__(self, name, mainMenu, handler):
        super().__init__(name)
        self.menuImage = mainMenu
        self.handler = handler

    def update(self, screen):
        # TODO add code to make buttons on screen work
        # Buttons with transition to Control state or Player Selection state

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)

        screen.blit(self.menuImage, [0, 0])

        if (14 < pygame.mouse.get_pos()[0] < 323 and pygame.mouse.get_pressed()[0]) and (590 < pygame.mouse.get_pos()[1] < 740 and pygame.mouse.get_pressed()[0]):
            self.handler.getStateManager().setCurrentState("GameState")

