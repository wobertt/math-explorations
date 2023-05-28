"""
CSCB36 Problem Set 1

Let i > 0. Let s be a binary string of length i. We define C(s) to be the number of odd parity1
substrings of s. We further define M (i) to be the maximum number of odd parity substrings
that a binary string of length i can have. I.e., M(i) is the maximum of C(s) over all binary
strings s of length i.
How is M(i) related to ai from part (a)? Prove your answer.
"""
import itertools
from math import ceil

# Best Results
def count_odd_fast(s: str): # O(n) time, O(1) space!
    prefix = 0
    is_odd = False
    for c in s:
        is_odd ^= (c == '1')
        prefix += is_odd
    return prefix * (len(s) - prefix + 1)


def find_max_odd_fast(n: int): # Proven!
    return ceil(n/2) * ceil((n+1)/2)


# Experimenting

def generate_binary_strings(n: int):
    return itertools.product('01', repeat=n)


def count_odd_slow(s: str): # O(n^2)
    ans = 0
    n = len(s)
    for i in range(n):
        counter = 0
        for j in range(i, n):
            counter += s[j] == '1'
            ans += counter % 2
    return ans



def find_max_odd(n: int): # O(2^n * count_odd(n))
    ans = 0
    for s in generate_binary_strings(n):
        ans = max(ans, count_odd_slow(s))
    return ans


def find_strings_with_count(n: int, cnt: int):
    for s in generate_binary_strings(n):
        if count_odd_slow(s) == cnt:
            print(''.join(s))


def main():
    N = 7
    mmap = {i*(N-i+1): i for i in range(0, (N+1)//2+1)}
    results = []
    print(mmap)

    for s in generate_binary_strings(N):
        ans = count_odd_slow(s)
        print(''.join(s), mmap[ans], ans)
        results.append(mmap[ans])
    # print(results[::2])
    # print(results[1::4])


main()
