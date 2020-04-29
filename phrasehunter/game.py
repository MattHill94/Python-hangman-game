import random
from .phrase import Phrase
import string 

class Game(list):
    def __init__(self, *args):
        super().__init__()
        for phrs in args:
            self.append(Phrase(phrs))
        self.active = random.choice(self)
        self.life = 5
        self.choices_made = set()

    def reset(self):
        self.life = 5
        self.active.reset()
        self.active = random.choice(self)
        self.choices_made = set()

    def main_loop(self):    
        while self.life:    
            print(self.active)
            choice = input("Choose a letter for the phrase: ")
            if choice.upper() not in string.ascii_uppercase:
                print("The choice must be a letter (a-z)")
            elif len(choice) > 1:
                print("The choice must be a single letter")
            else:
                if choice not in self.choices_made:
                    self.choices_made.add(choice)
                    if self.active.guess(choice):
                        print("You guessed right!")
                        if self.active.all_guessed:
                            print(self.active)
                            again = input("You win!, do you want to play again? (y) yes / (n) no : ")
                            if again.lower() == "y":
                                self.reset()
                            if again.lower() == "n":
                                print("Thanks for playing!")
                                break
                    else:
                        self.life -= 1
                        print("You chose wrong. You have {} out of 5 lives remaining!".format(self.life))
                        if 0 == self.life:
                            again = input("You lose!, want to play again? (y) yes / (n) no : ")
                            if again.lower() == "y":
                                self.reset()
                            if again.lower() == "n":
                                print("Thanks for playing!")
                                break
                else:
                    print("You can't repeat your choice.")


    

        

