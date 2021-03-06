import pygame
from utils.Colors import colors


class InfoBar(pygame.sprite.Sprite):
    def __init__(self, screen, player, handler):
        super().__init__()
        self.LIGHT_GRAY = (150, 150, 150)
        self.DARK_GRAY = (100, 100, 100)

        self.screen = screen
        self.player = player

        self.width = player.width
        self.height = 10
        self.specialrect = pygame.Rect(player.rect.x, player.rect.y, self.width, self.height)
        self.rangedrect = pygame.Rect(player.rect.x, player.rect.y, self.width, self.height / 2)
        pygame.font.init()
        self.font = pygame.font.SysFont("Boogaloo Regular", 24)
        self.lasttickhp = player.health
        self.damagearray = []
        self.arraypos = 0
        self.handler = handler

    def update(self, rangedcd, specialcd, currenthp):
        if self.lasttickhp != currenthp:
            if len(self.damagearray) > 3:
                del(self.damagearray[0])
            self.damagearray.reverse()
            self.damagearray.append([self.lasttickhp - currenthp, self.handler.getTick()])
            self.damagearray.reverse()

        for obj in self.damagearray:
            text = self.font.render(str(int(obj[0])), False, colors.get("RED"))
            self.screen.blit(text, (self.player.rect.x + 20, self.player.rect.y - 35 - (self.handler.getTick() - obj[1])))
            if self.handler.getTick() - obj[1] > 80:
                self.damagearray.remove(obj)

        if self.player.special_cooldown.getTotalCooldown() > 0:
            self.specialrect.x = self.player.rect.x
            self.specialrect.y = self.player.rect.y - 10
            specialpct = specialcd / self.player.special_cooldown.getTotalCooldown()
            if specialpct > 1:
                specialpct = 1
            self.specialrect.width = self.width * specialpct
            if specialpct > 0:
                pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.specialrect)

        if self.player.ranged_cooldown.getTotalCooldown() > 0:
            self.rangedrect.x = self.player.rect.x
            self.rangedrect.y = self.player.rect.y - 15
            rangedpct = rangedcd / self.player.ranged_cooldown.getTotalCooldown()
            if rangedpct > 1:
                rangedpct = 1
                self.rangedrect.x = self.player.rect.x
            self.rangedrect.width = self.width * rangedpct
            if rangedpct > 0:
                pygame.draw.rect(self.screen, self.DARK_GRAY, self.rangedrect)

        self.lasttickhp = currenthp
