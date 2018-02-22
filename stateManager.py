class StateManager:

    def __init__(self, states):
        self.states = states
        self.currentState = None

    def addState(self, name, state):
        self.states[name] = state

    def setCurrentState(self, name):
        if name in self.states:
            self.currentState = self.states[name]
        else:
            raise Exception("Selected an invalid state.")
