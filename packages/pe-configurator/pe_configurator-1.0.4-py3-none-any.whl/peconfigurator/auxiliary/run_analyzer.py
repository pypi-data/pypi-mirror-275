#!/usr/bin/env python
import numpy as np


def sigmoid(support,c1=0.03):
    """Completely arbitrary sigmoid function to give empirically reasonable new bounds

    Args:
        support (float): The support in percent of the edge bin
        c1 (float, optional): Controls the steepness of the sigmoid. Defaults to 0.03.

    Returns:
        [float]: The value of the sigmoid
    """
    return 0.66/(1+np.exp(-c1*(support-30)))

def new_bound(params,support,lower=True):
    if lower:
        return  (1-sigmoid(support))*params
    else:
        return  (1+sigmoid(support))*params

def railing_check(samples, Nbin, tolerance,label,input_min_edge=None):
    """
    Taken from LAPLACE: https://git.ligo.org/tsun-ho.pang/lalinference-pe-result-sanity-check
    Check if the posterior is railing against the prior
    by checking if the bins at the bound has a support higher
    than tolerance * the support of the most supported bin

    args:
        samples (np.array): Posterior samples to be checked
        Nbin (int or np.array): Number of bins or edges of the bins to be used in the histogram
        tolerance (float): Tolerance at which the railing below it is accepted

    return:
        low_end_railing (boolean): If the samples are railing against the lower end
        high_end_railing (boolean): If the samples are railing against the higher end
    """
    hist, bin_edges = np.histogram(samples, bins=Nbin, density=True)

    highest_hist = np.amax(hist)
    lower_support = hist[0] / highest_hist * 100
    higher_support = hist[-1] / highest_hist * 100

    low_end_railing = lower_support > tolerance
    high_end_railing = higher_support > tolerance
    if label == "mass_ratio":
        # No upper bound railing for q, since q=1 is an actual boundary
        high_end_railing = False

    prior_bound_low = None
    prior_bound_high = None
    recommendation = ""
    if low_end_railing:
        # We are railing at the low end
        # If there is a lot of support, ask for much wider priors, otherwise ask for
        # modestly wider priors
        min_edge = np.round(np.amin(samples),4)
        prior_bound_low = np.round(new_bound(min_edge,lower_support,lower=True),4)
        recommendation += f"Railing at lower end at {min_edge}. Suggested new bound is {prior_bound_low}. "
        # Following is to avoid false positives for distance low railing
        if input_min_edge is not None:
            if input_min_edge < prior_bound_low:
                low_end_railing = False
                prior_bound_low = None
                recommendation = ""
                
    if high_end_railing:
        max_edge = np.round(np.amax(samples),4)
        prior_bound_high = np.round(new_bound(max_edge,lower_support,lower=False),4)
        recommendation += f"Railing at higher end at {max_edge}. Suggested new bound is {prior_bound_high}"

    return low_end_railing, high_end_railing, recommendation, (prior_bound_low,prior_bound_high)


def NS_check(samples,alert=False):
    """
    Check if the run might have 1 or 2 neutron stars. This is just defined
    as having support for component masses below 3 solar masses

    Args:
        samples (array-like): The samples
    """
    m1 = samples["mass_1"]
    m2 = samples["mass_2"]
    m1_low = np.percentile(m1, 5)
    m2_low = np.percentile(m2, 5)
    m1_med = np.percentile(m1, 50)
    m2_med = np.percentile(m2, 50)
    message = []
    if m1_low < 3 and m1_med > 3:
        message.append("Mass 1 has minor support for mass < 3 $M_{\\odot}$")
    elif m1_med < 3:
        message.append("Mass 1 has strong support for mass < 3  $M_{\\odot}$")

    if m2_low < 3 and m2_med > 3:
        if message is not None:
            message.append("Mass 2 has minor support for mass < 3 $M_{\\odot}$")
        else:
            message.append("Mass 2 has minor support for mass < 3 $M_{\\odot}$")
    elif m2_med < 3:
        if message is not None:
            message.append("Mass 2 has strong support for mass < 3 $M_{\\odot}$")
        else:
            message.append("Mass 2 has strong support for mass < 3 $M_{\\odot}$")

    is_BNS = False
    if m1_med < 3 and m2_med < 3:
        is_BNS = True
        message.append("This is likely a binary neutron star system! Note: `ell_max` was set to 2.")
    if alert:
        return message,is_BNS

    return message

