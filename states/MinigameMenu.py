import pygame

from utils.Colors import colors
from utils.Rect import Rect
from states.State import State
from states.Pong import Pong
from states.Tetris import Tetris


class MinigameMenu(State):
    def __init__(self, name, handler, img):
        super().__init__(name)
        self.handler = handler
        self.img = img

        self.rects = {
            Rect(51, 103, 337, 159): Pong("Pong", handler),
            Rect(44, 282, 346, 129): Tetris("Tetris", handler)
        }

    def resetState(self):
        pass

    def update(self, screen):
        screen.blit(self.img, (0, 0))

        pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        for key in self.rects:
            if key.contains(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10):
                if pressed:
                    self.handler.getStateManager().setCurrentState(self.rects[key].name)
                else:
                    pygame.draw.rect(screen, colors["GREEN"], key)