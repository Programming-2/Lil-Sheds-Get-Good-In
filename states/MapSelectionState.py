import pygame
from states.State import State
from utils.Rect import Rect
from levels.GrassLevel import GrassLevel
from levels.IceLevel import IceLevel
from levels.LavaLevel import LavaLevel
from levels.RandomLevel import RandomLevel
from levels.FactoryLevel import FactoryLevel
from levels.Mazelevel import Mazelevel
from utils.Colors import colors


class MapSelectionState(State):

    def __init__(self, name, handler, screen, img):
        super().__init__(name)
        self.img = img
        self.handler = handler
        self.map = None

        # Rectangle Dict
        self.rects = {
            Rect(18, 18, 1064, 114): GrassLevel(screen, handler),
            Rect(18, 160, 1064, 115): IceLevel(screen, handler),
            Rect(18, 304, 1064, 114): LavaLevel(screen, handler),
            Rect(18, 664, 100, 114): RandomLevel(screen, handler),
            Rect(18, 444, 1064, 114): FactoryLevel(screen, self.handler),
            Rect(20, 464, 40, 114): Mazelevel(screen, handler),
        }

    def resetState(self):
        self.map = None
        self.handler.player1.__init__(150, 100, self.handler)
        self.handler.player2.__init__(950, 100, self.handler)

    def update(self, screen):
        pressed = False

        # Event look
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        # Drawing background image
        screen.blit(self.img, [0, 0])

        # Button to return to the main menu
        if (715 < pygame.mouse.get_pos()[0] < 1055 and pressed) and (600 < pygame.mouse.get_pos()[1] < 750 and pressed):
            self.handler.getStateManager().resetStates()
            self.handler.getStateManager().setCurrentState("MainMenuState")

        # Looks at keys in rects dict, and determines if the mouse if clicking that rect
        for key in self.rects:
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                if pressed:
                    self.rects[key].__init__(screen, self.handler)
                    self.handler.setLevel(self.rects[key])
                    self.handler.getStateManager().getState("GameState").reloadLevel()
                    self.handler.getStateManager().setCurrentState("GameState")
                else:
                    pygame.draw.rect(screen, colors["GREEN"], key)
