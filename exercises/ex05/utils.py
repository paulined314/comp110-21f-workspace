"""More List Utility Functions."""

__author__ = "730390549"


def only_evens(a_list: list[int]) -> list[int]:
    """Even."""
    i: int = 0
    l_list: list[int] = []
    while i < len(a_list):
        x: int = a_list[i]
        y: int = x % 2
        if y == 0:
            l_list.append(x)
        i += 1
    return l_list


def sub(a_list: list[int], b: int, c: int) -> list[int]:
    """Cherry Picking."""
    if b < 0:
        b = 0
    if c > len(a_list):
        c = len(a_list)
    if len(a_list) == 0:
        return []
    if b == len(a_list):
        return []
    d_list: list[int] = []
    e: int = a_list[b]
    f: int = a_list[c - 1]
    d_list.append(e)
    d_list.append(f)
    return d_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Concatentation."""
    c: list[int] = []
    d: int = len(a)
    e: int = len(b)
    i: int = 0
    i2: int = 0
    while i < d:
        c.append(a[i])
        i += 1
    while i2 < e:
        c.append(b[i2])
        i2 += 1
    return c
