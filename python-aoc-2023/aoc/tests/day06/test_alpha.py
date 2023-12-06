from aoc.models import InputLines
from aoc.solutions.day06.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """Time:      7  15   30
Distance:  9  40  200
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 288


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == 71503
