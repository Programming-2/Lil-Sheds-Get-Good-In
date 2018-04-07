import pygame


class Animation:

    def __init__(self, startingNode):
        self.currectAnimation = startingNode

    def getCurrectAnimationFrame(self):
        returnNode = self.currectAnimation
        self.currectAnimation = self.currectAnimation.getNextNode()
        return returnNode