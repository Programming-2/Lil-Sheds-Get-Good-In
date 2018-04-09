from dataStructures.Node import Node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def instet(self, data):
        newNode = Node(data)
        newNode.setNextNode(self.head)
        self.head = newNode

    def size(self):
        currentNode = self.head
        i = 0
        while currentNode:
            i += 1
            currentNode = currentNode.nextNode()
        return i

    def search(self, data):
        currentNode = self.head
        foundNode = False
        while currentNode and not foundNode:
            if currentNode.getData() == data:
                foundNode = True
            else:
                currentNode = currentNode.nextNode()
        if currentNode is None:
            raise ValueError("Data not in list")
        return currentNode