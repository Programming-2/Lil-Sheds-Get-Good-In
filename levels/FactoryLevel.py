from levels.Level import Level
from src.Button import Button
from datastructures.CircularQueue import CircularQueue
from src.Platform import Platform
import pygame


class FactoryLevel(Level):

    def __init__(self, screen, handler):
        super().__init__(screen, "media/Levels/Factory.png")
        self.plat1 = Platform(screen, 0, 416, 450, 50, speed=2)
        self.plat2 = Platform(screen, 650, 416, 450, 50, speed=-2)
        self.platformGroup.add(self.plat1)
        self.platformGroup.add(self.plat2)
        self.conveyorAnimation = CircularQueue()
        self.conveyorAnimation2 = CircularQueue()
        self.conveyorOne = pygame.image.load("media/misc/conveyorSpriteOne.png").convert_alpha()
        self.conveyorTwo = pygame.image.load("media/misc/conveyorSpriteTwo.png").convert_alpha()
        self.shedsprite = pygame.image.load("media/misc/shedSprite.png")

        actionLeft = lambda: print("Drop box left")

        actionRight = lambda: print("Drop box right")

        self.buttonLeft = Button(actionLeft, 60, 400, 48, handler)
        self.buttonRight = Button(actionRight, 1000, 400, 48, handler)

        for a in range(0, 10):
            self.conveyorAnimation.addData(self.conveyorOne)
        for a in range(0, 10):
            self.conveyorAnimation.addData(self.conveyorTwo)

        self.conveyorOne2 = pygame.transform.flip(self.conveyorOne, True, False)
        self.conveyorTwo2 = pygame.transform.flip(self.conveyorTwo, True, False)

        for a in range(0, 10):
            self.conveyorAnimation2.addData(self.conveyorOne2)
        for a in range(0, 10):
            self.conveyorAnimation2.addData(self.conveyorTwo2)

    def dropsheds(self, screen):
        if Button.playerInRange:
            screen.blit(self.shedsprite, (300, 300))
            self.shed = Platform(screen, 300, 300, 80, 90, fallspeed=.1)
            self.platformGroup.add(self.shed)
            print("TRUE")

    def update(self, screen):
        screen.blit(self.conveyorAnimation.get(), (0, 416))
        screen.blit(self.conveyorAnimation2.get(), (650, 416))

        self.buttonLeft.update(screen)
        self.buttonRight.update(screen)

        self.plat1.fall()
