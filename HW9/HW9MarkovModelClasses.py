import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import scr.RandomVariantGenerators as rndClasses
import scr.EconEvalClasses as EconCls
import HW9ParameterClasses as P
import HW9InputData as Data


class Patient:
    def __init__(self, id, parameters):
        """ initiates a patient
        :param id: ID of the patient
        :param parameters: parameter object
        """

        self._id = id
        # random number generator for this patient
        self._rng = None
        # parameters
        self._param = parameters
        # state monitor
        self._stateMonitor = PatientStateMonitor(parameters)
        # simulation time step
        self._delta_t = parameters.get_delta_t()
        self._stroke = 0

    def simulate(self, sim_length):
        """ simulate the patient over the specified simulation length """

        # random number generator for this patient
        self._rng = rndClasses.RNG(self._id)

        k = 0  # current time step

        # while the patient is alive and simulation length is not yet reached
        while self._stateMonitor.get_if_alive() and k*self._delta_t < sim_length:

            # find the transition probabilities of the future states
            trans_probs = self._param.get_transition_prob(self._stateMonitor.get_current_state())
            # create an empirical distribution
            empirical_dist = rndClasses.Empirical(trans_probs)
            # sample from the empirical distribution to get a new state
            # (returns an integer from {0, 1, 2, ...})
            new_state_index = empirical_dist.sample(self._rng)

            # update health state
            self._stateMonitor.update(k, P.HealthStats(new_state_index))

            # increment time step
            k += 1

    def get_survival_time(self):
        """ returns the patient's survival time"""
        return self._stateMonitor.get_survival_time()

    def get_stroke(self):

        return self._stateMonitor.get_stroke()


class PatientStateMonitor:
    """ to update patient outcomes (years survived, cost, etc.) throughout the simulation """
    def __init__(self, parameters):
        """
        :param parameters: patient parameters
        """
        self._currentState = parameters.get_initial_health_state() # current health state
        self._delta_t = parameters.get_delta_t()    # simulation time step
        self._survivalTime = 0          # survival time
        self._timeToAIDS = 0        # time to develop AIDS
        self._stroke = ()


    def update(self, k, next_state):
        """
        :param k: current time step
        :param next_state: next state
        """

        # if the patient has died, do nothing
        if not self.get_if_alive():
            return

        # update survival time
        if next_state in [P.HealthStats.Dead]:
            self._survivalTime = (k+0.5)*self._delta_t  # corrected for the half-cycle effect


        if self._currentState == P.HealthStats.Stroke:
            self._stroke.append(1)
        else:
            self._stroke.append(0)


        # update current health state
        self._currentState = next_state

    def get_if_alive(self):
        result = True
        if self._currentState in [P.HealthStats.Dead]:
            result = False
        return result

    def get_current_state(self):
        return self._currentState

    def get_survival_time(self):
        """ returns the patient survival time """
        # return survival time only if the patient has died
        if not self.get_if_alive():
            return self._survivalTime
        else:
            return None

    def get_stroke(self):
        return sum(self._stroke)

