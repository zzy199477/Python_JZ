import HW4_Common as Cls

PROB = 0.4
TIME_STEPS = 20
Realization= 1000

myGame = Cls.Main(realization=Realization, prob=PROB)

myGame.simulate(TIME_STEPS)

print(myGame.get_ave_exp_cost())