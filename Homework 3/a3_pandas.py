"""
Jaiden Atterbury
CSE 163 AD
04/15/23

Implements the pandas functions for Pokemon. In particular, these functions
provide and compute descriptive statistics for summarizing the pokemon
dataset, using the Pandas library to solve each problem. These functions
include: species_count, max_level, filter_range, mean_attack_for_type,
count_types, and mean_attack_per_type.
"""

import pandas as pd


def species_count(data_pandas: pd.DataFrame) -> int:
    """
    Takes in a DataFrame called data_pandas representing the pokemon dataset
    and returns the number of unique pokemon species in the dataset.
    """
    return len(data_pandas['name'].unique())


def max_level(data_pandas: pd.DataFrame) -> tuple[str, int]:
    """
    Takes in a DataFrame called data_pandas representing the pokemon dataset
    and returns a two element tuple of the name and level of the pokemon with
    the highest level. If there is a tie between the highest level, return the
    pokemon that appears first in the file.
    """
    max_level = data_pandas['level'].max()
    max_index = data_pandas['level'].idxmax()
    max_name = data_pandas.loc[max_index, 'name']
    return max_name, max_level


def filter_range(data_pandas: pd.DataFrame, low: int, up: int) -> list[str]:
    """
    Takes in a a DataFrame called data_pandas representing the pokemon dataset
    and two integers: a lower bound (inclusive) called low and an upper bound
    (exclusive) called up and returns a list of the names of pokemon whose
    level fall within the bounds in the same order that they appear in the
    data set.
    """
    is_gte_min = data_pandas['level'] >= low
    is_lt_max = data_pandas['level'] < up
    in_range = data_pandas[is_gte_min & is_lt_max]
    return list(in_range['name'])


def mean_attack_for_type(data_pandas: pd.DataFrame,
                         type_poke: str) -> float | None:
    """
    Takes in a DataFrame called data_pandas representing the pokemon dataset
    and a string called type_poke representing the type of the pokemon and
    returns the average attack for all of the pokemon in the dataset with the
    given type. If there are no pokemon of the given type, return None.
    """
    is_type = data_pandas['type'] == type_poke
    type_df = data_pandas[is_type]
    if not len(type_df):
        return None
    return type_df['atk'].mean()


def count_types(data_pandas: pd.DataFrame) -> dict[str, int]:
    """
    Takes in a DataFrame called data_pandas representing the pokemon dataset
    and returns a dictionary where the keys are strings representing each
    pokemon type, and the keys are integers representing the number of pokemon
    of that type.
    """
    grouped_type_df = data_pandas.groupby('type').size()
    return dict(grouped_type_df)


def mean_attack_per_type(data_pandas: pd.DataFrame) -> dict[str, float]:
    """
    Takes in a DataFrame called data_pandas representing the pokemon dataset
    and returns a dictionary where the keys are strings representing the
    pokemon type, and the values are floats representing the average attack of
    pokemon of that type.
    """
    grouped_type_atk_df = data_pandas.groupby('type')['atk'].mean()
    return dict(grouped_type_atk_df)
