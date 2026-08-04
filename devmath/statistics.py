"""
devmath.statistics
Statistical and probability functions.
"""

import math
import statistics as stats


# ==========================
# CENTRAL TENDENCY
# ==========================

def mean(data):
    return stats.mean(data)


def median(data):
    return stats.median(data)


def mode(data):
    return stats.mode(data)


def multimode(data):
    return stats.multimode(data)


def geometric_mean(data):
    return stats.geometric_mean(data)


def harmonic_mean(data):
    return stats.harmonic_mean(data)


# ==========================
# DISPERSION
# ==========================

def variance(data):
    return stats.variance(data)


def population_variance(data):
    return stats.pvariance(data)


def standard_deviation(data):
    return stats.stdev(data)


def population_standard_deviation(data):
    return stats.pstdev(data)


def data_range(data):
    return max(data) - min(data)


def coefficient_of_range(data):
    return (max(data) - min(data)) / (max(data) + min(data))


# ==========================
# QUARTILES
# ==========================

def quartiles(data):
    data = sorted(data)
    n = len(data)

    q2 = median(data)

    if n % 2 == 0:
        lower = data[:n//2]
        upper = data[n//2:]
    else:
        lower = data[:n//2]
        upper = data[n//2+1:]

    q1 = median(lower)
    q3 = median(upper)

    return q1, q2, q3


def interquartile_range(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1


# ==========================
# PERCENTILES
# ==========================

def percentile(data, p):
    data = sorted(data)
    index = (len(data) - 1) * (p / 100)

    lower = math.floor(index)
    upper = math.ceil(index)

    if lower == upper:
        return data[int(index)]

    return (
        data[lower] +
        (data[upper] - data[lower]) *
        (index - lower)
    )


# ==========================
# Z SCORE
# ==========================

def z_score(value, data):
    return (
        value - mean(data)
    ) / standard_deviation(data)


# ==========================
# COVARIANCE
# ==========================

def covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must have the same length.")

    mx = mean(x)
    my = mean(y)

    total = 0

    for a, b in zip(x, y):
        total += (a - mx) * (b - my)

    return total / (len(x) - 1)


# ==========================
# CORRELATION
# ==========================

def correlation(x, y):
    return covariance(x, y) / (
        standard_deviation(x) *
        standard_deviation(y)
    )


# ==========================
# SIMPLE LINEAR REGRESSION
# ==========================

def linear_regression(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must have equal length.")

    mx = mean(x)
    my = mean(y)

    numerator = 0
    denominator = 0

    for xi, yi in zip(x, y):
        numerator += (xi - mx) * (yi - my)
        denominator += (xi - mx) ** 2

    slope = numerator / denominator
    intercept = my - slope * mx

    return slope, intercept


def predict(x_value, slope, intercept):
    return slope * x_value + intercept


# ==========================
# PROBABILITY
# ==========================

def factorial(n):
    return math.factorial(n)


def permutations(n, r):
    return math.perm(n, r)


def combinations(n, r):
    return math.comb(n, r)


def probability(success, total):
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")
    return success / total


def odds(success, failure):
    return success / failure


# ==========================
# DISTRIBUTIONS
# ==========================

def normal_pdf(x, mean_value=0, std=1):
    return (
        1 /
        (std * math.sqrt(2 * math.pi))
    ) * math.exp(
        -((x - mean_value) ** 2) /
        (2 * std ** 2)
    )


def binomial_probability(n, k, p):
    return (
        math.comb(n, k) *
        (p ** k) *
        ((1 - p) ** (n - k))
    )


def poisson_probability(lam, k):
    return (
        math.exp(-lam) *
        lam ** k /
        math.factorial(k)
    )


# ==========================
# RANDOM HELPERS
# ==========================

def expected_value(values, probabilities):
    if len(values) != len(probabilities):
        raise ValueError("Length mismatch.")

    total = 0

    for v, p in zip(values, probabilities):
        total += v * p

    return total