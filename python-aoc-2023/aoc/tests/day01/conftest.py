from typing import Any

import pytest

from aoc.models import InputLines

FIRST_EXAMPLE = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".lstrip().splitlines()
FIRST_EXPECTED = 142
SECOND_EXAMPLE = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".lstrip().splitlines()
SECOND_EXPECTED = 281


@pytest.fixture
def first_example() -> tuple[InputLines, Any]:
    return InputLines(FIRST_EXAMPLE), FIRST_EXPECTED


@pytest.fixture
def second_example() -> tuple[InputLines, Any]:
    return InputLines(SECOND_EXAMPLE), SECOND_EXPECTED
