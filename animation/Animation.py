import pygame


class Animation:
    def __init__(self, handler, player, image_list=None):
        self.image_list = []
        if image_list:
            self.image_list = image_list
        self.index = 0
        self.loop_count = 0
        self.loop_once_count = 0
        self.start_tick = 0

        self.handler = handler
        self.player = player

    def add(self, image):
        self.image_list.append(image)

    def loop(self, delay):
        if self.loop_count == 0:
            self.start_tick = self.handler.getTick()
            self.loop_count += 1
        if (self.handler.getTick() - self.start_tick) % delay == 0:
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
            self.start_tick = self.handler.getTick()
        if (self.handler.getTick() - self.start_tick) % delay == 0:
            self.index += 1
            if self.index >= len(self.image_list):
                self.index = 0
                self.loop_once_count = 1
            if self.player.facing is -1:
                self.player.sprite = pygame.transform.flip(self.image_list[self.index], True, False)
            if self.player.facing is 1:
                self.player.sprite = self.image_list[self.index]
    
    def displayFirst(self):
        if self.player.facing == 1:
            self.player.sprite = self.image_list[0]
        if self.player.facing == -1:
            self.player.sprite = pygame.transform.flip(self.image_list[0], True, False)

    def reset(self):
        self.loop_count = 0
        self.loop_once_count = 0
