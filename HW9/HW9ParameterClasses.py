from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import HW9InputData as Data
import scr.HW9MarkovModelClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients"""
    Well = 0
    Stroke = 1
    PostStroke = 2
    Dead = 3


class Therapies(Enum):
    """ No treatment vs. anticoagulation therapy """
    NoTreat = 0
    AntiCo = 1


class Parameters():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.Well

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        if self._therapy == Therapies.NoTreat:
            self._prob_matrix = Data.TRANS_MATRIX_NoTreat
        else:
            self._prob_matrix = Data.TRANS_MATRIX_AntiCo

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

