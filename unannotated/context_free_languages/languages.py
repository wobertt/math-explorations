import re


def count_substrings_with_overlap(substring: str, string: str) -> int:
    return len(re.findall(f'(?={substring})', string))


def ps4_q2_exact(s: str) -> bool:
    return count_substrings_with_overlap('010', s) == count_substrings_with_overlap('110', s)


def final_f2022_l7(s: str) -> bool:
    return 2 * s.count('0') == s.count('1') + 1


def ps4_q2_crunchy(s: str) -> bool:
    return count_substrings_with_overlap('010', s) == count_substrings_with_overlap('101', s)


def extra_101(s: str) -> bool:
    return count_substrings_with_overlap('010', s) == count_substrings_with_overlap('101', s) - 1