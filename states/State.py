from abc import abstractmethod


class State:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self, screen):
        pass
