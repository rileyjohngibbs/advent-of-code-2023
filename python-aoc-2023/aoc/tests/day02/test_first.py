from aoc.solutions.day02.first import first_star, second_star


def test_first_star(example_input, example_output) -> None:
    assert first_star(example_input) == example_output


def test_second_star(example_input, example_output_two) -> None:
    assert second_star(example_input) == example_output_two
