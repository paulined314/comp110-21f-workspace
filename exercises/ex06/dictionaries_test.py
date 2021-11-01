<<<<<<< HEAD
"""Dictionaries Unit Test."""

__author__ = "730390549"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_one() -> None:
    """Invert 1."""
    a: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(a) == {"b": "a", "d": "c"}


def test_invert_two() -> None:
    """Invert 2."""
    a: dict[str, str] = {"Pauline": "Dang", "Julia": "Mata"}
    assert invert(a) == {"Dang": "Pauline", "Mata": "Julia"}


def test_invert_three() -> None:
    """Invert 3."""
    a: dict[str, str] = {"COMP": "110", "COMP SCI": "283"}
    assert invert(a) == {"110": "COMP", "283": "COMP SCI"}


def test_favorite_color_one() -> None:
    """Favorite Color 1."""
    a: dict[str, str] = {"Pauline": "blue", "Joey": "brown", "Julia": "white", "Adi": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_color_two() -> None:
    """Favorite Color 2."""
    a: dict[str, str] = {"Pauline": "blue", "Chloe": "red", "Bria": "red", "Sierra": "purple"}
    assert favorite_color(a) == "red"


def test_favorite_color_three() -> None:
    """Favorite Color 3."""
    a: dict[str, str] = {"Kathy": "yellow", "Lily": "purple"}
    assert favorite_color(a) == "yellow"


def test_count_one() -> None:
    """Count 1."""
    a: list[str] = ["blue", "blue", "blue"]
    assert count(a) == {"blue": 3}


def test_count_two() -> None:
    """Count 2."""
    a: list[str] = ["Pauline", "William", "Joey", "Joey", "Mariana"]
    assert count(a) == {"Pauline": 1, "William": 1, "Joey": 2, "Mariana": 1}


def test_count_three() -> None:
    """Count 3."""
    a: list[str] = ["Pauline", "Kayla", "Tam", "Danny"]
    assert count(a) == {"Pauline": 1, "Kayla": 1, "Tam": 1, "Danny": 1}
=======
"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"
>>>>>>> 7fee9dc6edad0a3ed524716ae227d1e6de158d67
