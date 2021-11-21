#master function for mean calculations
def mean(dlist):
    if isinstance(dlist, list):
        return sum(dlist) / len(dlist)
    else:
        return dlist

# master function for rate/proportion calculations
def rate(numerator, denominator, per, tenpower=False):
    if tenpower:
        return (numerator / denominator) * (10 ** per)
    else:
        return (numerator / denominator) * per

def r_diff(exposed, unexposed): # difference between two rates
    return exposed - unexposed

def r_ratio(exposed, unexposed): # ratio of two rates
    return exposed / unexposed

# estimates sum(person-time) for a population size and followup duration
def ptime(pop_size, duration):
    avg_pop = mean(pop_size)
    avg_dur = mean(duration)

    return avg_pop * avg_dur

#specialized rate/proportion functions

def incidence_p(onsets, at_risk, power=0): # can only be used for closed populations
    if isinstance(onsets, list):
        onsets = sum(onsets)
    if isinstance(onsets,):
        at_risk = sum(at_risk)
    return rate(onsets, at_risk, power, tenpower=True)

def incidence_r(onsets, time, power, s_onset=False, p_time=False, cohort=False): # calculates incidence rate specifically
    if p_time:
        time = ptime(time)
    if cohort:
        time = sum(time)
    if s_onset:
        onsets = sum(onsets)
    return rate(onsets, time, power, tenpower=True)

def prevalence(cases, individuals, power):
    if isinstance(cases, list):
        cases = sum(cases)
    if isinstance(individuals, list):
        individuals = len(individuals)
    return rate(cases, individuals, power, tenpower=True)