#Parent Level Class
from abc import abstractmethod

import pygame
pygame.init()


class Level():
    def __init__(self, screen, back_img):
        self.__screen = screen
        self.__back_img = back_img

<<<<<<< HEAD
size = (1100, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Game")
testlevelchange = 0

background_image1 = pygame.image.load("Test.png").convert()
background_image1p2 = pygame.image.load("Test1p2.png").convert()
background_image1p3 = pygame.image.load("Test1p3.png").convert()
background_image1p4 = pygame.image.load("Test1p4.png").convert

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    testlevelchange += 1
    pygame.display.flip()
    clock.tick(60)
    if testlevelchange <= 1000:
        screen.blit(background_image1, [0, 0])
    if testlevelchange >= 2000 and testlevelchange <= 2999:
        screen.blit(background_image1p2, [0, 0])
    if testlevelchange >= 3000 and testlevelchange <= 399:
        screen.blit(background_image1p3, [0, 0])
    if testlevelchange >= 4000 and testlevelchange <= 4999:
        screen.blit(background_image1p4, [0, 0])
    print (testlevelchange)
pygame.quit()
=======
    @abstractmethod
    def update(self):
        pass
>>>>>>> 6e4ac37551561c4717791945e2dc25bd1d08bbb4
