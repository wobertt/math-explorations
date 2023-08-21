import math
import random
import statistics


def g(u, l): # Inverse CDF Transformation for Exp(l) variable
    assert 0 <= u < 1
    return -1/l * math.log(1-u)


def simulate(g, l):
    return g(random.random(), l)


def simulate_conditional(x=None):
    if x is None:
        x = simulate(g, L)
    return simulate(g, 1/x)


def get_samples(num_samples):
    # return [simulate(g, L) for _ in range(num_samples)]
    # return [simulate_conditional() for _ in range(num_samples)]
    return [simulate_conditional(x=0.5) for _ in range(num_samples)]


def estimate_stats(num_samples):
    samples = get_samples(num_samples)

    ev = statistics.mean(samples)
    variance = statistics.variance(samples)
    print(f"EV: {ev}, Variance: {variance}")


if __name__ == '__main__':
    L = 1
    estimate_stats(1000000)