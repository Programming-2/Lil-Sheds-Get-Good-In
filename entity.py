import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, startx, starty, image):
        self.x = startx
        self.y = starty
        self.changex = 0
        self.changey = 0
        self.image = image

    def move(self):
        self.x += self.changex
        self.y += self.changey

    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y