import Parameters as P
import Classes as Cls
import SupportSteadyState as Support

cohortFair = Cls.SetOfGames(
    id=1,
    prob_head=P.PROB_HEAD_FAIR,
    n_games=P.SIM_GAME)

fairOutcome = cohortFair.simulation()

cohortUnfair = Cls.SetOfGames(
    id=2,
    prob_head=P.PROB_HEAD_UNFAIR,
    n_games=P.SIM_GAME)

unfairOutcome = cohortUnfair.simulation()

Support.print_comparative_outcomes(fairOutcome, unfairOutcome)
