#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: size of the Square
            """
            self.__size = size

            if not isinstance(size, init):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

