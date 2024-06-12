"""
Jaiden Atterbury
CSE 163 AD
04/08/23

Tests the functions for Primer. In particular, tests the functions in a2.py.
"""

import a2

from cse163_utils import assert_equals


def test_total() -> None:
    """
    Tests the total method.
    """
    # The regular case
    assert_equals(15, a2.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, a2.total(1))
    assert_equals(0, a2.total(0))
    # Test the None case
    assert_equals(None, a2.total(-1))


def test_travel() -> None:
    """
    Tests the method in a2.py called travel.
    """
    # Specification test case:
    assert_equals((-1, 4), a2.travel('NW!ewnW', (1, 2)))
    # No valid characters:
    assert_equals((1, 2), a2.travel('abcd', (1, 2)))
    # Tests the case where all characters are lowercase:
    assert_equals((1, 2), a2.travel('nesw', (1, 2)))
    # Tests the empty string case:
    assert_equals((-1, -2), a2.travel('', (-1, -2)))


def test_reformat_date() -> None:
    """
    Tests the method in a2.py called reformat_date.
    """
    # Specification test case #1:
    assert_equals("31/12/1998",
                  a2.reformat_date("12/31/1998", "M/D/Y", "D/M/Y"))
    # Specification test case #2:
    assert_equals("3/1/2", a2.reformat_date("1/2/3", "M/D/Y", "Y/M/D"))
    # Specification test case #3:
    assert_equals("4/0", a2.reformat_date("0/200/4", "Y/D/M", "M/Y"))
    # Specification test case #4:
    assert_equals("2", a2.reformat_date("3/2", "M/D", "D"))
    # Tests a different ordering than the above tests:
    assert_equals("1/3/2", a2.reformat_date("1/2/3", "M/D/Y", "M/Y/D"))
    # Tests the case when target is the same as current
    assert_equals("3/2", a2.reformat_date("3/2", "M/D", "M/D"))


def test_longest_word() -> None:
    """
    Tests the method in a2.py called longest_word.
    """
    # Specification test case:
    assert_equals("3: Merrily,", a2.longest_word('/home/song.txt'))
    # Tests the case where there is a tie between longest word:
    assert_equals("2: longest", a2.longest_word('/home/test.txt'))
    # Test the case where the file is empty
    assert_equals(None, a2.longest_word('/home/empty.txt'))


def test_get_average_in_range() -> None:
    """
    Tests the method in a2.py called get_average_in_range.
    """
    # Specification test #1:
    assert_equals(5.5, a2.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    # Specification test #2:
    assert_equals(2.067, a2.get_average_in_range([1, 2, 3.2], -1, 10))
    # Tests the case where there are no values in the given range:
    assert_equals(0, a2.get_average_in_range([1, 2, 3, 4], 5, 10))
    # Tests the case where the average is a negative value:
    assert_equals(-1.275, a2.get_average_in_range([5, -5, 0, -5.1], -10, 6))
    # Tests the case where the average is an int value:
    assert_equals(2, a2.get_average_in_range([0, 3, 3], 0, 6))
    # Tests the case where there is no value in the input range:
    assert_equals(0, a2.get_average_in_range([], 5, 10))


def test_mode_digit() -> None:
    """
    Tests the method in a2.py called mode_digit:
    """
    # Specification test #1:
    assert_equals(1, a2.mode_digit(12121))
    # Specification test #2:
    assert_equals(0, a2.mode_digit(0))
    # Specification test #3:
    assert_equals(2, a2.mode_digit(-122))
    # Specification test #4:
    assert_equals(2, a2.mode_digit(1211232231))
    # Tests the case where there is a tie:
    assert_equals(4, a2.mode_digit(444333222111))
    # Tests the case where the mode is 0:
    assert_equals(0, a2.mode_digit(100000000))


def main():
    test_total()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == '__main__':
    main()
