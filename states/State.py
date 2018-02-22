from abc import abstractmethod


class State:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
