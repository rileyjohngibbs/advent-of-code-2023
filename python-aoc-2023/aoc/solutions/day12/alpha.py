import re
from itertools import starmap
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 12

BREAKABLE = {"#", "?"}
WORKABLE = {".", "?"}


def first_star(input_lines: InputLines) -> Any:
    parsed_lines = (
        (left, list(map(int, right.split(","))))
        for left, right in (line.split() for line in input_lines)
    )
    return sum(starmap(build_arrangements_two, parsed_lines))


def second_star(input_lines: InputLines) -> Any:
    parsed_lines = (
        ("?".join([left] * 5), list(map(int, ",".join([right] * 5).split(","))))
        for left, right in (line.split() for line in input_lines)
    )
    return sum(starmap(build_arrangements_two, parsed_lines))


def valid(left: str, right: list[int]) -> bool:
    if len(right) == 0:
        return not any(s == "#" for s in left)
    next_grouping = right[0]
    for start, symbol in enumerate(left):
        if symbol != ".":
            if start + next_grouping > len(left):
                return False
            if (
                all(s in BREAKABLE for s in left[start : start + next_grouping])
                and (
                    start + next_grouping == len(left)
                    or left[start + next_grouping] in WORKABLE
                )
                and valid(left[start + next_grouping + 1 :], right[1:])
            ):
                return True
            elif symbol == "#":
                return False
    return False


def build_arrangements(left: str, right: list[int]) -> int:
    if not valid(left, right):
        return 0
    if not any(symbol == "?" for symbol in left):
        return 1
    working = left.replace("?", ".", 1)
    broken = left.replace("?", "#", 1)
    working_arrangements = build_arrangements(working, right)
    broken_arrangements = build_arrangements(broken, right)
    return working_arrangements + broken_arrangements


def build_arrangements_two(left: str, right: list[int]) -> int:
    if not left:
        return not right
    if not right:
        return all(s != "#" for s in left)
    m = re.match(r"\.*(\#+)[.$](.*)", left)
    if m is not None and len(m.group(1)) == right[0]:
        return build_arrangements_two(m.group(2), right[1:])
    working = left.replace("?", ".", 1)
    broken = left.replace("?", "#", 1)
    working_arrangements = build_arrangements(working, right)
    broken_arrangements = build_arrangements(broken, right)
    return working_arrangements + broken_arrangements


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
