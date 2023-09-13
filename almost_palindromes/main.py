'''
CMU 21-228 Discrete Mathematics A1

Q: A 4-digit number is called a palindrome if it is the same when the digits are read in reverse.
For example, 7337 and 3333 are 4-digit palindromes, but 1337 and 0990 are not. Note that
0990 doesn’t count because it’s actually a 3-digit number.
A 4-digit number is called an almost-palindrome if there is a way to change exactly one digit
so that the result is a 4-digit palindrome. For example, 1337, 1501, and 1990 are 4-digit
almost-palindromes (they could become 1331 or 7337, 1001 or 1551, and 1991), but 1234,
0991, and 1331 are not. The issue with 0991 is again that it is actually a 3-digit number, and
the issue with 1331 is that if you change any digit, then it becomes a non-palindrome.
How many 4-digit almost-palindromes are there?

A: All four-digit numbers are of the form WXYZ, where W, X, Y, Z are digits and W ≠ 0.
WXYZ is an almost-palindrome iff (1) W=Z and X≠Y, or (2) W≠Z and X=Y.

(1) There are 9 choices for W=Z and 90 choices for X≠Y, so there are 9*90 = 810 total.
(2) If Z = 0, there are 9 choices for W and 10 choices for X=Y.
    If Z ≠ 0 (9 choices), there are 8 choies for W and 10 choices for X=Y.
    So, there are 9*10 + 9*8*10 = 810 total.

This gives 810+810 = 1620 4-digit almost-palindromes.
'''

ALPHABET = '0123456789'


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_almost_palindrome(s: str) -> bool:
    for idx, current_letter in enumerate(s):
        for substituted_letter in ALPHABET:
            if current_letter == substituted_letter:
                continue
            if is_palindrome(s[:idx] + substituted_letter + s[idx+1:]):
                return True
    return False


def main():
    counter = 0
    for num in map(str, range(1000, 9999)):
        if is_almost_palindrome(num):
            print(num)
            counter += 1
    print("Total:", counter)


main()