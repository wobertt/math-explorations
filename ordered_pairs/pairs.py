"""
Define the ordered pair (a, b) as {{a}, {a, b}}.
Define the ordered triple (a, b, c) as (a, (b, c)).

Can you write (a, b, c) as a set?
What about (a, b, c, d)?

Remark: It is very easy to miss a bracket!
"""


def ordered_pair(a, b):
    return '{{ONE}, {ONE, TWO}}'.replace('ONE', a).replace('TWO', b)


print(ordered_pair('a', ordered_pair('b', 'c')))
print(ordered_pair('a', ordered_pair('b', ordered_pair('c', 'd'))))
