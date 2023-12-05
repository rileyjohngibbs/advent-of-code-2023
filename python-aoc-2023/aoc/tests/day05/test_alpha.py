import pytest

from aoc.models import InputLines
from aoc.solutions.day05.alpha import Interval, build_map, first_star, second_star

EXAMPLE_IN = InputLines(
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(EXAMPLE_IN) == 35


def test_second_star() -> None:
    assert second_star(EXAMPLE_IN) == 46


@pytest.mark.parametrize(
    "left, size, expected",
    [
        (0, 4, [(5, 3), (3, 1)]),
        (0, 10, [(5, 3), (3, 2), (0, 2), (7, 3)]),
        (8, 2, [(8, 2)]),
    ],
)
def test_build_map(left, size, expected) -> None:
    interval = Interval(left=left, size=size)
    rules = [(5, 0, 3), (0, 5, 2)]
    map_ = build_map(rules)
    assert map_(interval) == [Interval(left=left, size=size) for left, size in expected]
