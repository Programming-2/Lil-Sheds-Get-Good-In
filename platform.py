#Platform class
import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, length, height):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.image = pygame.Surface([self.length, self.height])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = self.x, self.y