import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

def print_comparative_outcomes(sim_output_fair, sim_output_unfair):

    # increase in reward
    increase = Stat.DifferenceStatIndp(
        name='Increase in reward',
        x=sim_output_fair.get_reward(),
        y_ref=sim_output_unfair.get_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average increase in reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in reward
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in reward',
        x=sim_output_fair.get_reward(),
        y_ref=sim_output_unfair.get_reward()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=relative_diff.get_mean(),
        interval=relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage increase in reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

