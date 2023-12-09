import itertools
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 9


def first_star(input_lines: InputLines) -> Any:
    return sum(map(infer_next_value, map(parse_line, input_lines)))


def second_star(input_lines: InputLines) -> Any:
    return sum(map(infer_next_value, (h[::-1] for h in map(parse_line, input_lines))))


def parse_line(input_line: str) -> list[int]:
    return list(map(int, input_line.split()))


def infer_next_value(temperatures: list[int]) -> int:
    delta_lists = [temperatures]
    while not all(d == delta_lists[-1][0] for d in delta_lists[-1]):
        delta_lists.append([b - a for a, b in itertools.pairwise(delta_lists[-1])])
    for lower, higher in itertools.pairwise(reversed(delta_lists)):
        higher.append(higher[-1] + lower[-1])
    return delta_lists[0][-1]


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
