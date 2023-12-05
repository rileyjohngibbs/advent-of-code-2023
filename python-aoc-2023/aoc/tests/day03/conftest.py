import pytest

from aoc.models import InputLines

INPUT_ONE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()

PART_ONE_ANSWER = 4361

PART_TWO_ANSWER = 467835


@pytest.fixture
def input_one() -> list[str]:
    return InputLines(INPUT_ONE)


@pytest.fixture
def answer_one() -> int:
    return PART_ONE_ANSWER


@pytest.fixture
def answer_two() -> int:
    return PART_TWO_ANSWER
