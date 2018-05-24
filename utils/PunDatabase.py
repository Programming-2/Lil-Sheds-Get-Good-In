import random

class PunDatabase:

    def __init__(self):
        self.puns = [
            "Is your dish washer running? If so you better go catch it!",
            "I stayed up all night to see where the sun went, then it dawned on me",
            "What's a cow eating grass, a lawn mooer",
            "The majority of people find bananas a peeling",
            "An old man fell into a well, he couldn't see that well",
            "How do make a tissue dance? You put a little boogie in it",
            "The Energizer Bunny was charged with battery",
            ""
        ]

    def getRandomPun(self):
        randNum = random.randrange(0, len(self.puns))
        return self.puns[randNum]
