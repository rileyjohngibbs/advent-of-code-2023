from aoc.solutions.day03.alpha import first_star, second_star


def test_first_star(input_one, answer_one) -> None:
    assert first_star(input_one) == answer_one


def test_second_star(input_one, answer_two) -> None:
    assert second_star(input_one) == answer_two
