import pygame
from states.State import State
from utils.Handler import Handler
from utils.Colors import colors
from utils.StateManager import StateManager

class EndGameState(State):

    def __init__(self, name, handler):
        super().__init__(name)
        self.img = pygame.image.load("media/Screens/EndScreen.png")
        self.one = pygame.image.load("media/Screens/oneSprite.png").convert_alpha()
        self.two = pygame.image.load("media/Screens/twoSprite.png").convert_alpha()
        self.handler = handler

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
        screen.blit(self.img, [0, 0])

        self.winner = self.handler.getStateManager().getState("GameState").victor
        if self.winner == 1:
            screen.blit(self.one, [485, 210])
        if self.winner == 2:
            screen.blit(self.two, [485, 210])
        # TODO something is funky here, doesn't really work properly
        if (403 < pygame.mouse.get_pos()[0] < 696 and pressed) and (496 < pygame.mouse.get_pos()[1] < 590 and pressed):
            self.handler.getStateManager().setCurrentState("MainMenuState")
        if (403 < pygame.mouse.get_pos()[0] < 696) and (496 < pygame.mouse.get_pos()[1] < 590):
            pygame.draw.rect(screen, colors["GREEN"], [403, 496, 294, 94])

        if (403 < pygame.mouse.get_pos()[0] < 696 and pressed) and (596 < pygame.mouse.get_pos()[1] < 690 and pressed):
            self.handler.getStateManager().setCurrentState("PlayerSelectionState")
        if (403 < pygame.mouse.get_pos()[0] < 696) and (596 < pygame.mouse.get_pos()[1] < 690):
            pygame.draw.rect(screen, colors["GREEN"], [403, 596, 294, 94])

        if (403 < pygame.mouse.get_pos()[0] < 696 and pressed) and (696 < pygame.mouse.get_pos()[1] < 790 and pressed):
            self.handler.getStateManager().setCurrentState("MapSelectionState")
        if (403 < pygame.mouse.get_pos()[0] < 696) and (696 < pygame.mouse.get_pos()[1] < 790):
            pygame.draw.rect(screen, colors["GREEN"], [403, 696, 294, 94])
