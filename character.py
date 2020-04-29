# Create your Character class logic in here.
class Character:
    def __init__(self, char):
        try:
            if len(char) != 1:
                raise ValueError("The value should be a single letter.")
        except TypeError as err:
            print("{}: You should input a letter.".format(err))
        else:
            self.char = str(char)
            self.reset()

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.guessed:
            return self.char
        else:
            return "_"

    def __add__(self, other):
        return  str(self) + str(other)

    def __radd__(self, other):
        return str(other) + str(self)

    def guess(self, char):
        if self.char.lower() == char.lower():
            self.guessed = True
            return True
        else:
            return False

    def reset(self):
        self.guessed = True if self.char == " " else False  