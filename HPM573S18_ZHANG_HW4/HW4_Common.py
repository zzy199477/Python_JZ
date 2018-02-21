from enum import Enum
import numpy as np

class Flip(Enum):
    Head = 1
    Tail = 0

class Game(object):
    def __init__(self, id, prob):
        self._id = id
        self._prob = prob
        self._rnd = np.random
        self.outcome = []

    def simulate(self, flips):
        t = 0
        while t < flips:
            if self._rnd.sample() < self._prob:
                self.outcome.append(1)
            else:
                self.outcome.append(0)
            t += 1

    def get_outcome(self):
        return self.outcome

    def get_exp_cost(self):
        exp_cost = -250
        for i in range(len(self.outcome)-2):
            if self.outcome[i] == 0 and self.outcome[i+1] == 0 and self.outcome[i+2] == 1:
                    exp_cost += 100
        return exp_cost


class Main():
    def __init__(self, realization, prob):
        self._prob = prob
        self._realization = realization
        self.main = []
        self.expected_cost = []

        for i in range(realization):
            game = Game(i, prob)
            self.main.append(game)

    def simulate(self, flips):
        for game in self.main:
            game.simulate(flips)

    def get_ave_exp_cost(self):

        for game in self.main:
            value = game.get_exp_cost()
            self.expected_cost.append(value)
            ave_exp_cost = sum(self.expected_cost) / len(self.expected_cost)
        return ave_exp_cost

