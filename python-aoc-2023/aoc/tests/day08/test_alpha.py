import pytest

from aoc.models import InputLines
from aoc.solutions.day08.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()
)

SAMPLE_INPUT_2 = InputLines(
    """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()
)

SAMPLE_INPUT_3 = InputLines(
    """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().splitlines()
)


@pytest.mark.parametrize(
    "sample_input, solution", [(SAMPLE_INPUT, 2), (SAMPLE_INPUT_2, 6)]
)
def test_first_star(sample_input, solution) -> None:
    assert first_star(sample_input) == solution


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT_3) == 6
