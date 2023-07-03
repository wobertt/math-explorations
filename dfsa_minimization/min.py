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
    # non_max_strings = generate_strings(n-1)
    non_max_strings = it.product('01', repeat=n-1)
    max_strings = it.product('01', repeat=n)

    non_max_langs = mit.powerset(non_max_strings)
    max_langs = mit.powerset(max_strings)
    next(max_langs) # skip empty set 

    lang_product = it.product(non_max_langs, max_langs)
    return (it.chain(non_max_lang, max_lang) for non_max_lang, max_lang in lang_product)


def count_equivalence_classes(lang, n, output=False):
    postfixes = {s: set() for s in generate_strings(n)}
    for s in lang:
        for prefix_length in range(0, len(s)+1):
            prefix, postfix = s[:prefix_length], s[prefix_length:]
            postfixes[prefix].add(postfix)
    
    equivalence_classes = set(frozenset(postfix_set) for postfix_set in postfixes.values())
    equivalence_classes.add(frozenset())

    if output:
        for prefix, postfix_set in postfixes.items():
            print("Prefix:", ''.join(prefix).__repr__())
            print_language(postfix_set)

    return len(equivalence_classes)


def print_language(lang):
    print(*[''.join(s).__repr__() for s in lang])


def get_worst_case(n):
    worst_case = 0
    prev = 0
    for lang in generate_An(n):
        lang = list(lang)
        worst_case = max(worst_case, count_equivalence_classes(lang, n))
        if worst_case != prev:
            print(n, worst_case)
            print_language(lang)
        prev = worst_case
    return worst_case


def get_worst_cases_up_to(n):
    for i in range(1, n):
        print(i, get_worst_case(i))
    

def test():
    lang = (
        '0000', '00000', '00001', '00010', '00011', '0010', '00100', '00110', '0100', '01001', '01011', '01100', '10001', '10110', '11011', '11100', '11101'
    )

    lang = tuple('0'+s for s in lang) + tuple('1'+s for s in lang) + tuple('1'+''.join(s) for s in it.product('01', repeat=3))

    lang = tuple(tuple(s) for s in lang)
    n = max(len(s) for s in lang)

    print(count_equivalence_classes(lang, n, output=True))


"""
Worst cases:
n=4 (15):
lang = ('000', '0010', '010', '0100', '0111', '100', '1001', '1010', '1011', '110', '1100', '1101')

n=5 (23):
lang = ('0000', '00000', '00001', '00010', '00011', '0010', '00100', '00110', '0100', '01001', '01011', '01100', '10001', '10110', '11011', '11100', '11101')

n=6 (39):
'00000' '10010' '1001' '1010' '100110' '000000' '011011' '101100' '001011' '010001' '011100' '000011' '1110' '100010' '101011' '1000' '1101' '100001' '10000' '000110' '00010' '100100' '111011' '111101' '000010' '110001' '00100' '10100' '001001' '1011' '110110' '100000' '000001' '1100' '101001' '011101' '001100' '111100' '010110' '1111' '000100' '100011'
"""

if __name__ == '__main__':
    test()
    # get_worst_case(5)
    # get_worst_cases_up_to(5)
    
