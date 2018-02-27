import pygame


class Rect(pygame.Rect):

    def __hash__(self):
        return self.x.__hash__() + self.y.__hash__() + self.width.__hash__() + self.height.__hash__()
