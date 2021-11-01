<<<<<<< HEAD
"""More List Utility Functions."""

__author__ = "730390549"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_1() -> None:
    """Even Test."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_2() -> None:
    """Even Test."""
    a_list: list[int] = [1, 5, 3]
    assert only_evens(a_list) == []


def test_only_evens_3() -> None:
    """Even Test."""
    a_list: list[int] = [4, 4, 4]
    assert only_evens(a_list) == [4, 4, 4]


def test_sub_1() -> None:
    """Cerry Picking Test."""
    a_list = [10, 20, 30, 40]
    b = 1
    c = 3
    assert sub(a_list, b, c) == [20, 30]


def test_sub_2() -> None:
    """Cerry Picking Test."""
    a_list = [10, 20, 30, 40]
    b = 1
    c = 2
    assert sub(a_list, b, c) == [20, 20]


def test_sub_3() -> None:
    """Cerry Picking Test."""
    a_list = [10, 20, 30, 40]
    b = 0
    c = 3
    assert sub(a_list, b, c) == [10, 30]


def test_concat_1() -> None:
    """Concatentation Test."""
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Concatentation Test."""
    a = [1, 2]
    b = [4, 5]
    assert concat(a, b) == [1, 2, 4, 5]


def test_concat_3() -> None:
    """Concatentation Test."""
    a = [1, 2, 3]
    b = [4]
    assert concat(a, b) == [1, 2, 3, 4]
=======
"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"
>>>>>>> 7fee9dc6edad0a3ed524716ae227d1e6de158d67
