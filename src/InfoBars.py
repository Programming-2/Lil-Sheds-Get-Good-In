import pygame
from utils.Colors import colors


class InfoBar(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.LIGHT_GRAY = (150, 150, 150)

        self.screen = screen
        self.player = player

        self.width = player.width
        self.height = 10
        self.rect = pygame.Rect(player.rect.x, player.rect.y, self.width, self.height)
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 16)
        self.lasttickhp = player.health
        self.damagearray = []
        self.arraypos = 0

    def update(self, currentcd, currenthp):
        print("Last tick: " + str(self.lasttickhp))
        print("Current: " + str(currenthp))
        if self.lasttickhp != currenthp:
            if len(self.damagearray) > 3:
                del(self.damagearray[0])
            self.damagearray.reverse()
            self.damagearray.append(self.lasttickhp - currenthp)
            self.damagearray.reverse()
        if len(self.damagearray) >= 1:
            for i in range(0, len(self.damagearray)):
                if i == 0:
                    text = self.font.render(str(int(self.damagearray[i])), False, colors.get("RED"))
                    self.screen.blit(text, (self.player.rect.x, self.player.rect.y - 30))
                if i == 1:
                    text = self.font.render(str(int(self.damagearray[i])), False, colors.get("RED"))
                    self.screen.blit(text, (self.player.rect.x, self.player.rect.y - 45))
                if i == 2:
                    text = self.font.render(str(int(self.damagearray[i])), False, colors.get("RED"))
                    self.screen.blit(text, (self.player.rect.x, self.player.rect.y - 60))
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y - 10
        pct = currentcd / self.player.special_total_cooldown
        self.rect.width = self.width * pct
        if pct > 0:
            pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.rect)

        self.lasttickhp = currenthp
