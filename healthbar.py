import pygame


class HealthBar(pygame.sprite.Sprite):
    RED = (255,   0,   0)

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

    def update(self, currenthp):
        pct = currenthp / self.health
        pygame.draw.rect(self.screen, self.RED, self.rect)
        self.rect.width = self.width * pct
