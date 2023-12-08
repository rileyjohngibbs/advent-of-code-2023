from aoc.models import InputLines
from aoc.solutions.day07.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 6440


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == 5905
