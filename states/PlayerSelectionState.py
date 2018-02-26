import pygame
from states.State import State


class PlayerSelectionState(State):

    # TODO Implement player selection

    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img
        self.firstSelection = True
        self.player1 = None
        self.player2 = None

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

        # TODO Make code nicer
        if (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (15 < pygame.mouse.get_pos()[1] < 70 and pressed):
            # David
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = David
            else:
                # self.player1 = David
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (85 < pygame.mouse.get_pos()[1] < 140 and pressed):
            # Will
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = Will
            else:
                # self.player1 = Will
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (160 < pygame.mouse.get_pos()[1] < 215 and pressed):
            # Kyle
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = Kyle
            else:
                # self.player1 = Kyle
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (230 < pygame.mouse.get_pos()[1] < 285 and pressed):
            # JB
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = JB
            else:
                # self.player1 = JB
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (305 < pygame.mouse.get_pos()[1] < 355 and pressed):
            # TBJ
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = TBJ
            else:
                # self.player1 = TBJ
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (385 < pygame.mouse.get_pos()[1] < 455 and pressed):
            # Greg
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = Greg
            else:
                # self.player1 = Greg
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
        elif (15 < pygame.mouse.get_pos()[0] < 70 and pressed) and (505 < pygame.mouse.get_pos()[1] < 560 and pressed):
            # Lil' Shed
            if self.firstSelection:
                self.firstSelection = False
                # self.player1 = LilShed
            else:
                # self.player1 = LilShed
                self.handler.getStateManager().getState("GameState").setPlayers(self.player1, self.player2)
                self.handler.getStateManager().setCurrentState("GameState")
