"""
Jaiden Atterbury
CSE 163 AD
04/08/23

Implements the functions for Primer. These functions are total, travel,
reformat_date, longest_word, get_average_in_range, and mode_digit.
"""


def total(n: int) -> int | None:
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


# Write your functions here!
def travel(directions: str, start: tuple[int, int]) -> tuple[int, int]:
    """
    Takes a string called directions of north, east, south, west directions
    and a tuple called start indicating the starting x, y location on a grid,
    and returns a tuple indicating the final x, y location on a grid. Any
    characters that are not 'N', 'E', 'W', or 'S', ignoring letter-casing,
    should be ignored.
    """
    x_new, y_new = start

    # Go through each char in direction and increment/decrement the x and y
    # coordinate depending on the value of char. Uses if, elif, ..., elif
    # branches to ignore other characters that arent "N", "E", "S", and "W".
    for char in directions.upper():
        if char == 'N':
            y_new += 1
        elif char == 'E':
            x_new += 1
        elif char == 'S':
            y_new -= 1
        elif char == 'W':
            x_new -= 1

    return x_new, y_new


def reformat_date(date: str, current: str, target: str) -> str:
    """
    Takes three strings as arguments called date, current, and target
    representing a date, a current date format, and a target date format
    respectively, and returns a new string with the date formatted in the
    target format.
    """
    # Creates a dict that maps "D", "M", "Y" to their corresponding value in
    # date.
    curr_date_dict = {}
    for text, value in zip(current.split("/"), date.split("/")):
        curr_date_dict[text] = value

    # Create a str that takes the values in the above dict and maps
    # the values to their corresponding places in target.
    final = ""
    for char in target:
        if char == "/":
            final += char
        else:
            final += curr_date_dict[char]

    return final


def longest_word(file_name: str) -> str | None:
    """
    Takes a string representing a file called file_name and returns a string
    that reports the longest word in the file and with which line it appears
    on. Returns the word that appears firs in the file if there are ties for
    the longest word. Returns None if the file is empty/has no words.
    """
    line_num = 0
    word_length = 0
    long_word = ""

    # Opens the file and creates a list of all the lines, returning None if
    # the list is empty.
    with open(file_name) as f:
        lines = f.readlines()
        if not lines:
            return None

        # Loops through and creates a counter for each line breaking the line
        # up into individual words
        for num, line in enumerate(lines, start=1):
            words = line.split()

            # Loops through each word in the given line and finds the line
            # number, length, and corresponding word of the largest word in
            # the given line.
            for word in words:
                if len(word) > word_length:
                    line_num = num
                    word_length = len(word)
                    long_word = word

    return str(line_num) + ": " + long_word


def get_average_in_range(lst: list[float], low: float, high: float) -> float:
    """
    Takes in a list of floats called lst and floats called low and high, and
    returns the average of all values within the list that lies in the given
    range from low (inclusive), to high (exclusive). If there are no values
    in the range, returns 0.
    """
    # Create a new list that contains the values in lst that are between
    # low and high.
    new_lst = [value for value in lst if value >= low and value < high]

    if not len(new_lst):
        return 0

    return sum(new_lst) / len(new_lst)


def mode_digit(n: int) -> int:
    """
    Takes in an integer number n and returns the digit that appears most
    frequently in that number. If there is a tie between the most frequent
    digit, the digit with the higher value will be returned.
    """
    # Return 0 if n == 0 since the only way we don't enter the loop is if
    # n == 0.
    if n == 0:
        return 0

    # Create a dictionary that has the keys as the digits and the values as
    # the frequency.
    mode_dict = {}
    n = abs(n)
    while n > 0:
        digit = n % 10
        if digit in mode_dict:
            mode_dict[digit] += 1
        else:
            mode_dict[digit] = 1
        n = n // 10

    # Now that we have this dictionary, loop through the digits and their
    # corresponding frequencies and return the digit that occurs most often
    # while breaking tiebreakers with the larger digit.
    max_digit = 0
    max_total = 0
    for digit, total in mode_dict.items():
        if total > max_total:
            max_total = total
            max_digit = digit
        elif total == max_total and digit > max_digit:
            max_digit = digit

    return max_digit
