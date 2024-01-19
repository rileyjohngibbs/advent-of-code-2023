from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 14


def first_star(input_lines: InputLines) -> Any:
    new_state: list[list[str]] = []
    for y, row in enumerate(input_lines):
        new_row: list[str] = []
        new_state.append(new_row)
        for x, cell in enumerate(row):
            if cell == "O":
                obstruction_y = next(
                    (y_ for y_ in range(y)[::-1] if new_state[y_][x] != "."),
                    -1,
                )
                rest_y = obstruction_y + 1
                if rest_y == y:
                    new_row.append(cell)
                else:
                    new_state[rest_y][x] = cell
                    new_row.append(".")
            else:
                new_row.append(cell)
    return sum(
        len(new_state) - y
        for y, row in enumerate(new_state)
        for x, cell in enumerate(row)
        if cell == "O"
    )


def second_star(input_lines: InputLines) -> Any:
    return 0


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
