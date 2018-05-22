import pygame


class Animation:
    def __init__(self, handler, player, image_list=None):
        self.image_list = []
        if image_list:
            self.image_list = image_list
        self.index = 0
        self.loop_once_count = 0

        self.handler = handler
        self.player = player

    def add(self, image):
        self.image_list.append(image)

    def loop(self, delay):
        print(self.image_list)
        if self.handler.getTick() % delay == 0:
            self.index += 1
            if self.index >= len(self.image_list):
                self.index = 0
            if self.player.facing == -1:
                self.player.sprite = pygame.transform.flip(self.image_list[self.index], True, False)
            if self.player.facing == 1:
                self.player.sprite = self.image_list[self.index]

    def loopFromStart(self, delay):
        if self.loop_once_count == 0:
            self.index = -1
            self.loop_once_count += 1
        if self.handler.getTick() % delay == 0:
            self.index += 1
            if self.index >= len(self.image_list):
                self.index = 0
                self.loop_once_count = 0
            self.player.sprite = self.image_list[self.index]
    
    def displayFirst(self):
        if self.player.facing == 1:
            self.player.sprite = self.image_list[0]
        if self.player.facing == -1:
            self.player.sprite = pygame.transform.flip(self.image_list[0], True, False)
