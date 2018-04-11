# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals

DELTA_T = 1       # years




TRANS_MATRIX_NoTreat = [
    [0.75, 0.15, 0, 0.1],
    [0, 0, 1, 0],
    [0, 0.25, 0.55, 0.2],
    [0, 0, 0, 1],
    ]

TRANS_MATRIX_AntiCo = [
    [0.75,  0.15,    0,    0.1],
    [0,     0,    1,    0],
    [0,     0.25,      0.55,   0.2],
    [0,     0,         0,      1],
    ]