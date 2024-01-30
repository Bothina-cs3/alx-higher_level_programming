#!/usr/bin/python3
"""Defines a function that prints a square with the character #.

Attributes:
    print_square: prints a square with the character #
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size of the square

    Raises:
        TypeError: If size is not an integer and less than 0.
        ValueError: If size is less than 0.
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError("message")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("message")

    for i in range(size):
        print("#" * size)
