import pygame


# Basic structure for entities
class Entity(pygame.sprite.Sprite):

    def __init__(self, startx, starty, xchange, ychange, image):
        super().__init__()
        self.xchange = xchange
        self.ychange = ychange
        self.image = image
        self.image_width = image.get_size()[0]
        self.image_height = image.get_size()[1]
        self.rect = pygame.Rect(startx, starty, self.image_width, self.image_height)
        self.rect.x = startx
        self.rect.y = starty

    # Used to move entity
    def move(self):
        self.rect.x += self.changex
        self.rect.y += self.changey
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.image_width, self.image_height)

    # Used to render entity
    def render(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    # Returns x pos of the entity
    def getX(self):
        return self.rect.x

    # Returns y pos of the entity
    def getY(self):
        return self.rect.y

    # Sets x pos of the entity
    def setX(self, x):
        self.rect.x = x

    # Sets y pos of the entity
    def setY(self, y):
        self.rect.y = y

    # Sets change x
    def setChangeX(self, x):
        self.changex = x

    # Sets change y
    def setChangeY(self, y):
        self.changey = y
