"""
Jaiden Atterbury
CSE 163 AD
04/15/23

Implements the manual functions for Pokemon. In particular, these functions
provide and compute descriptive statistics for summarizing the pokemon
dataset, wihout using the Pandas library to solve each problem. These functions
include: species_count, max_level, filter_range, mean_attack_for_type,
count_types, and mean_attack_per_type.
"""

from cse163_utils import Pokemon


def species_count(data_manual: list[Pokemon]) -> int:
    """
    Takes in a list of dictionaries called data_maunal representing the
    pokemon dataset and returns the number of unique pokemon species in the
    dataset.
    """
    num_unique = set()
    for pokemon in data_manual:
        num_unique.add(pokemon['name'])
    return len(num_unique)


def max_level(data_manual: list[Pokemon]) -> tuple[str, int]:
    """
    Takes in a list of dictionaries called data_manual representing the
    pokemon dataset and returns a two element tuple of the name and level
    of the pokemon with the highest level. If there is a tie between the
    highest level, return the pokemon that appears first in the file.
    """
    max_level = 0
    max_name = ""
    for pokemon in data_manual:
        if pokemon['level'] > max_level:
            max_level = pokemon['level']
            max_name = pokemon['name']
    return max_name, max_level


def filter_range(data_manual: list[Pokemon], low: int, up: int) -> list[str]:
    """
    Takes in a list of dictionaries called data_manual representing the
    pokemon dataset and two integers: a lower bound (inclusive) called low
    and an upper bound (exclusive) called up and returns a list of the names
    of pokemon whose level fall within the bounds in the same order that they
    appear in the data set.
    """
    name_list = []
    for pokemon in data_manual:
        if low <= pokemon['level'] < up:
            name_list.append(pokemon['name'])
    return name_list


def mean_attack_for_type(data_manual: list[Pokemon],
                         type_poke: str) -> float | None:
    """
    Takes in a list of dictionaries called data_manual representing the
    pokemon dataset and a string called type_poke representing the type of the
    pokemon and returns the average attack for all of the pokemon in the
    dataset with the given type. If there are no pokemon of the given type,
    return None.
    """
    total_attack = 0
    num_of_type = 0
    for pokemon in data_manual:
        if pokemon['type'] == type_poke:
            total_attack += pokemon['atk']
            num_of_type += 1
    if not num_of_type:
        return None
    return total_attack / num_of_type


def count_types(data_manual: list[Pokemon]) -> dict[str, int]:
    """
    Takes in a list of dictionaries called data_manual representing the
    pokemon dataset and returns a dictionary where the keys are strings
    representing each pokemon type, and the keys are integers representing
    the number of pokemon of that type.
    """
    types_dict = {}
    for pokemon in data_manual:
        if pokemon['type'] not in types_dict:
            types_dict[pokemon['type']] = 0
        types_dict[pokemon['type']] += 1
    return types_dict


def mean_attack_per_type(data_manual: list[Pokemon]) -> dict[str, float]:
    """
    Takes in a list of dictionaries called data_manual representing the
    pokemon dataset and returns a dictionary where the keys are strings
    representing the pokemon type, and the values are floats representing
    the average attack of pokemon of that type.
    """
    types = {}
    counts = {}
    for pokemon in data_manual:
        type_poke = pokemon['type']
        if type_poke not in types:
            types[type_poke] = 0
            counts[type_poke] = 0
        types[type_poke] += pokemon['atk']
        counts[type_poke] += 1
    return {uniq: types[uniq] / counts[uniq] for uniq in types.keys()}
