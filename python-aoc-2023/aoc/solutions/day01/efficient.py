from typing import Any

from aoc.models import DigitName, InputLines, WordTree
from aoc.run import solve

DAY = 1


def first_star(input_lines: InputLines) -> Any:
    tree_builder = [(str(i), i) for i in range(1, 10)]
    tree = WordTree.build(tree_builder)
    total: int = 0
    for line in input_lines:
        tens: int | None = None
        ones: int | None = None
        digits = tree.lookup_all(line)
        for digit in digits:
            if tens is None:
                tens = digit
            ones = digit
        assert tens is not None and ones is not None, line
        total += tens * 10 + ones
    return total


def second_star(input_lines: InputLines) -> Any:
    tree_builder = [(str(i), i) for i in range(1, 10)] + [
        (e.name, e.value) for e in DigitName
    ]
    tree = WordTree.build(tree_builder)
    total: int = 0
    for line in input_lines:
        tens: int | None = None
        ones: int | None = None
        digits = tree.lookup_all(line)
        for digit in digits:
            if tens is None:
                tens = digit
            ones = digit
        assert tens is not None and ones is not None, line
        total += tens * 10 + ones
    return total


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
