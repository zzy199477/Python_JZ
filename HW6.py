
from enum import Enum
import numpy as np
import scr.SamplePathClass as PathCls
import scr.StatisticalClasses as Stat

class Game(object):
    def __init__(self, id, prob_head):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)
        self._probHead = prob_head
        self._countWins = 0

    def simulate(self, n_of_flips):

        count_tails = 0

        # flip the coin 20 times
        for i in range(n_of_flips):

            # in the case of flipping a heads
            if self._rnd.random_sample() < self._probHead:
                if count_tails >= 2:  # if the series is ..., T, T, H
                    self._countWins += 1  # increase the number of wins by 1
                count_tails = 0  # the tails counter needs to be reset to 0 because a heads was flipped

            # in the case of flipping a tails
            else:
                count_tails += 1  # increase tails count by one

    def get_reward(self):
        # calculate the reward from playing a single game
        return 100*self._countWins - 250


class SetOfGames:
    def __init__(self, prob_head, n_games):
        self._gameRewards = [] # create an empty list where rewards will be stored

        self._sumStat_Rewards = None
        # simulate the games
        for n in range(n_games):
            # create a new game
            game = Game(id=n, prob_head=prob_head)
            # simulate the game with 20 flips
            game.simulate(20)
            # store the reward
            self._gameRewards.append(game.get_reward())

        self._sumStat_Rewards=Stat.SummaryStat('Reward', self._gameRewards)

    def get_ave_reward(self):
        """ returns the average reward from all games"""
        return sum(self._gameRewards) / len(self._gameRewards)

    def get_probability_loss(self):
        """ returns the probability of a loss """
        count_loss = 0
        for value in self._gameRewards:
            if value < 0:
                count_loss += 1
        return count_loss / len(self._gameRewards)

    def get_reward_CI(self, alpha):
        return self._sumStat_Rewards.get_t_CI(alpha)

    def get_reward_PI(self, alpha):
        return self._sumStat_Rewards.get_PI(alpha)

# Q1
trial = SetOfGames(prob_head=0.5, n_games=1000)
print("The 95% CI of expected reward is:", trial.get_reward_CI(0.05))
print("The Probablity of loss is:", trial.get_probability_loss())

# Q2
#Interpretation: The true average expected rewards will be in the interval between -31.79 and -20.00 with probability 95%.
#The Probablity of loss is: 0.607

# Q3
# The casino owner who gets to play this game many times
A = SetOfGames(prob_head=0.5, n_games=100000)
print("The average expected reward is:", A.get_ave_reward())
print("The 95% CI of expected reward is:", A.get_reward_CI(0.05))
print("The Probablity of loss of A is:", A.get_probability_loss())
#Interpretation: The true average expected rewards will be in the interval between -25.33 and -24.13 with probability 95%.
#The uncertainty is relatively low because the game is repeated for many times
#The Probablity of loss is: 0.606

# A gambler who gets to play this game only 10 times
B = SetOfGames(prob_head=0.5, n_games=10)
print("The average expected reward is:", B.get_ave_reward())
print("The 95% CI of expected reward is:", B.get_reward_PI(0.05))
print("The Probablity of loss of B is:", B.get_probability_loss())
#Interpretation: The true average expected rewards will be in the interval between -227.50 and -50.00 with probability 95%
#The uncertainty is relatively higher because the game is only repeated for 10 times
#The Probablity of loss is: 0.800