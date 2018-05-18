import random

class PunDatabase:

    def __init__(self):
        self.puns = [
            "That is wheely funny",
            "I stayed up all night to see where the sun went, then it dawned on me",
            "What's a cow eating grass, a lawn mooer",
            "The majority of people find bananas a peeling"
        ]

    def getRandomPun(self):
        randNum = random.randint(0, len(self.puns))
        return self.puns[randNum]
