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
