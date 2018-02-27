import pygame
from states.State import State
from Rect import Rect


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
            Rect(15, 15, 55, 55): "David",
            Rect(15, 85, 55, 55): "Will",
            Rect(15, 160, 55, 55): "Kyle",
            Rect(15, 230, 55, 55): "JB",
            Rect(15, 305, 55, 55): "TBJ",
            Rect(15, 385, 55, 55): "Greg",
            Rect(15, 505, 55, 55): "Lil' Shed"
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
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                if self.firstSelection:
                    self.player1 = self.rects[key]
                else:
                    self.player2 = self.rects[key]
                    self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                    self.handler.getStateManager().setCurrentState("GameState")
