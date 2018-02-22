import pygame
from State import State


class MainMenuState(State):

    def __init(self, name):
        super().__init__(name)
        self.menuImage = pygame.image.load("media/LilShedTitleScreen.png").convert()

    def tick(self):
        # TODO add code to make buttons on screen work
        # Buttons with transition to Control state or Player Selection state

        if self.isPressingControlButton():
            pass
        elif self.isPressingPlayerSelectionButton():
            pass

    def render(self, screen):
        screen.blit(self.menuImage, [0, 0])

    def isPressingControlButton(self):
        pass

    def isPressingPlayerSelectonButton(self):
        pass
