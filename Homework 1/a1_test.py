"""
Jaiden Atterbury
CSE 163 AD
04/01/23

Tests the functions for Startup. In particular, tests the functions in a1.py.
"""

import a1

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the functionality of the function in a1.py named total.
    """
    # The regular case
    assert_equals(15, a1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, a1.total(1))
    assert_equals(0, a1.total(0))
    # TODO: add your own total test here
    assert_equals(None, a1.total(-1))


def test_funky_sum() -> None:
    """
    Tests the functionality of the function in a1.py named funky_sum.
    """
    assert_equals(2.0, a1.funky_sum(1, 3, 0.5))
    assert_equals(1, a1.funky_sum(1, 3, 0))
    assert_equals(1.5, a1.funky_sum(1, 3, 0.25))
    assert_equals(2.2, a1.funky_sum(1, 3, 0.6))
    assert_equals(3, a1.funky_sum(1, 3, 1))
    # Test when mix > 1
    assert_equals(3, a1.funky_sum(1, 3, 1.5))
    # Test when mix < 0
    assert_equals(1, a1.funky_sum(1, 3, -1.5))


def test_swip_swap() -> None:
    """
    Tests the functionality of the function in a1.py named swip_swap.
    """
    assert_equals('offbar', a1.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', a1.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', a1.swip_swap('foobar', 'z', 'c'))
    # every character in source is a target
    assert_equals('bobobo', a1.swip_swap('obobob', 'o', 'b'))
    # empty source string
    assert_equals('', a1.swip_swap('', 'a', 'b'))
    # space in source
    assert_equals('bobo ', a1.swip_swap('obob ', 'o', 'b'))


def main():
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
