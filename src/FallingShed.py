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
        if pygame.sprite.collide_rect(self.handler.getPlayer1(), self):
            self.handler.getPlayer1().takeTrueDamage(15)
        if pygame.sprite.collide_rect(self.handler.getPlayer2(), self):
            self.handler.getPlayer2().takeTrueDamage(15)

    def moveY(self):
        self.rect.y += self.ychange
        if pygame.sprite.spritecollide(self, self.handler.getPlatformArray(), False):
            print("Collide")
            self.destroyBox()
