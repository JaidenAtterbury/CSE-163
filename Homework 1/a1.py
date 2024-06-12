"""
Jaiden Atterbury
CSE 163 AD
04/01/23

Implements the functions for Startup. These functions are funky_sum, total,
and swip_swap.
"""


def funky_sum(a: float, b: float, mix: float) -> float:
    """
    Takes in numbers a, b, and mix, where a and b are numbers to be added
    together, and mix is a number used to determine the relative amount to
    use from a and from b. If mix is 0 or less, the function returns a. If
    mix is 1 or more, the function returns b. For any value of mix between
    0 and 1, the function returns a weighted average of a and b of the form:
    (1 - mix) * a + mix * b.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n: int) -> int | None:
    """
    Takes in an integer n and returns the sum of the integers from 0 to n,
    both inclusive. If n is negative, the function should return None
    instead.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source: str, c1: str, c2: str) -> str:
    """
    Takes in a string named source and characters c1 and c2 and returns a copy
    of source with all occurrences of c1 and c2 being swapped.
    """
    final = ""
    for char in source:
        if char == c1:
            final += c2
        elif char == c2:
            final += c1
        else:
            final += char
    return final
