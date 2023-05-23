"""
The Apocalypse: In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or
else they face massive fines. If all families abide by this policy-that is, they have continue to have
children until they have one girl, at which point they immediately stop-what will the gender ratio
of the new generation be? (Assume that the odds of someone having a boy or a girl on any given
pregnancy is equal.)
"""

"""
Answer:
The expected ratio is 1:1.

But how? Every family stops on a girl!

Consider each childbirth in isolation: the ratio is clearly 1:1. Stopping on a girl has no effect - there is no way to change this ratio!

Alternatively, we can compute the expected # of boys before the 1st girl, with the same result.
"""

import random

NUM_SIMULATIONS = 1000
NUM_FAMILIES = 1000


def simulate(num_families):
    boys = 0
    girls = 0
    for _ in range(NUM_FAMILIES):
        while True:
            if random.choice(['boy', 'girl']) == 'girl':
                girls += 1
                break
            boys += 1

    print(f'The ratio is {boys}:{girls} = {boys/girls:.4f}')
    return boys/girls


results = [simulate(NUM_FAMILIES) for _ in range(NUM_SIMULATIONS)]
print(f'The average ratio over all simulations is {sum(results)/NUM_SIMULATIONS:.4f}.')