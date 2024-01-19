from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 11


def first_star(input_lines: InputLines) -> Any:
    return sum_expanded_distances(input_lines, 2)


def second_star(input_lines: InputLines) -> Any:
    return sum_expanded_distances(input_lines, 1_000_000)


def sum_expanded_distances(galaxy: list[str], expansion_factor: int) -> int:
    empty_rows = {y for y, row in enumerate(galaxy) if all(p == "." for p in row)}
    empty_columns = {
        x for x in range(len(galaxy[0])) if all(row[x] == "." for row in galaxy)
    }
    galaxies = [
        (y, x)
        for y, row in enumerate(galaxy)
        for x, point in enumerate(row)
        if point == "#"
    ]

    def distance(y1: int, x1: int, y2: int, x2: int) -> int:
        if y2 < y1:
            y1, y2 = y2, y1
        if x2 < x1:
            x1, x2 = x2, x1
        row_expansions = sum(y in empty_rows for y in range(y1, y2)) * (
            expansion_factor - 1
        )
        column_expansions = sum(x in empty_columns for x in range(x1, x2)) * (
            expansion_factor - 1
        )
        return abs(y2 - y1) + abs(x2 - x1) + row_expansions + column_expansions

    distances = [
        distance(*g1, *g2)
        for i, g1 in enumerate(galaxies[:-1])
        for g2 in galaxies[i + 1 :]
    ]
    return sum(distances)


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
