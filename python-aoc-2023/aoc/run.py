import datetime as dt
from collections.abc import Iterator
from contextlib import contextmanager

from aoc.models import Solution
from aoc.solutions.config import config
from aoc.solutions.helpers import parse_input


@contextmanager
def noop() -> Iterator[None]:
    yield None


@contextmanager
def timer() -> Iterator[None]:
    start = dt.datetime.now()
    yield
    end = dt.datetime.now()
    print(end - start)


def solve(first_star: Solution, second_star: Solution, day: str | int) -> None:
    ctx = timer() if config.time_execution else noop()
    with ctx:
        input_lines = parse_input(day)
        print(first_star(input_lines))
        print(second_star(input_lines))