def NSBH_check(samples, seglen):
    """
    Check if the run is consistent with an NSBH system.

    Args:
        samples (array-like): The samples
    """
    m1 = samples["mass_1"]
    m2 = samples["mass_2"]
    m1_low = np.percentile(m1, 5)
    m2_low = np.percentile(m2, 5)
    m1_med = np.percentile(m1, 50)
    m2_med = np.percentile(m2, 50)
    message = []

    if m2_low < 3 and m1_low > 5:
        if seglen < 128:
            message.append("System is compatible with NSBH binary.")
        else:
            message.append("<span style='color:red'>WARNING: System is compatible with NSBH binary and estimated seglen >= 128. If analyzing with NSBH model, consider setting ell_max to 2")
    elif m2_med < 3 and m1_med > 5:
        if seglen < 128:
            message.append("System has minor support for NSBH binary.")
        else:
            message.append("<span style='color:red'>WARNING: System has minor support for NSBH binary and estimated seglen >= 128. If analyzing with NSBH model, consider setting ell_max to 2")
    
    return message

def highmass_check(samples, alert=False, enforce_ellmax=False):
    """
    Check if the total mass is high enough that it would be worth to run with the (4,4) mode in band and with the (4,4) RD well-resolved.

    Args:
        samples (array-like): The samples
    """
    mtot = samples["total_mass"]
    mtot_med = np.percentile(mtot, 50)
    message = []
    is_highmass = False
    if mtot_med > 200.0:
        is_highmass = True
        if enforce_ellmax:
            message.append("<span style='color:red'>Total mass has strong support above 200 $M_{\\odot}$!Consider to set ell_max to 4 for the analysis, or to disable --enforce_ellmax.</span>")
        else:
            message.append("<span style='color:red'>Total mass has strong support above 200 $M_{\\odot}$! Note: ell_max was set to 4.</span>")
    if alert:
        return message,is_highmass    

    return message


def SNR_threshold(samples, th_low=8.0, th_high=25.0):
    """Check if the network SNR is lower than some threshold.
    This is intended for very special cases where we somehow
    miss the signal.

    Args:
        samples (array-like): The samples
    """
    snr = samples["network_matched_filter_snr"]
    median_snr = np.median(snr)
    message = []
    if median_snr < th_low:
        message.append(f"The median network matched filter SNR is below {th_low}. Is the signal being found?")
    if median_snr > th_high:
        message.append(
            f"The median network matched filter SNR is above {th_high}! Very loud event?"
        )
    return message


def spin_checks(samples):
    """Perform several checks on the spin parameters
    1. Confidently bound a1 or a2 away from 0 or measure them very well.
    2. Confidently bound chi_eff from 0, check if it's largely +ve/-ve
    3. Confidently bound chi_p away from 0, or measure very well
    Args:
        samples (array-like): The samples
    """
    a1 = samples['a_1']
    a2 = samples['a_2']
    chi_eff = samples['chi_eff']
    chi_p = samples['chi_p']
    a1_low = np.percentile(a1,5)
    a1_high = np.percentile(a1,95)
    a1_width = a1_high-a1_low
    a2_low = np.percentile(a2,5)
    a2_high = np.percentile(a2,95)
    a2_width = a2_high-a2_low

    chi_eff_med = np.median(chi_eff)
    chi_p_med = np.median(chi_p)
    message=[]
    if a1_width<0.4:
        message.append(r"$a_{1}$ is well constrained!")
    if a2_width<0.4:
        message.append(r"$a_{2}$ is well constrained!")
    if chi_eff_med < -0.1:
        message.append(r"The median $\chi_{\rm eff}<-0.1$!")
    elif chi_eff_med > 0.3:
        message.append(r"The median $\chi_{\rm eff}>0.3$!")
    if chi_p_med > 0.6:
        message.append(r"The median $\chi_{p}>0.6$, highly precessing event?")

    return message

def mass_ratio_checks(samples):
    """Perform various checks on mass ratio

    Args:
        samples (array-like): The samples
    """
    mass_ratio = samples["mass_ratio"]

    # Checks on the 90% confidence
    low = np.percentile(mass_ratio, 5)
    high = np.percentile(mass_ratio, 95)
    med = np.percentile(mass_ratio,50)
    message=[]
    if high < 0.9:
        message.append("Equal masses are excluded at high confidence for this event!")
    if med<1./3:
        message.append("Median mass ratio is below 1/3, highly unequal mass event!")
    return message

def distance_checks(samples, th_low=150, th_high=5000):
    """Perform various checks on the distance. In particular, is the distance
    is very small or very large

    Args:
        samples (array-like): The samples
    """
    # Distance in Mpc
    dist = samples["luminosity_distance"]
    median_dist = np.median(dist)
    message = []
    if median_dist < th_low:
        message.append(f"The median luminosity distance is below {th_low} Mpc!")
    elif median_dist > th_high:
        message.append(f"The median luminosity distance is above {th_high} Mpc!")
    return message


def theta_JN_checks(samples):
    """Perform check on inclination. In particular, highlight if the inclination
    is close to edge-on

    Args:
        samples (array-like): Samples
    """
    theta_JN = samples["theta_jn"]
    # Is the inclination closer to edge-on than face-on?
    # theta_JN is usually bi-modal, kde the data, find the peaks and check
