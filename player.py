import pygame


class player(pygame.sprite.Sprite):

    def __init__(self, img):
        super().__init__()
        self.img = img