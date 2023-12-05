import os

from aoc.models import InputLines
from aoc.solutions.config import config


def parse_input(day: str | int, /) -> InputLines:
    if isinstance(day, int):
        path = f"{str(day).zfill(2)}.txt"
    else:
        path = day
    with open(os.path.join(config.input_dir, path)) as f:
        lines = f.read().rstrip().splitlines()
    return InputLines(lines)
