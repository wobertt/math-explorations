"""
Let A_n be the set of languages over the alphabet {0, 1} where the longest string has length n.
For any L in A_n, let m(L) be the minimum number of states needed in a DFSA that accepts L.

Q: What is the maximum value of m(L) over all possible languages L in A_n?
"""

import itertools as it
import more_itertools as mit


def generate_strings(max_length):
    return it.chain.from_iterable((it.product('01', repeat=i) for i in range(0, max_length+1)))


def generate_An(n):
    non_max_strings = generate_strings(n-1)
    max_strings = it.product('01', repeat=n)

    non_max_langs = mit.powerset(non_max_strings)
    max_langs = mit.powerset(max_strings)
    next(max_langs) # skip empty set 

    lang_product = it.product(list(non_max_langs), list(max_langs))
    return (it.chain(non_max_lang, max_lang) for non_max_lang, max_lang in lang_product)


def count_equivalence_classes(lang, n):
    postfixes = {s: set() for s in generate_strings(n)}
    for s in lang:
        for prefix_length in range(0, len(s)+1):
            prefix, postfix = s[:prefix_length], s[prefix_length:]
            postfixes[prefix].add(postfix)
    
    equivalence_classes = set(frozenset(postfix_set) for postfix_set in postfixes.values())
    equivalence_classes.add(frozenset())
    return len(equivalence_classes)


def print_language(lang, n):
    print(*[''.join(s).__repr__() for s in lang])


def get_worst_case(n):
    worst_case = 0
    prev = 0
    for lang in generate_An(n):
        worst_case = max(worst_case, count_equivalence_classes(lang, n))
        if worst_case != prev:
            print(worst_case)
        prev = worst_case
    return worst_case


def main():
    n = 2
    for lang in generate_An(n):
        lang = list(lang)
        print_language(lang, n)
        print(count_equivalence_classes(lang, n))
    

def test_00_11():
    n = 2
    lang = (('0', '0'), ('1', '1'))
    print_language(lang, n)
    print(count_equivalence_classes(lang, n))


if __name__ == '__main__':
    # main()
    for i in range(1, 10):
        print(i, get_worst_case(i))
