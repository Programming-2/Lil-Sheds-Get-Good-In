import pygame
from states.State import State
from utils.Rect import Rect
from players.David import David
from players.Will import Will
from players.Kyle import Kyle
from players.JaccobBonkley import JaccobBonkley
from players.Jakob import Jakob
from players.Greg import Greg
from players.Shed import Shed
from players.Collin import Collin
from utils.Colors import colors


class PlayerSelectionState(State):

    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img
        self.firstSelection = True
        self.player1 = None
        self.player2 = None
        self.player1Rect = Rect(0, 0, 0, 0)
        self.player2Rect = Rect(0, 0, 0, 0)

        # TODO Fix bug with duplicated players or made it so same player cannot be selected twice

        # Rectangle Dict
        self.rects = {
            Rect(14, 15, 54, 55): David(150, 100, handler),
            Rect(14, 85, 54, 55): Will(150, 100, handler),
            Rect(14, 159, 54, 55): Kyle(150, 100, handler),
            Rect(14, 231, 54, 55): JaccobBonkley(150, 100, handler),
            Rect(14, 303, 54, 55): Jakob(150, 100, handler),
            Rect(14, 388, 54, 55): Greg(150, 100, handler),
            Rect(1050, 750, 50, 50): Collin(150, 100, handler),
            Rect(14, 503, 54, 55): Shed(150, 100, handler)
        }

    def resetState(self):
        self.firstSelection = True
        self.player1 = None
        self.player2 = None
        self.player1Rect = (0, 0, 0, 0)
        self.player2Rect = (0, 0, 0, 0)

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

        # TODO Make going to main menu reset selections

        # Button to return to the main menu
        if (715 < pygame.mouse.get_pos()[0] < 1055 and pressed) and (600 < pygame.mouse.get_pos()[1] < 750 and pressed):
            self.handler.getStateManager().resetStates()
            self.handler.getStateManager().setCurrentState("MainMenuState")

        # Looks at keys in rects dict, and determines if the mouse if clicking that rect
        for key in self.rects:
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                if pressed:
                    if self.firstSelection:
                        self.player1 = self.rects[key]
                        self.player1.setPlayerNum(1)
                        self.player1.setX(150)
                        self.player1.y = 100
                        self.firstSelection = False
                        self.player1Rect = key
                    else:
                        self.player2 = self.rects[key]
                        self.player2Rect = key
                        self.player2.setPlayerNum(2)
                        self.player2.setX(950)
                        self.player2.y = 100
                        self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                        self.handler.getStateManager().setCurrentState("MapSelectionState")
                        # self.handler.getStateManager().setCurrentState("GameState")
                else:
                    pygame.draw.rect(screen, colors["GREEN"], key)

        # Colors selected player black
        pygame.draw.rect(screen, colors["BLACK"], self.player1Rect)
        pygame.draw.rect(screen, colors["BLACK"], self.player2Rect)
