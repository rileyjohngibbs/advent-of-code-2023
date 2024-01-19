from aoc.models import InputLines
from aoc.solutions.day11.alpha import first_star, second_star

SAMPLE_INPUT = InputLines(
    """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 374


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == -1
