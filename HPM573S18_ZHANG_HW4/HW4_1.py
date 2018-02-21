import random

class Game:
    def __init__(self):
        self.upperside = 'Tails'

    def simulate(self):
        if random.randint(0, 1) == 0:
            self.upperside = 'Tails'
        else:
            self.upperside = 'Heads'

    def get_upperside(self):
         return self.upperside


def main():
    # Create an object from the Cointoss class.
    start_toss = Game()

    # Object calling the function of class.
    print("This is upper side Before Toss :[", start_toss.get_upperside(), "]")

    print("........tossing the coin........")
    start_toss.tossing()

    # Object calling the function of class.
    print("Got the up side After Toss :[", start_toss.get_upperside(), "]")


main()
