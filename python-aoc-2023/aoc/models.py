from collections.abc import Callable, Iterable, Iterator
from enum import IntEnum
from itertools import chain
from typing import Any, Generic, NewType, TypedDict, TypeVar, overload

from pydantic import BaseModel, Field

InputLines = NewType("InputLines", list[str])
Solution = Callable[[InputLines], Any]


class DigitName(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


T = TypeVar("T")


class NoValue(BaseModel):
    pass


NO_VALUE = NoValue()


TreeDict = dict[str, "TreeDict"]


class TreeValues(TypedDict, Generic[T]):
    value: T | NoValue
    branches: dict[str, "TreeValues[T]"]


class WordTree(BaseModel, Generic[T]):
    value: T | NoValue = NO_VALUE
    branches: dict[str, "WordTree[T]"] = Field(default_factory=dict)

    @overload
    @classmethod
    def build(cls, words: Iterable[str]) -> "WordTree[str]":
        ...

    @overload
    @classmethod
    def build(cls, words: Iterable[tuple[str, T]]) -> "WordTree[T]":
        ...

    @classmethod
    def build(
        cls,
        words: Iterable[str] | Iterable[tuple[str, T]],
    ) -> "WordTree[str] | WordTree[T]":
        tree: TreeValues[T | str] = {"value": NO_VALUE, "branches": {}}
        for word in words:
            value: str | T
            if isinstance(word, tuple):
                word, value = word
            else:
                value = word
            leaf = tree
            for letter in word:
                leaf = leaf.setdefault("branches", {}).setdefault(
                    letter, {"value": NO_VALUE, "branches": {}}
                )
            leaf["value"] = value
        return WordTree.model_validate(tree)  # type: ignore

    def lookup(self, string: str) -> Iterator[T]:
        branch = self
        for character in string:
            if character not in branch.branches:
                break
            branch = branch.branches[character]
            if not isinstance(branch.value, NoValue):
                yield branch.value

    def lookup_all(self, string: str) -> Iterator[T]:
        return chain(*(self.lookup(string[left:]) for left in range(len(string))))


class GridCell(BaseModel, Generic[T]):
    y: int
    x: int
    value: T


class Grid(Generic[T]):
    grid: list[list[T]]
    height: int
    width: int

    def __init__(self, grid: Iterable[Iterable[T]]) -> None:
        self.grid = [[c for c in r] for r in grid]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def value(self, y: int, x: int) -> T:
        return self.grid[y][x]

    def neighbors(
        self, y: int, x: int, include_center: bool = False
    ) -> Iterator[GridCell[T]]:
        return (
            GridCell(y=y_, x=x_, value=self.value(y_, x_))
            for y_ in range(max(0, y - 1), min(self.height, y + 2))
            for x_ in range(max(0, x - 1), min(self.width, x + 2))
            if include_center or y_ != y or x_ != x
        )

    def __iter__(self) -> Iterator[GridCell[T]]:
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                yield GridCell(y=y, x=x, value=value)
