import pygame
import random
from levels.Level import Level
from src.Platform import Platform


class RandomLevel(Level):

    def __init__(self, screen):
        super().__init__(screen, "media/random_map.png")
        self.lWall = Platform(screen, -100, -1000, 100, 1800)
        self.rWall = Platform(screen, 1100, -1000, 100, 1800)
        self.p1 = Platform(screen, (random.randint(0,100)), (random.randint(300,600)), (random.randint(100,150)), (random.randint(300,600)))
        self.p2 = Platform(screen, (random.randint(100,200)), (random.randint(300,600)), (random.randint(200,250)), (random.randint(300,600)))
        self.p3 = Platform(screen, (random.randint(200,300)), (random.randint(300,600)), (random.randint(300,350)),(random.randint(300,600)))
        self.p4 = Platform(screen, (random.randint(300,400)), (random.randint(300,600)), (random.randint(400,450)),(random.randint(300,600)))
        self.p5 = Platform(screen, (random.randint(400,500)), (random.randint(300,600)), (random.randint(500,550)),(random.randint(300,600)))
        self.p6 = Platform(screen, (random.randint(500,600)), (random.randint(300,600)), (random.randint(600,650)),(random.randint(300,600)))
        self.p7 = Platform(screen, (random.randint(600,700)), (random.randint(300,600)), (random.randint(700,750)),(random.randint(300,600)))
        self.p8 = Platform(screen, (random.randint(700,800)), (random.randint(300,600)), (random.randint(800,850)),(random.randint(300,600)))
        self.p9 = Platform(screen, (random.randint(800,900)), (random.randint(300,600)), (random.randint(900,950)),(random.randint(300,600)))
        self.p10 = Platform(screen, (random.randint(900,1000)), (random.randint(300,600)), (random.randint(1000,1050)),(random.randint(300,600)))
        self.p11 = Platform(screen, (random.randint(1000,1100)), (random.randint(300,600)), (random.randint(1000,1100)),(random.randint(300,600)))
        self.platformGroup = pygame.sprite.Group()

        self.platformGroup.add(self.lWall)
        self.platformGroup.add(self.rWall)
        self.platformGroup.add(self.p1)
        self.platformGroup.add(self.p2)
        self.platformGroup.add(self.p3)
        self.platformGroup.add(self.p4)
        self.platformGroup.add(self.p5)
        self.platformGroup.add(self.p6)
        self.platformGroup.add(self.p7)
        self.platformGroup.add(self.p8)
        self.platformGroup.add(self.p9)
        self.platformGroup.add(self.p10)
        self.platformGroup.add(self.p11)


    def update(self):
        pass