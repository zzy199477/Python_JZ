import scr.FormatFunctions as Format
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat
import Parameters as P

def print_comparative_outcomes(multi_cohort_fair, multi_cohort_unfair):

    #increase in reward
    increase = Stat.DifferenceStatIndp(
        name='Increase in mean reward',
        x=multi_cohort_fair.get_all_total_rewards(),
        y_ref=multi_cohort_unfair.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_PI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected increase in mean reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in reward
    relative_diff = Stat.RelativeDifferenceIndp(
        name='% increase in reward',
        x=multi_cohort_fair.get_all_total_rewards(),
        y_ref=multi_cohort_unfair.get_all_total_rewards()
    )
    # estimate and prediction interval
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_PI(alpha=P.ALPHA),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Expected percentage increase in mean reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)