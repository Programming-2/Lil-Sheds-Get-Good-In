from levels.Level import Level
from src.Platform import Platform
from datastructures.CircularQueue import CircularQueue
import pygame


class FactoryLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/Factory.png")
        self.ground = Platform(screen, 0, 650, 1100, 150, -1)
        self.cPlat = Platform(screen, 350, 400, 400, 50, -1)
        self.platformGroup.add(self.ground)
        self.platformGroup.add(self.cPlat)

        self.conveyorAnimation = CircularQueue()
        self.conveyorOne = pygame.image.load("media/misc/conveyorSpriteOne.png")
        self.conveyorTwo = pygame.image.load("media/misc/conveyorSpriteTwo.png")
        self.conveyorAnimation.addData(self.conveyorOne)
        self.conveyorAnimation.addData(self.conveyorTwo)

    def update(self, screen):
        screen.blit(self.conveyorAnimation.get(), (400, 500))
