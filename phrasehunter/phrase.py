from .character import Character

class Phrase(list):
    def __init__(self, phrs):
        super().__init__()
        if type(phrs) != str:
            raise TypeError("The phrase should be a string")
        else:
            for i in phrs:
                self.append(Character(i))

    def __repr__(self):
        return " ".join([str(i) for i in self])

    def guess(self, char):
        return True in [i.guess(char) for i in self]

    @property
    def all_guessed(self):
        g = [i.guessed for i in self]
        g = False if False in g else True
        return g

    def reset(self):
        for i in self:
            i.reset()