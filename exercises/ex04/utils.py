"""All(Level: Novice)."""

__author__ = "730390549"


def all(haystack: list[int], needle: int) -> bool:
    """All."""
    i: int = 0
    equal: int = 0
    if len(haystack) == 0:
        return False
    else:
        while i < len(haystack):
            if haystack[i] == needle:
                equal += 1
            i += 1
        if equal == len(haystack):
            return True
        else:
            return False


def is_equal(a: list[int], search: list[int]) -> bool:
    """Deep equality."""
    if len(a) != len(search):
        return False
    else:
        i: int = 0
        equal: int = 0
        while i < len(a):
            if a[i] == search[i]:
                equal += 1
            i += 1
        if equal == len(a):
            return True
        else:
            return False


def max(a: list[int]) -> int:
    """Max Integer."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        great: int = a[0]
        while i < len(a):
            if a[i] >= great:
                great = a[i]
            i += 1
        return great