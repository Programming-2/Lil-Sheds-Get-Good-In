import pygame
import Assets
from states.State import State


class MainMenuState(State):

    def __init__(self, name):
        super().__init__(name)
        self.menuImage = Assets.mainMenu

    def update(self, screen):
        # TODO add code to make buttons on screen work
        # Buttons with transition to Control state or Player Selection state

        screen.blit(self.menuImage, [0, 0])
