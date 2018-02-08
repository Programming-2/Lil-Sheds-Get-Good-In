import pygame

class Entity:

    def __init__(startx, starty, image, self):
        self.x = startx
        self.y = starty
        self.changex = 0
        self.changey = 0
        self.image = image

    def move(self):
        self.x += self.changex
        self.y += self.changey

    def render(screen, self):
        screen.blit(self.image, [self.x, self.y])