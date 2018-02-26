import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, startx, starty, changex, changey, image):
        super().__init__()
        self.x = startx
        self.y = starty
        self.changex = changex
        self.changey = changey
        self.image = image
        self.image_width = image.get_size()[0]
        self.image_height = image.get_size()[1]
        self.rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)

    def move(self):
        self.x += self.changex
        self.y += self.changey
        self.rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)

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

    def setChangeX(self, x):
        self.changex = x

    def setChangeY(self, y):
        self.changey = y
