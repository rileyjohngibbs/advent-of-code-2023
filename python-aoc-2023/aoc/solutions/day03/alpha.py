from typing import Any

from aoc.models import Grid, GridCell, InputLines
from aoc.run import solve

DAY = 3


def first_star(input_lines: InputLines) -> Any:
    grid = Grid(input_lines)
    numbers: list[int] = []
    row = -1
    number = 0
    symbol_adjacent = False
    for cell in grid:
        if cell.y != row or not cell.value.isdigit():
            if symbol_adjacent:
                numbers.append(number)
                symbol_adjacent = False
            row = cell.y
            number = 0
        if cell.value.isdigit():
            number = 10 * number + int(cell.value)
            if not symbol_adjacent and any(
                n.value != "." and not n.value.isdigit()
                for n in grid.neighbors(cell.y, cell.x)
            ):
                symbol_adjacent = True
    return sum(numbers)


def second_star(input_lines: InputLines) -> Any:
    grid = Grid(input_lines)
    total = 0
    for cell in grid:
        if cell.value == "*":
            adjacent_numbers: list[int] = []
            blobbed_addresses: set[tuple[int, int]] = set()
            for neighbor in grid.neighbors(cell.y, cell.x):
                if (
                    neighbor.y,
                    neighbor.x,
                ) not in blobbed_addresses and neighbor.value.isdigit():
                    blob = gather_blob(grid, neighbor)
                    blobbed_addresses.update((c.y, c.x) for c in blob)
                    adjacent_numbers.append(
                        sum(
                            10**n * int(cell.value)
                            for n, cell in enumerate(reversed(blob))
                        )
                    )
            if len(adjacent_numbers) == 2:
                factor1, factor2 = adjacent_numbers
                total += factor1 * factor2
    return total


def gather_blob(grid: Grid[str], point: GridCell[str]) -> list[GridCell[str]]:
    cells = [point]
    left = point.x - 1
    while left >= 0:
        value = grid.value(point.y, left)
        if value.isdigit():
            cells.insert(0, GridCell(y=point.y, x=left, value=value))
        else:
            break
        left -= 1
    right = point.x + 1
    while right < grid.width:
        value = grid.value(point.y, right)
        if value.isdigit():
            cells.append(GridCell(y=point.y, x=right, value=value))
        else:
            break
        right += 1
    return cells


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
