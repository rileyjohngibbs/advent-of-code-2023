from aoc.models import InputLines
from aoc.solutions.day09.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 114


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == 2
