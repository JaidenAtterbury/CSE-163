"""
Jaiden Atterbury
CSE 163 AD
04/15/23

Tests the functions for Pokemon. In particular, tests the functions in
a3_manual.py and a3_pandas.py.
"""

import pandas as pd

from cse163_utils import assert_equals, parse, Pokemon

import a3_manual
import a3_pandas

# If you want to include more global constants,
# please check the code quality guide!
SPEC_TEST_FILE = "/home/pokemon_test.csv"
CREATED_TEST_FILE = "/home/pokemon_test_user.csv"


# Your tests here!
def test_species_count(data_manual: list[Pokemon],
                       created_manual: list[Pokemon],
                       data_pandas: pd.DataFrame,
                       created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    species_count.
    """
    # Specification tests:
    assert_equals(3, a3_manual.species_count(data_manual))
    assert_equals(3, a3_pandas.species_count(data_pandas))
    # Created tests:
    assert_equals(5, a3_manual.species_count(created_manual))
    assert_equals(5, a3_pandas.species_count(created_pandas))


def test_max_level(data_manual: list[Pokemon],
                   created_manual: list[Pokemon],
                   data_pandas: pd.DataFrame,
                   created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    max_level.
    """
    # Specification tests:
    assert_equals(('Lapras', 72), a3_manual.max_level(data_manual))
    assert_equals(('Lapras', 72), a3_pandas.max_level(data_pandas))
    # Created file tests:
    assert_equals(('Jynx', 72), a3_manual.max_level(created_manual))
    assert_equals(('Jynx', 72), a3_pandas.max_level(created_pandas))


def test_filter_range(data_manual: list[Pokemon],
                      created_manual: list[Pokemon],
                      data_pandas: pd.DataFrame,
                      created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    filter_range.
    """
    # Specification tests:
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  a3_manual.filter_range(data_manual, 35, 72))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  a3_pandas.filter_range(data_pandas, 35, 72))
    # Created file tests:
    assert_equals(['Venusaur'],
                  a3_manual.filter_range(created_manual, 35, 72))
    assert_equals(['Venusaur'],
                  a3_pandas.filter_range(created_pandas, 35, 72))
    # All names out of range tests:
    assert_equals([], a3_manual.filter_range(created_manual, 73, 74))
    assert_equals([], a3_pandas.filter_range(created_pandas, 73, 74))
    # All names in range tests:
    assert_equals(['Arcanine', 'Arcanine', 'Starmie', "Lapras"],
                  a3_manual.filter_range(data_manual, 35, 73))
    assert_equals(['Arcanine', 'Arcanine', 'Starmie', "Lapras"],
                  a3_pandas.filter_range(data_pandas, 35, 73))


def test_mean_attack_for_type(data_manual: list[Pokemon],
                              created_manual: list[Pokemon],
                              data_pandas: pd.DataFrame,
                              created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    mean_attack_for_type.
    """
    # Specification tests:
    assert_equals(47.5,
                  a3_manual.mean_attack_for_type(data_manual, 'fire'))
    assert_equals(47.5,
                  a3_pandas.mean_attack_for_type(data_pandas, 'fire'))
    # Created file tests:
    assert_equals(111,
                  a3_manual.mean_attack_for_type(created_manual,
                                                 'psychic'))
    assert_equals(111,
                  a3_pandas.mean_attack_for_type(created_pandas,
                                                 'psychic'))
    # None of type tests:
    assert_equals(None,
                  a3_manual.mean_attack_for_type(data_manual, 'grass'))
    assert_equals(None,
                  a3_pandas.mean_attack_for_type(data_pandas, 'grass'))


def test_count_types(data_manual: list[Pokemon],
                     created_manual: list[Pokemon],
                     data_pandas: pd.DataFrame,
                     created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    count_types.
    """
    # Specification tests:
    assert_equals({'fire': 2, 'water': 2}, a3_manual.count_types(data_manual))
    assert_equals({'fire': 2, 'water': 2}, a3_pandas.count_types(data_pandas))
    # Created file tests:
    assert_equals({'fire': 2, 'grass': 2, 'psychic': 1, 'water': 1},
                  a3_manual.count_types(created_manual))
    assert_equals({'fire': 2, 'grass': 2, 'psychic': 1, 'water': 1},
                  a3_pandas.count_types(created_pandas))


def test_mean_attack_per_type(data_manual: list[Pokemon],
                              created_manual: list[Pokemon],
                              data_pandas: pd.DataFrame,
                              created_pandas: pd.DataFrame) -> None:
    """
    Tests the functions from a3_manual.py and a3_pandas.py called
    mean_attack_per_type.
    """
    # Specification tests:
    assert_equals({'fire': 47.5, 'water': 140.5},
                  a3_manual.mean_attack_per_type(data_manual))
    assert_equals({'fire': 47.5, 'water': 140.5},
                  a3_pandas.mean_attack_per_type(data_pandas))
    # Created file tests:
    assert_equals({'fire': 109, 'grass': 140.5, 'psychic': 111, 'water': 107},
                  a3_manual.mean_attack_per_type(created_manual))
    assert_equals({'fire': 109, 'grass': 140.5, 'psychic': 111, 'water': 107},
                  a3_pandas.mean_attack_per_type(created_pandas))


def main():
    # Create input data:
    data_manual: list[Pokemon] = parse(SPEC_TEST_FILE)
    manual_created: list[Pokemon] = parse(CREATED_TEST_FILE)
    data_pandas: pd.DataFrame = pd.read_csv(SPEC_TEST_FILE)
    pandas_created: pd.DataFrame = pd.read_csv(CREATED_TEST_FILE)

    # Test implementation:
    test_species_count(data_manual, manual_created,
                       data_pandas, pandas_created)
    test_max_level(data_manual, manual_created,
                   data_pandas, pandas_created)
    test_filter_range(data_manual, manual_created,
                      data_pandas, pandas_created)
    test_mean_attack_for_type(data_manual, manual_created,
                              data_pandas, pandas_created)
    test_count_types(data_manual, manual_created,
                     data_pandas, pandas_created)
    test_mean_attack_per_type(data_manual, manual_created,
                              data_pandas, pandas_created)


if __name__ == "__main__":
    main()
