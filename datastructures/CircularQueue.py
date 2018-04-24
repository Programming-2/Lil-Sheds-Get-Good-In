class CircularQueue:

    def __init__(self):
        self.queue = []

    def addData(self, data):
        self.queue.append(data)

    def get(self):
        result = self.queue.pop(0)
        self.queue.append(result)
        return result

    def size(self):
        return len(self.queue)
