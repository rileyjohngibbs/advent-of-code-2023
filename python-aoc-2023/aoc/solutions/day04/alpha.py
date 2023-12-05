from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 4


def first_star(input_lines: InputLines) -> Any:
    return sum(
        2 ** (x - 1)
        for x in (
            len(winners & on_card) for winners, on_card in map(parse_card, input_lines)
        )
        if x > 0
    )


def second_star(input_lines: InputLines) -> Any:
    scores = (
        len(winners & on_card) for winners, on_card in map(parse_card, input_lines)
    )
    duplicates = [1] * len(input_lines)
    for card_number, score in enumerate(scores):
        left, right = card_number + 1, card_number + 1 + score
        duplicates[left:right] = [
            n + duplicates[card_number] for n in duplicates[left:right]
        ]
    return sum(duplicates)


def parse_card(card_line: str) -> tuple[set[int], set[int]]:
    _, numbers_string = card_line.split(":", 1)
    winners, on_card = (
        set(map(int, side.split())) for side in numbers_string.split("|")
    )
    return winners, on_card


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
