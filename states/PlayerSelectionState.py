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
from players.Kemul import Kemul
from players.Jarod import Jarod
from players.Smo import Smo
from players.Reynaldo import Reynaldo
from utils.Colors import colors
from utils.Sound import Sound


class PlayerSelectionState(State):

    def __init__(self, name, handler, base_img, hidden_img):
        super().__init__(name)
        self.handler = handler
        self.base_img = base_img
        self.hidden_img = hidden_img
        self.player1 = None
        self.player2 = None
        self.player1Rect = Rect(0, 0, 0, 0)
        self.player2Rect = Rect(0, 0, 0, 0)
        self.hoverOver = Sound("Beep2")
        self.hoverPlay = 0
        self.background_color = [0, 0, 0]
        self.background_rect = pygame.Rect(0, 0, 1100, 800)
        self.red_change = 1
        self.green_change = 1
        self.blue_change = 1
        self.red_done = False
        self.green_done = False
        self.blue_done = False
        self.state = 1

        # Rectangle Dict
        self.base_player_rects = {
            Rect(30, 51, 47, 47): David(150, 100, handler),
            Rect(30, 141, 47, 47): Greg(150, 100, handler),
            Rect(30, 225, 47, 47): JaccobBonkley(150, 100, handler),
            Rect(30, 311, 47, 47): Jakob(150, 100, handler),
            Rect(30, 395, 47, 47): Kyle(150, 100, handler),
            Rect(30, 482, 47, 47): Will(150, 100, handler),
            Rect(228, 323, 26, 34): Shed(150, 100, handler)
        }

        self.hidden_player_rects = {
            Rect(23, 89, 60, 60): Collin(150, 100, handler),
            Rect(23, 214, 60, 60): Smo(150, 100, handler),
            Rect(23, 336, 60, 60): Kemul(150, 100, handler),
            Rect(23, 465, 60, 60): Jarod(150, 100, handler),
            Rect(818, 45, 35, 35): Reynaldo(150, 100, handler)
        }

        self.color_rects = {
            colors.get("RED"): Rect(0, 0, 200, 800),
            colors.get("ORANGE"): Rect(200, 0, 200, 800),
            colors.get("YELLOW"): Rect(400, 0, 200, 800),
            colors.get("GREEN"): Rect(600, 0, 200, 800),
            colors.get("BLUE"): Rect(800, 0, 200, 800),
            colors.get("PURPLE"): Rect(1000, 0, 200, 800),
            colors.get("PINK"): Rect(1200, 0, 200, 800),
        }

    def resetState(self):
        self.handler.firstSelection = True
        self.player1 = None
        self.player2 = None
        self.player1Rect = (0, 0, 0, 0)
        self.player2Rect = (0, 0, 0, 0)

    def update(self, screen):
        if self.state == 1:
            if not self.background_color[0] == 255 and not self.red_done:
                self.background_color[0] += self.red_change
            if self.background_color[0] == 255:
                self.red_done = True
            if self.red_done:
                self.background_color[0] -= self.red_change
            if self.background_color[0] == 0:
                self.red_done = False
            if self.red_done and not self.background_color[1] == 255:
                self.background_color[1] += self.green_change
            if self.background_color[1] == 255:
                self.green_done = True
            if self.green_done:
                self.background_color[1] -= self.green_change
            if self.background_color[1] == 0:
                self.green_done = False
            if self.green_done and not self.background_color[2] == 255:
                self.background_color[2] += self.blue_change
            if self.background_color[2] == 255:
                self.blue_done = True
            if self.blue_done:
                self.background_color[2] -= self.blue_change
            if self.background_color[2] == 0:
                self.blue_done = False
            pygame.draw.rect(screen, self.background_color, self.background_rect)
            pressed = False

            # Event look
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handler.setDone(True)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pressed = True

            # Drawing background image
            screen.blit(self.base_img, [0, 0])

            # Button to return to the main menu
            if (715 < pygame.mouse.get_pos()[0] < 1055 and pressed) and (600 < pygame.mouse.get_pos()[1] < 750 and pressed):
                self.handler.getStateManager().resetStates()
                self.handler.getStateManager().setCurrentState("MainMenuState")

            # Hidden Character Menu
            if (1050 < pygame.mouse.get_pos()[0] < 1100 and pressed) and (750 < pygame.mouse.get_pos()[1] < 800 and pressed):
                self.state = 2

            # Looks at keys in rects dict, and determines if the mouse if clicking that rect
            for key in self.base_player_rects:
                if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                    if pressed:
                        self.hoverOver.playSound()
                        if self.handler.firstSelection:
                            self.player1 = self.base_player_rects[key]
                            self.player1.setX(150)
                            self.player1.y = 100
                            self.handler.firstSelection = False
                            self.player1Rect = key
                            self.hoverPlay = 0
                            self.handler.player1 = self.player1
                        else:
                            if self.player1.name != self.base_player_rects[key].name:
                                self.player2 = self.base_player_rects[key]
                                self.player2Rect = key
                                self.player2.setX(950)
                                self.player2.y = 100
                                self.handler.player2 = self.player2
                                self.handler.getStateManager().getState("HiddenPlayerState").resetState()
                                self.handler.getStateManager().getState("GameState").setPlayers(self.handler.player1, self.handler.player2)
                                self.handler.getStateManager().setCurrentState("MapSelectionState")
                                # self.handler.getStateManager().setCurrentState("GameState")
                                self.hoverPlay = 0
                    else:
                        pygame.draw.rect(screen, colors["GREEN"], key)

            # Colors selected player black
            pygame.draw.rect(screen, colors["BLACK"], self.player1Rect)
            pygame.draw.rect(screen, colors["BLACK"], self.player2Rect)
        if self.state == 2:
            for key in self.color_rects:
                pygame.draw.rect(screen, key, self.color_rects[key])
                self.color_rects[key].x += 10
                if self.color_rects[key].x > 1200:
                    self.color_rects[key].x = -200

            pressed = False

            # Event look
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handler.setDone(True)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pressed = True

            # Drawing background image
            screen.blit(self.hidden_img, [0, 0])

            # Button to return to the main menu
            if (715 < pygame.mouse.get_pos()[0] < 1055 and pressed) and (
                    600 < pygame.mouse.get_pos()[1] < 750 and pressed):
                self.state = 1

            # Looks at keys in rects dict, and determines if the mouse if clicking that rect
            for key in self.hidden_player_rects:
                if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                    if pressed:
                        self.hoverOver.playSound()
                        if self.handler.firstSelection:
                            self.player1 = self.hidden_player_rects[key]
                            self.player1.setX(150)
                            self.player1.y = 100
                            self.handler.firstSelection = False
                            self.player1Rect = key
                            self.hoverPlay = 0
                            self.handler.player1 = self.player1
                        else:
                            if self.player1.name != self.hidden_player_rects[key].name:
                                self.player2 = self.hidden_player_rects[key]
                                self.player2Rect = key
                                self.player2.setX(950)
                                self.player2.y = 100
                                self.handler.player2 = self.player2
                                self.handler.getStateManager().getState("GameState").setPlayers(self.handler.player1,
                                                                                                self.handler.player2)
                                self.handler.getStateManager().setCurrentState("MapSelectionState")
                                # self.handler.getStateManager().setCurrentState("GameState")
                                self.hoverPlay = 0
                    else:
                        pygame.draw.rect(screen, colors["GREEN"], key)

            # Colors selected player black
            pygame.draw.rect(screen, colors["BLACK"], self.player1Rect)
            pygame.draw.rect(screen, colors["BLACK"], self.player2Rect)

