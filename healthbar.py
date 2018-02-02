import pygame


class HealthBar(pygame.sprite.Sprite):
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
            self.x = (self.screensize[0] / 2) + 10
            self.y = 10

        self.width = (self.screensize[0] / 2) - 20
        self.height = (self.screensize[1] / 20)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect.topleft = self.x, self.y
        self.rect.width *= self.health
