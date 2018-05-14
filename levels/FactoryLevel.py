from levels.Level import Level
from src.Platform import Platform
from datastructures.CircularQueue import CircularQueue
import pygame


class FactoryLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/Levels/Factory.png")
        self.conveyorAnimation = CircularQueue()
        self.conveyorAnimation2 = CircularQueue()
        self.conveyorOne = pygame.image.load("media/misc/conveyorSpriteOne.png")
        self.conveyorTwo = pygame.image.load("media/misc/conveyorSpriteTwo.png")
        #self.conveyorOne = pygame.transform.flip(self.conveyorOne, True, False)
        for a in range(0,5):
            self.conveyorAnimation.addData(self.conveyorOne)
        for a in range(0,5):
            self.conveyorAnimation.addData(self.conveyorTwo)
        self.conveyorOne2 = pygame.transform.flip(self.conveyorOne, True, False)
        self.conveyorTwo2 = pygame.transform.flip(self.conveyorTwo, True, False)
        for a in range(0,5):
            self.conveyorAnimation2.addData(self.conveyorOne2)
        for a in range(0,5):
            self.conveyorAnimation2.addData(self.conveyorTwo2)
    def update(self, screen):
        screen.blit(self.conveyorAnimation.get(), (0, 416))
        screen.blit(self.conveyorAnimation2.get(), (650, 416))
