import math
from functools import reduce
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 6


def first_star(input_lines: InputLines) -> Any:
    races = parse_races(input_lines)
    win_counts = map(
        lambda x: x[1] - x[0] + 1, (calculate_winning_range(*race) for race in races)
    )
    return reduce(lambda a, b: a * b, win_counts, 1)


def second_star(input_lines: InputLines) -> Any:
    time = int("".join(filter(str.isdigit, input_lines[0].split())))
    distance = int("".join(filter(str.isdigit, input_lines[1].split())))
    lower, upper = calculate_winning_range(time, distance)
    return upper - lower + 1


def parse_races(input_lines: InputLines) -> list[tuple[int, int]]:
    times = map(int, filter(str.isdigit, input_lines[0].split()))
    distances = map(int, filter(str.isdigit, input_lines[1].split()))
    return list(zip(times, distances))


def calculate_winning_range(time: int, distance: int) -> tuple[int, int]:
    root_term = math.sqrt(time**2 - 4 * distance)
    lower = (time - root_term) / 2
    upper = (time + root_term) / 2
    return (
        math.ceil(lower) if int(lower) != lower else int(lower) + 1,
        math.floor(upper) if int(upper) != upper else int(upper) - 1,
    )


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
