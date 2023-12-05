import re
from typing import Any

from pydantic import BaseModel

from aoc.models import InputLines
from aoc.run import solve

DAY = 2


def first_star(input_lines: InputLines) -> int:
    bag = BallCollection(red=12, green=13, blue=14)
    games = map(parse_line, input_lines)
    return sum(
        game_number
        for game_number, pulls in games
        if all(bag.covers(pull) for pull in pulls)
    )


def second_star(input_lines: InputLines) -> int:
    games = map(parse_line, input_lines)
    minimums = (BallCollection.minimum_cover(pulls) for _, pulls in games)
    return sum(map(BallCollection.power, minimums))


class BallCollection(BaseModel):
    red: int = 0
    green: int = 0
    blue: int = 0

    def covers(self, other: "BallCollection") -> bool:
        return (
            self.red >= other.red
            and self.green >= other.green
            and self.blue >= other.blue
        )

    @classmethod
    def minimum_cover(cls, others: list["BallCollection"]) -> "BallCollection":
        red, green, blue = 0, 0, 0
        for other in others:
            red = max(red, other.red)
            green = max(green, other.green)
            blue = max(blue, other.blue)
        return cls(red=red, green=green, blue=blue)

    def power(self) -> int:
        return self.red * self.green * self.blue


def parse_line(line: str) -> tuple[int, list[BallCollection]]:
    game_regex = r"Game (\d+): (.*)"
    regex_match = re.match(game_regex, line)
    assert regex_match is not None
    game_num_str, pulls_string = regex_match.groups()
    game_number = int(game_num_str)
    pulls = pulls_string.split("; ")
    ball_collections: list[BallCollection] = []
    for pull in pulls:
        counts = [c.split(" ") for c in pull.split(", ")]
        ball_collections.append(
            BallCollection(**{color: int(count) for count, color in counts})
        )
    return game_number, ball_collections


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
