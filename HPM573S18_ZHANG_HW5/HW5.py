import HW4Solution as La
import scr.FigureSupport as Fig


myGame = La.SetOfGames(prob_head=0.5, n_games=1000)

print(myGame.get_minimum())
print(myGame.get_maximum())
print(myGame.get_set_rewards())

Fig.graph_histogram(
    observations=myGame.get_set_rewards(),
    title='Histogram of Rewards',
    x_label='Rewards',
    y_label='Count of Flips')


import HW4Solution as La
myGame = La.SetOfGames(prob_head=0.5, n_games=1000)
print(myGame.get_loss())
proportion_of_times = myGame.get_loss()/1000
print(proportion_of_times)