import pygame
from states.State import State


class MainMenuState(State):

    def __init__(self, name, mainMenu):
        super().__init__(name)
        self.menuImage = mainMenu

    def update(self, screen):
        # TODO add code to make buttons on screen work
        # Buttons with transition to Control state or Player Selection state

        screen.blit(self.menuImage, [0, 0])
