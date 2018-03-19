import pygame
from utils.Colors import colors


class InfoBar(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.LIGHT_GRAY = (150, 150, 150)

        self.screen = screen
        self.player = player

        self.x = player.x
        self.y = player.y
        self.width = player.width
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.font.init()
        self.font = pygame.font.SysFont("Comic Sans MS", 16)
        self.lasttickhp = player.health
        self.damagearray = []
        self.arraypos = 0

    def update(self, currentcd, currenthp):
        '''if not self.special_available:
            self.special_cooldown = 0
            if self.special_count == 0:
                self.special_start_time = pygame.time.get_ticks()
                self.special_count = 1
            self.special_cooldown = (pygame.time.get_ticks() - self.special_start_time) / 1000
            if self.special_cooldown >= self.special_total_cooldown:
                self.special_available = True
                self.special_count = 0'''
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
                    self.screen.blit(text, (self.player.x, self.player.y - 30))
                if i == 1:
                    text = self.font.render(str(int(self.damagearray[i])), False, colors.get("RED"))
                    self.screen.blit(text, (self.player.x, self.player.y - 45))
                if i == 2:
                    text = self.font.render(str(int(self.damagearray[i])), False, colors.get("RED"))
                    self.screen.blit(text, (self.player.x, self.player.y - 60))
        self.rect.x = self.player.x
        self.rect.y = self.player.y - 10
        pct = currentcd / self.player.special_total_cooldown
        self.rect.width = self.width * pct
        if pct > 0:
            pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.rect)

        self.lasttickhp = currenthp
