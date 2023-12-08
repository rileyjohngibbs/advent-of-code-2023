import itertools
import math
from functools import partial
from typing import Any

from aoc.models import InputLines
from aoc.run import solve

DAY = 8


def first_star(input_lines: InputLines) -> Any:
    directions = input_lines[0]
    nodes = build_nodes(input_lines[2:])
    return steps_to_end(directions, nodes, "AAA")


def second_star(input_lines: InputLines) -> Any:
    directions = input_lines[0]
    nodes = build_nodes(input_lines[2:])
    starts = (node for node in nodes if node.endswith("A"))
    step_counts = map(partial(steps_to_end, directions, nodes), starts)
    return math.lcm(*step_counts)


def build_nodes(input_lines: list[str]) -> dict[str, tuple[str, str]]:
    nodes = {line[0:3]: (line[7:10], line[12:15]) for line in input_lines}
    return nodes


def steps_to_end(directions: str, nodes: dict[str, tuple[str, str]], start: str) -> int:
    location = start
    for steps, direction in enumerate(itertools.cycle(directions)):
        if location.endswith("Z"):
            break
        location = nodes[location][direction == "R"]
    return steps


if __name__ == "__main__":
    solve(first_star, second_star, DAY)
