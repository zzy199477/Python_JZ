import Parameters as P
import Classes as Cls
import SupportTransientState as Support

multiCohortFair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),
    prob_head=P.PROB_HEAD_FAIR,
    n_games_in_a_set=P.REAL_GAME_SIZE)

multiCohortFair.simulation()

multiCohortUnfair = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS, 2*P.NUM_SIM_COHORTS),
    prob_head=P.PROB_HEAD_UNFAIR,
    n_games_in_a_set=P.REAL_GAME_SIZE)

multiCohortUnfair.simulation()

Support.print_comparative_outcomes(multiCohortFair, multiCohortUnfair)
