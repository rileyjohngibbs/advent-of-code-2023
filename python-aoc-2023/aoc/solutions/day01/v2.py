from collections.abc import Iterator, Sequence
from typing import Any

from aoc.models import DigitName, InputLines
from aoc.run import solve

DAY = 1


def first_star(input_lines: InputLines) -> Any:
    return sum(squash_digits(get_digits(line)) for line in input_lines)


def second_star(input_lines: InputLines) -> Any:
    return sum(squash_digits(get_digits(line, True)) for line in input_lines)


def get_digits(characters: Sequence[str], with_words: bool = False) -> list[int]:
    if not with_words:
        return [int(char) for char in characters if char.isdigit()]

    digit_searches: Iterator[int] = (
        int(character)
        if character.isdigit()
        else next(
            (
                digit
                for digit in DigitName
                if str(characters[left:]).startswith(digit.name)
            ),
            -1,
        )
        for left, character in enumerate(characters)
    )
    digits = [x for x in digit_searches if x > 0]
    return digits


def squash_digits(digits: Sequence[int]) -> int:
    return digits[0] * 10 + digits[-1]


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
