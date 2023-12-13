import itertools

import pytest

from aoc.models import InputLines
from aoc.solutions.day12.alpha import (
    build_arrangements,
    build_arrangements_two,
    first_star,
    second_star,
    valid,
)

SAMPLE_INPUT = InputLines(
    """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()
)


def test_first_star() -> None:
    assert first_star(SAMPLE_INPUT) == 21


def test_second_star() -> None:
    assert second_star(SAMPLE_INPUT) == 525152


@pytest.mark.parametrize(
    "left, right, result",
    [
        ("?????", [1, 1, 1], True),
        ("##???", [1, 1, 1], False),
        ("#?#?#", [1, 1, 1], True),
        ("???##", [1, 1, 1], False),
        ("#.#.#", [1, 1, 1], True),
        (".??.###", [1, 1, 3], False),
        ("..#..##...?##.", [1, 1, 3], False),
        ("...#########.#..#", [9, 1, 2], False),
        ("#..", [1, 1], False),
        ("?..", [1, 1], False),
        ("..?", [1], True),
        ("..##", [2, 1], False),
    ],
)
def test_valid(left: str, right: list[int], result: bool) -> None:
    assert valid(left, right) == result


@pytest.mark.parametrize(
    "left, right, result",
    [
        ("?###????????", [3, 2, 1], 10),
        (".?????????.#??", [1, 6, 2], 3),
        ("?????", [1], 5),
        ("?????", [1, 1, 1], 1),
        ("...?????#???????#", [9, 1, 2], 1),
        (".##.???#", [2, 2], 1),
        (".#?????#", [2, 2], 1),
        (".???#.#?", [2, 2], 1),
    ],
)
def test_build_arrangements(left: str, right: list[int], result: int) -> None:
    assert build_arrangements(left, right) == result


@pytest.mark.parametrize(
    "left, right, result",
    [
        ("?###????????", [3, 2, 1], 10),
        (".?????????.#??", [1, 6, 2], 3),
        ("?????", [1], 5),
        ("?????", [1, 1, 1], 1),
        ("...?????#???????#", [9, 1, 2], 1),
        (".##.???#", [2, 2], 1),
        (".#?????#", [2, 2], 1),
        (".???#.#?", [2, 2], 1),
    ],
)
def test_build_arrangements_two(left: str, right: list[int], result: int) -> None:
    assert build_arrangements_two(left, right) == result


@pytest.mark.skip
@pytest.mark.parametrize(
    "left, right",
    list(("".join(prod), [2, 2]) for prod in itertools.product(*[(".", "#", "?")] * 8)),
)
def test_build_vs_brute(left: str, right: list[int]) -> None:
    assert build_arrangements(left, right) == brute_force(left, right)


def brute_force(left: str, right: list[int]) -> int:
    resolved: list[str] = [""]
    for symbol in left:
        if symbol in {"#", "."}:
            resolved = [r + symbol for r in resolved]
        else:
            resolved = [r + "#" for r in resolved] + [r + "." for r in resolved]
    return sum(matches(r, right) for r in resolved)


def matches(left: str, right: list[int]) -> bool:
    return list(map(len, left.replace(".", " ").split())) == right
