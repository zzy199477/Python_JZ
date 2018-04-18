import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating none therapy
# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.none)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# simulating combination therapy
# create a cohort
cohort_anticog = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.anticog)
# simulate the cohort
simOutputs_anticog = cohort_anticog.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_anticog)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_none, "None Therapy:")
SupportMarkov.print_outcomes(simOutputs_anticog, "Anticog Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticog)

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticog)
