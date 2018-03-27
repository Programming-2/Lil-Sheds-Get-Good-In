import pygame
from utils.Colors import colors


class HealthBar(pygame.sprite.Sprite):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, screen, position, health):
        super().__init__()
        self.screen = screen
        self.position = position
        self.screensize = screen.get_size()
        self.health = health

        if position == "topleft":
            self.x = 10
            self.y = 10

        if position == "topright":
            self.x = self.screensize[0] - 510
            self.y = 10

        self.width = 500
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.borderrect = pygame.Rect(self.x-5, self.y-5, self.width+10, self.height + 10)
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 24)

    def update(self, currenthp):
        pygame.draw.rect(self.screen, self.BLACK, self.borderrect)
        if currenthp < 0:
            currenthp = 0
        pct = currenthp / self.health
        if self.position == "topleft":
            self.rect.width = self.width * pct
            if pct >= .7:
                pygame.draw.rect(self.screen, self.GREEN, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("WHITE"))
            if .3 <= pct < .7:
                pygame.draw.rect(self.screen, self.YELLOW, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("BLACK"))
            if pct < .3:
                pygame.draw.rect(self.screen, self.RED, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("WHITE"))
            self.screen.blit(text, (20, 20))
        if self.position == "topright":
            self.rect.width = self.width * pct
            self.rect.x = (self.screensize[0] - 10) - self.rect.width
            if pct >= .7:
                pygame.draw.rect(self.screen, self.GREEN, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("WHITE"))
            if .3 <= pct < .7:
                pygame.draw.rect(self.screen, self.YELLOW, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("BLACK"))
            if pct < .3:
                pygame.draw.rect(self.screen, self.RED, self.rect)
                text = self.font.render(str(int(currenthp)) + " | " + str(self.health), False, colors.get("WHITE"))
            self.screen.blit(text, (self.screensize[0] - 125, 20))
