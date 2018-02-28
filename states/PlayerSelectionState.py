import pygame
from states.State import State
from Rect import Rect
from players.David import David
from players.Will import Will
from players.Kyle import Kyle
from players.JaccobBonkley import JaccobBonkley
from players.Jakob import Jakob
from players.Greg import Greg
from players.Shed import Shed


class PlayerSelectionState(State):

    # TODO Implement player selection

    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img
        self.firstSelection = True
        self.player1 = None
        self.player2 = None

        # Rectangle Dict
        self.rects = {
            Rect(15, 15, 55, 55): David(150, 100, handler, 0),
            Rect(15, 85, 55, 55): Will(150, 100, handler, 0),
            Rect(15, 160, 55, 55): Kyle(150, 100, handler, 0),
            Rect(15, 230, 55, 55): JaccobBonkley(150, 100, handler, 0),
            Rect(15, 305, 55, 55): Jakob(150, 100, handler, 0),
            Rect(15, 385, 55, 55): Greg(150, 100, handler, 0),
            Rect(15, 505, 55, 55): Shed(150, 100, handler, 0)
        }

    def update(self, screen):
        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        screen.blit(self.img, [0, 0])

        if (690 < pygame.mouse.get_pos()[0] < 975 and pressed) and (545 < pygame.mouse.get_pos()[1] < 690 and pressed):
            self.handler.getStateManager().setCurrentState("MainMenuState")

        for key in self.rects:
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10) and pressed:
                if self.firstSelection:
                    self.player1 = self.rects[key]
                    self.player1.setPlayerNum(1)
                    self.firstSelection = False
                else:
                    self.player2 = self.rects[key]
                    self.player2.setPlayerNum(2)
                    self.player2.setX(850)
                    self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                    self.handler.getStateManager().setCurrentState("GameState")
