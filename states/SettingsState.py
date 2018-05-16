import pygame
from states.State import State
from utils.Rect import Rect
from players.Collin import Collin
from players.Kemul import Kemul
from players.Jarod import Jarod
from players.Smo import Smo
from utils.Colors import colors
from utils.Sound import Sound
from user.settings import Settings


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
        self.settings = Settings()

        # TODO Fix bug with duplicated players or made it so same player cannot be selected twice

        # Rectangle Dict
        self.rects = {
            Rect(23, 89, 60, 60): Collin(150, 100, handler),
            Rect(23, 214, 60, 60): Smo(150, 100, handler),
            Rect(23, 336, 60, 60): Kemul(150, 100, handler),
            Rect(23, 465, 60, 60): Jarod(150, 100, handler)
        }

        self.color_rects = {
            colors.get("RED"): Rect(0, 0, 200, 1000),
            colors.get("ORANGE"): Rect(200, 0, 200, 800),
            colors.get("YELLOW"): Rect(400, 0, 200, 800),
            colors.get("GREEN"): Rect(600, 0, 200, 800),
            colors.get("BLUE"): Rect(800, 0, 200, 800),
            colors.get("PURPLE"): Rect(1000, 0, 200, 800),
            colors.get("PINK"): Rect(1200, 0, 200, 800),
        }

    def update(self, screen):
        pressed = False

        for key in self.color_rects:
            pygame.draw.rect(screen, key, self.color_rects[key])
            self.color_rects[key].x += 100
            if self.color_rects[key].x > 1200:
                self.color_rects[key].x = -200

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
            self.handler.getStateManager().setCurrentState("MainMenuState")

        if (39 < pygame.mouse.get_pos()[0] < 91 and pressed) and (66 < pygame.mouse.get_pos()[1] < 118 and pressed):
            self.settings.setSFX()
            self.settings.write()

        if (39 < pygame.mouse.get_pos()[0] < 91 and pressed) and (176 < pygame.mouse.get_pos()[1] < 228 and pressed):
            self.settings.setMusic()
            self.settings.write()

        # Colors selected player black
        if self.settings.useSFX():
            pygame.draw.rect(screen, colors.get("BLUE"), Rect(39, 66, 52, 52))
        
        if self.settings.useMusic(): 
            pygame.draw.rect(screen, colors.get("BLUE"), Rect(39, 176, 52, 52))
