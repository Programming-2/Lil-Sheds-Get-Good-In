import pygame


class KeyboardManager:

    def __init__(self):
        self.keysDown = [False] * 316
        self.keysUp = [False] * 316

    def update(self):
        self.keysDown = [False] * 316
        self.keysUp = [False] * 316
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keysDown[event.key] = True
            elif event.type == pygame.KEYUP:
                self.keysUp[event.key] = True
