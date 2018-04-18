import InputData as Settings
import scr.FormatFunctions as F
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import scr.EconEvalClasses as Econ


def print_outcomes(simOutput, therapy_name):
    """ prints the outcomes of a simulated cohort
    :param simOutput: output of a simulated cohort
    :param therapy_name: the name of the selected therapy
    """
    # mean and confidence interval text of patient survival time
    survival_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of time to AIDS
    time_to_HIV_death_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_time_to_AIDS().get_mean(),
        interval=simOutput.get_sumStat_time_to_AIDS().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # mean and confidence interval text of discounted total cost
    cost_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_discounted_cost().get_mean(),
        interval=simOutput.get_sumStat_discounted_cost().get_t_CI(alpha=Settings.ALPHA),
        deci=0,
        form=F.FormatNumber.CURRENCY)

    # mean and confidence interval text of discounted total utility
    utility_mean_CI_text = F.format_estimate_interval(
        estimate=simOutput.get_sumStat_discounted_utility().get_mean(),
        interval=simOutput.get_sumStat_discounted_utility().get_t_CI(alpha=Settings.ALPHA),
        deci=2)

    # print outcomes
    print(therapy_name)
    print("  Estimate of mean survival time and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          survival_mean_CI_text)
    print("  Estimate of mean time to AIDS and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          time_to_HIV_death_CI_text)
    print("  Estimate of discounted cost and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          cost_mean_CI_text)
    print("  Estimate of discounted utility and {:.{prec}%} confidence interval:".format(1 - Settings.ALPHA, prec=0),
          utility_mean_CI_text)
    print("")


def report_CEA_CBA(simOutputs_none, simOutputs_anticog):


    # define two strategies
    none_therapy_strategy = Econ.Strategy(
        name='none Therapy',
        cost_obs=simOutputs_none.get_costs(),
        effect_obs=simOutputs_none.get_utilities()
    )
    anticog_therapy_strategy = Econ.Strategy(
        name='anticog Therapy',
        cost_obs=simOutputs_anticog.get_costs(),
        effect_obs=simOutputs_anticog.get_utilities()
    )

    # CEA
    if Settings.PSA_ON:
        CEA = Econ.CEA(
            strategies=[none_therapy_strategy, anticog_therapy_strategy],
            if_paired=True
        )
    else:
        CEA = Econ.CEA(
            strategies=[none_therapy_strategy, anticog_therapy_strategy],
            if_paired=False
        )
    # show the CE plane
    CEA.show_CE_plane(
        title='Cost-Effectiveness Analysis',
        x_label='Additional discounted utility',
        y_label='Additional discounted cost',
        show_names=True,
        show_clouds=True,
        show_legend=True,
        figure_size=6,
        transparency=0.3
    )
    # report the CE table
    CEA.build_CE_table(
        interval=Econ.Interval.CONFIDENCE,
        alpha=Settings.ALPHA,
        cost_digits=0,
        effect_digits=2,
        icer_digits=2,
    )

    # CBA
    if Settings.PSA_ON:
        NBA = Econ.CBA(
            strategies=[none_therapy_strategy, anticog_therapy_strategy],
            if_paired=True
        )
    else:
        NBA = Econ.CBA(
            strategies=[none_therapy_strategy, anticog_therapy_strategy],
            if_paired=False
        )
    # show the net monetary benefit figure
    NBA.graph_deltaNMB_lines(
        min_wtp=0,
        max_wtp=50000,
        title='Cost-Benefit Analysis',
        x_label='Willingness-to-pay for one additional QALY ($)',
        y_label='Incremental Net Monetary Benefit ($)',
        interval=Econ.Interval.CONFIDENCE,
        show_legend=True,
        figure_size=6
    )
