import pygame
from states.State import State
from utils.Rect import Rect
from players.Collin import Collin
from players.Kemul import Kemul
from players.Jarod import Jarod
from players.Smo import Smo
from utils.Colors import colors
from utils.Sound import Sound


class SettingsState(State):

    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img
        self.player1 = None
        self.player2 = None
        self.player1Rect = Rect(0, 0, 0, 0)
        self.player2Rect = Rect(0, 0, 0, 0)
        self.hoverOver = Sound("Beep2")
        self.hoverPlay = 0

        # TODO Fix bug with duplicated players or made it so same player cannot be selected twice

        # Rectangle Dict
        self.rects = {
            Rect(23, 89, 60, 60): Collin(150, 100, handler),
            Rect(23, 214, 60, 60): Smo(150, 100, handler),
            Rect(23, 336, 60, 60): Kemul(150, 100, handler),
            Rect(23, 465, 60, 60): Jarod(150, 100, handler)
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
            self.handler.getStateManager().setCurrentState("PlayerSelectionState")

        # Colors selected player black
        pygame.draw.rect(screen, colors["BLACK"], self.player1Rect)
        pygame.draw.rect(screen, colors["BLACK"], self.player2Rect)
