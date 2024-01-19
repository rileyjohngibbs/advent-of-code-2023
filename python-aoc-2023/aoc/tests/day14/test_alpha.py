from aoc.models import InputLines
from aoc.solutions.day14.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 136


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == -1
