import pygame


class Rect(pygame.Rect):

    def __hash__(self):
        prime = 31
        result = 0
        result = prime * result + self.height
        result = prime * result + self.width
        result = prime * result + self.x
        result = prime * result + self.y
        return result
