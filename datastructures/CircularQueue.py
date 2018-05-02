class CircularQueue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def addData(self, data):
        self.queue.append(data)

    def get(self):
        output = self.queue[self.index]
        if self.index + 1 == len(self.queue):
            self.index = 0
        else:
            self.index += 1
        return output

    def size(self):
        return len(self.queue)

    def reset(self):
        self.index = 0

    def getAnimFrames(self, handler, ticks, reset):
        if reset:
            self.reset()
        if handler.getTicks() % ticks:
            self.index += 1
        return self.queue[self.index]
