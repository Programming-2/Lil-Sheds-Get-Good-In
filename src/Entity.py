import pygame


# Basic structure for entities
class Entity(pygame.sprite.Sprite):

    def __init__(self, startx, starty, xchange, ychange, image):
        super().__init__()
        self.x = startx
        self.y = starty
        self.xchange = xchange
        self.ychange = ychange
        self.image = image
        self.image_width = image.get_size()[0]
        self.image_height = image.get_size()[1]
        self.rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)

    # Used to move entity
    def move(self):
        self.x += self.changex
        self.y += self.changey
        self.rect = pygame.Rect(self.x, self.y, self.image_width, self.image_height)

    # Used to render entity
    def render(self, screen):
        screen.blit(self.image, [self.x, self.y])

    # Returns x pos of the entity
    def getX(self):
        return self.x

    # Returns y pos of the entity
    def getY(self):
        return self.y

    # Sets x pos of the entity
    def setX(self, x):
        self.x = x

    # Sets y pos of the entity
    def setY(self, y):
        self.y = y

    # Sets change x
    def setChangeX(self, x):
        self.changex = x

    # Sets change y
    def setChangeY(self, y):
        self.changey = y
