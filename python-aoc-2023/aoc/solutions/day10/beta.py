from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 10

CONNECTIONS_MAP: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
    ".": ((0, 0), (0, 0)),
}

CrossBounds = bool
TraversalState = dict[str, tuple["TraversalState", CrossBounds]]
OFF_PIPE: TraversalState = {}
ABOVE: TraversalState = {}
BELOW: TraversalState = {}
OFF_PIPE.update(
    {
        "|": (OFF_PIPE, True),
        "F": (ABOVE, False),
        "L": (BELOW, False),
    }
)
ABOVE.update(
    {
        "-": (ABOVE, False),
        "7": (OFF_PIPE, False),
        "J": (OFF_PIPE, True),
    }
)
BELOW.update(
    {
        "-": (BELOW, False),
        "7": (OFF_PIPE, True),
        "J": (OFF_PIPE, False),
    }
)


def first_star(input_lines: InputLines) -> Any:
    loop = build_loop(input_lines)
    return len(loop) // 2


def second_star(input_lines: InputLines) -> Any:
    loop_list = build_loop(input_lines)
    loop = set(loop_list)
    animal_pipe = next(
        pipe
        for pipe, (left, right) in CONNECTIONS_MAP.items()
        if {move(loop_list[0], left), move(loop_list[0], right)}
        == {loop_list[1], loop_list[-1]}
    )

    inside_points: list[tuple[int, int]] = []
    for y, row in enumerate(input_lines):
        row = row.replace("S", animal_pipe)
        inside = False
        state = OFF_PIPE
        for x, pipe in enumerate(row):
            if (y, x) not in loop:
                if inside:
                    inside_points.append((y, x))
            else:
                state, switch = state[pipe]
                if switch:
                    inside = not inside
    return len(inside_points)


def move(address: tuple[int, int], delta: tuple[int, int]) -> tuple[int, int]:
    return (address[0] + delta[0], address[1] + delta[1])


def build_loop(input_lines: InputLines) -> list[tuple[int, int]]:
    def at(address: tuple[int, int]) -> str:
        return input_lines[address[0]][address[1]]

    def connections_from(
        address: tuple[int, int]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        left, right = CONNECTIONS_MAP[at(address)]
        return move(address, left), move(address, right)

    animal_position = next(
        (y, x)
        for y, row in enumerate(input_lines)
        for x, cell in enumerate(row)
        if cell == "S"
    )
    loop: list[tuple[int, int]] = [animal_position]
    neighbor_addresses = (
        move(animal_position, (y, x)) for (y, x) in ((-1, 0), (1, 0), (0, -1), (0, 1))
    )
    connections = (
        address
        for address in neighbor_addresses
        if animal_position in connections_from(address)
    )
    loop.append(next(connections))
    while loop[-1] != animal_position:
        loop.append(
            next(
                address for address in connections_from(loop[-1]) if address != loop[-2]
            )
        )
    return loop[:-1]


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
