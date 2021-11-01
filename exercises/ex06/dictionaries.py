"""Dictionaries."""

__author__ = "730390549"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert."""
    invert_a: dict[str, str] = {}
    for key in a:
        invert_a[a[key]] = key
    if len(a) > len(invert_a):
        raise KeyError("You have a double!")
    return invert_a
    

def favorite_color(a: dict[str, str]) -> str:
    """Favorite Color."""
    color_counter: dict[str, int] = {}
    for key in a:
        if a[key] in color_counter:
            color_counter[a[key]] += 1
        else:
            color_counter[a[key]] = 1
    great: int = 0
    fav_color: str = ""
    for key in color_counter:
        if color_counter[key] > great:
            great = color_counter[key]
            fav_color = key
    return fav_color


def count(a: list[str]) -> dict[str, int]:
    """Count."""
    counter: dict[str, int] = {}
    for item in a:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter