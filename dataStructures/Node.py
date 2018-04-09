class Node:

    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, node):
        self.nextNode = node

    def getData(self):
        return self.data
