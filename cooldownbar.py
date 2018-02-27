import pygame


class CooldownBar(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super().__init__()
        self.LIGHT_GRAY = (200, 200, 200)

        self.screen = screen
        self.player = player

        self.x = player.x
        self.y = player.y
        self.width = player.width
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, currentcd):
        print(currentcd)
        self.rect.x = self.player.x
        self.rect.y = self.player.y - 10
        pct = currentcd / self.player.special_total_cooldown
        self.rect.width = self.width * pct
        if pct > 0:
            pygame.draw.rect(self.screen, self.LIGHT_GRAY, self.rect)
