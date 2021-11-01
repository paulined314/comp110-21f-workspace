"""Examples of funcations imported elsewhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print(f"helper.py: {__name__}")