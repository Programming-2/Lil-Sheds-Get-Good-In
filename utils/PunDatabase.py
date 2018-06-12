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
            "You’re becoming a vegetarian? I think that’s a big missed steak",
            "Velcros are just a big rip-off",
            "I wanna make a joke about sodium, but Na",
            "I’m reading a book about anti-gravity. It’s impossible to put down!",
            "How did the picture end up in jail? It was framed!",
            ""
            ""
        ]

    def getRandomPun(self):
        randNum = random.randrange(0, len(self.puns))
        return self.puns[randNum]
