from aoc.models import WordTree


def test_empty_instantiation() -> None:
    WordTree()


def test_instantiation() -> None:
    WordTree(
        branches={
            "a": WordTree(
                value="a",
                branches={"s": WordTree(value="as"), "t": WordTree(value="at")},
            )
        }
    )


def test_build_from_list() -> None:
    words = ["as", "at", "art", "a"]
    word_tree = WordTree.build(words)
    expected = WordTree(
        branches={
            "a": WordTree(
                value="a",
                branches={
                    "s": WordTree(value="as"),
                    "t": WordTree(value="at"),
                    "r": WordTree(branches={"t": WordTree(value="art")}),
                },
            )
        }
    )
    assert word_tree == expected


def test_build_from_list_of_tuples() -> None:
    words: list[tuple[str, int]] = [
        ("two", 2),
        ("twenty", 20),
        ("sixty", 60),
        ("six", 6),
    ]
    word_tree = WordTree.build(words)
    expected = WordTree(
        branches={
            "s": WordTree(
                branches={
                    "i": WordTree(
                        branches={
                            "x": WordTree(
                                value=6,
                                branches={
                                    "t": WordTree(branches={"y": WordTree(value=60)})
                                },
                            )
                        }
                    )
                }
            ),
            "t": WordTree(
                branches={
                    "w": WordTree(
                        branches={
                            "o": WordTree(value=2),
                            "e": WordTree(
                                branches={
                                    "n": WordTree(
                                        branches={
                                            "t": WordTree(
                                                branches={"y": WordTree(value=20)}
                                            )
                                        }
                                    )
                                }
                            ),
                        }
                    )
                }
            ),
        }
    )
    assert word_tree == expected


def test_lookup() -> None:
    word_tree = WordTree.build(["as", "at", "art", "a"])
    assert list(word_tree.lookup("arta")) == ["a", "art"]


def test_lookup_all() -> None:
    seed_words = ["war", "wart", "hog", "art", "tho"]
    word_tree = WordTree.build(seed_words + ["herring"])
    actual = sorted(word_tree.lookup_all("warthog"))
    expected = sorted(seed_words)
    assert actual == expected
