from aoc.solutions.day01 import efficient


def test_first_star(first_example) -> None:
    assert efficient.first_star(first_example[0]) == first_example[1]


def test_second_star(second_example) -> None:
    assert efficient.second_star(second_example[0]) == second_example[1]
