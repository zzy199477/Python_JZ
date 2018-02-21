# import
import random


# Cointoss class to simulates the coin that can be flipped
class Cointoss:

    # The _ _init_ _ method initializes the upperside data attribute with 'Tails'.
    def __init__(self):
        self.upperside = 'Tails'

    # The tossing method generates a random number 1 and 0 using randint function.
    def tossing(self):
        if random.randint(0, 1) == 0:
            self.upperside = 'Tails'
        else:
            self.upperside = 'Heads'

    # The get_upperside method returns the value referenced by upperside.
    def get_upperside(self):
        return self.upperside


def main():
    store = []
    # Create an object from the Cointoss class.
    start_toss = Cointoss(20)

    # Object calling the function of class.
    print("This is upper side Before Toss :[", start_toss.get_upperside(), "]")

    print("........tossing the coin........")
    start_toss.tossing()

    # Object calling the function of class.
    print("Got the up side After Toss :[", start_toss.get_upperside(), "]")


# Call the main function.
main()