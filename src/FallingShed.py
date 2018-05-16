from src.Entity import Entity
import pygame


class FallingShed(Entity):

    def __init__(self, handler, startx):
        img = pygame.image.load("media/Players/Lil' Shed/Lil' Shed.png")
        super().__init__(startx, 50, 0, 3, img)
        self.broken = False
        self.handler = handler

    def update(self, screen):
        self.moveY()
        self.render(screen)

    def destroyBox(self):
        print("Destroy Box")
        self.broken = True

    def moveY(self):
        self.y += self.ychange
        platList = pygame.sprite.spritecollide(self, self.handler.getPlatformArray(), False)
        for platform in platList:
            print("Collide")
            if self.ychange > 0 and self.rect.bottom < platform.rect.bottom:  # Moving down and over platform
                self.rect.bottom = platform.rect.top
            self.setChangeY(0)
            platform.entMove(self)
            self.destroyBox()
