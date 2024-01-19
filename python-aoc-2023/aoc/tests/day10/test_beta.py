import pytest

from aoc.models import InputLines
from aoc.solutions.day10.beta import first_star, move, second_star

SAMPLE_INPUT = InputLines(
    """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 8


SECOND_SAMPLE = InputLines(
    """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".strip().splitlines()
)


def test_second_star() -> None:
    assert second_star(SECOND_SAMPLE) == 10


@pytest.mark.parametrize(
    "address, delta, expected",
    [
        ((0, 0), (1, 0), (1, 0)),
        ((5, 7), (0, -1), (5, 6)),
    ],
)
def test_move(
    address: tuple[int, int], delta: tuple[int, int], expected: tuple[int, int]
) -> None:
    assert move(address, delta) == expected
