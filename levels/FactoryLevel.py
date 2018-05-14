from levels.Level import Level
from src.Platform import Platform
from datastructures.CircularQueue import CircularQueue
import pygame


class FactoryLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/Factory.png")
        self.conveyorAnimation = CircularQueue()
        self.conveyorOne = pygame.image.load("media/misc/conveyorSpriteOne.png")
        self.conveyorTwo = pygame.image.load("media/misc/conveyorSpriteTwo.png")
        for a in range(0,5):
            self.conveyorAnimation.addData(self.conveyorOne)
        for a in range(0,5):
            self.conveyorAnimation.addData(self.conveyorTwo)

    def update(self, screen):
        screen.blit(self.conveyorAnimation.get(), (400, 500))
