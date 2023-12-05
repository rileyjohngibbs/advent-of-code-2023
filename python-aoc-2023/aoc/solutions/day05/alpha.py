from collections.abc import Callable
from dataclasses import dataclass
from functools import reduce
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 5


def first_star(input_lines: InputLines) -> Any:
    seeds, maps = get_seeds_and_maps(input_lines)
    locations = reduce(
        lambda intervals, mapping: [
            mapped_interval
            for interval in intervals
            for mapped_interval in mapping(interval)
        ],
        maps,
        seeds,
    )
    return min(location.left for location in locations)


def second_star(input_lines: InputLines) -> Any:
    seeds, maps = get_seeds_and_maps(input_lines, True)
    locations = reduce(
        lambda intervals, mapping: [
            mapped_interval
            for interval in intervals
            for mapped_interval in mapping(interval)
        ],
        maps,
        seeds,
    )
    return min(location.left for location in locations)


@dataclass
class Interval:
    left: int
    size: int

    @classmethod
    def from_bounds(cls, left: int, right: int) -> "Interval | None":
        if right > left:
            return Interval(left=left, size=right - left)
        return None

    @property
    def right(self) -> int:
        return self.left + self.size

    def cut(
        self, other: "Interval"
    ) -> tuple["Interval | None", "Interval | None", "Interval | None"]:
        left = Interval.from_bounds(self.left, min(self.right, other.left))
        middle = Interval.from_bounds(
            max(self.left, other.left), min(self.right, other.right)
        )
        right = Interval.from_bounds(max(self.left, other.right), self.right)
        return (left, middle, right)


def get_seeds_and_maps(
    input_lines: InputLines, seed_ranges: bool = False
) -> tuple[list[Interval], list[Callable[[Interval], list[Interval]]]]:
    seed_numbers = map(int, filter(str.isdigit, input_lines[0].split()))
    if seed_ranges:  # part two
        seeds = [
            Interval(left=left, size=size)
            for left, size in zip(seed_numbers, seed_numbers)
        ]
    else:
        seeds = [Interval(left=left, size=1) for left in seed_numbers]
    maps: list[Callable[[Interval], list[Interval]]] = []
    rules: list[tuple[int, int, int]] = []
    for line in input_lines[3:]:
        if not line:
            maps.append(build_map(rules))
            rules = []
        elif line[0].isdigit():
            dmin, smin, length = map(int, line.split())
            rules.append((dmin, smin, length))
    maps.append(build_map(rules))
    return (seeds, maps)


def build_map(
    rules: list[tuple[int, int, int]]
) -> Callable[[Interval], list[Interval]]:
    rules_ = sorted(rules, key=lambda rule: rule[1])

    def map_(interval: Interval) -> list[Interval]:
        mapped_intervals: list[Interval] = []
        for dest, source, size in rules_:
            rule_interval = Interval(left=source, size=size)
            left, middle, right = interval.cut(rule_interval)
            if left is not None:
                mapped_intervals.append(left)
            if middle is not None:
                mapped_intervals.append(
                    Interval(left=middle.left - source + dest, size=middle.size)
                )
            if right is not None:
                interval = right
            else:
                break
        else:
            mapped_intervals.append(interval)
        return mapped_intervals

    return map_


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
