class CircularQueue:

    def __init__(self):
        self.queue = []
        self.original_queue = []
        self.count = 0

    def addData(self, data):
        self.queue.append(data)
        self.original_queue.append(data)

    def get(self):
        result = self.queue.pop(0)
        self.queue.append(result)
        return result

    def size(self):
        return len(self.queue)

    def reset(self):
        self.queue = self.original_queue
        result = self.queue[0]
        return result
