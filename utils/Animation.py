# Documentation for how to use animations
# Make nodes and point them to the next animation frame
# The last node should point back to the first
# EX: walk1 -> walk2 -> walk3 -> walk1


class Animation:

    def __init__(self, startingNode):
        self.currectAnimation = startingNode

    def getCurrectAnimationFrame(self):
        returnNode = self.currectAnimation
        self.currectAnimation = self.currectAnimation.getNextNode()
        return returnNode