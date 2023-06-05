"""
Q (from Nick Cheng): What's so special about the sequence of k values that are computed by this program?
How do these values relate to the input p and q?

Answer: The k values satisfy 1/k_1 + 1/k_2 + ... + 1/k_n = p/q.
"""
from math import ceil

"""
Precondition: p, q are natural numbers
Postcondition: The program terminates
"""
def div(p, q):
    sequence = []
    x, y = p, q
    while x > 0:
        k = ceil(y/x)
        x = x*k - y
        y = y*k
        sequence.append(k)
    return sequence



# Testing
M = int(input())
for i in range(1, M):
    for j in range(i, M):
        print(f'({i}, {j}): {div(i, j)}')