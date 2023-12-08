from collections import Counter
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 7

CARDS = "AKQJT98765432"
CARD_RANKS = {card: n for n, card in enumerate(CARDS[::-1])}
CARD_RANKS_JOKER = {**CARD_RANKS, "J": -1}

HANDS: list[tuple[int, ...]] = [
    (5,),
    (4, 1),
    (3, 2),
    (3, 1, 1),
    (2, 2, 1),
    (2, 1, 1, 1),
    (1,) * 5,
]
HAND_SCORES = {hand: score for score, hand in enumerate(HANDS[::-1])}


def first_star(input_lines: InputLines) -> Any:
    hands = sorted(
        ((Hand(cards), wager) for cards, wager in map(parse_line, input_lines)),
        key=lambda x: x[0],
    )
    return sum(wager * rank for rank, (_, wager) in enumerate(hands, 1))


def second_star(input_lines: InputLines) -> Any:
    hands = sorted(
        ((Hand(cards, True), wager) for cards, wager in map(parse_line, input_lines)),
        key=lambda x: x[0],
    )
    return sum(wager * rank for rank, (_, wager) in enumerate(hands, 1))


def parse_line(input_line: str) -> tuple[str, int]:
    hand, score_str = input_line.split()
    return hand, int(score_str)


class Hand:
    cards: str
    score: tuple[int, ...]

    def __init__(self, cards: str, joker: bool = False) -> None:
        self.cards = cards
        self.score = self.calculate_score(cards, joker)

    @staticmethod
    def calculate_score(cards: str, joker: bool) -> tuple[int, ...]:
        card_counts = Counter(cards)
        group_sizes = sorted(
            [
                count
                for card, count in card_counts.items()
                if not (joker and card == "J")
            ],
            reverse=True,
        )
        if joker:
            if group_sizes:
                group_sizes[0] += card_counts["J"]
            else:
                group_sizes.append(card_counts["J"])
        hand_type_score = HAND_SCORES[tuple(group_sizes)]
        rank_map = CARD_RANKS_JOKER if joker else CARD_RANKS
        return (hand_type_score, *(rank_map[card] for card in cards))

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return NotImplemented
        return self.score > __value.score

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return NotImplemented
        return self.score < __value.score

    def __repr__(self) -> str:
        return f"<Hand({self.cards})>"


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
