class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    # Returns 0 if the next node should be the head
    def getNextNode(self):
        if self.nextNode is not None:
            return self.nextNode
        else:
            return 0

    def setNextNode(self, node):
        self.nextNode = node

    def getData(self):
        return self.data
