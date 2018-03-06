import pygame
from players.Player import Player
from src.Platform import Platform
from utils.Colors import colors


class Kyle(Player):

    # TODO Give real data

    def __init__(self, x, y, handler, playNum):
        health = 100
        damage = 15
        winQuote = "Are the platforms fixed yet?"
        loseQuote = "I\'d better try to fix that... emphasis on try"
        name = "Kyle"
        defense = .5

        super().__init__(health, damage, winQuote, loseQuote, name, x, y, handler.getPlatformArray(), handler.getAttackList(), handler, defense)

        self.attacksprite = pygame.image.load("media/PlatformSprite.png")

    def special(self):
        self.specialplatform = Platform(self.screen, self.x - 50, self.y + self.height + 10, self.width + 100, 25)
        self.handler.getPlatformArray().add(self.specialplatform)
        # pygame.draw.rect()
        print(self.specialplatform.rect)

    def update(self, screen):
        self.screen = screen
        self.gravityUpdate()
        self.moveX()
        self.moveY()
        screen.blit(self.sprite, [self.x, self.y])

        if self.xchange > 0:
            self.facing = 1
        elif self.xchange < 0:
            self.facing = -1

        self.attackUpdate(screen)

        for p in self.handler.getPlatformArray():
            if p.height == 25:
                pygame.draw.rect(screen, colors.get("BLACK"), p.rect)
