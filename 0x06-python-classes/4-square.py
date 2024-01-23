#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: size of the Square
            """
            self.__size = size

    def area(self):
        """Calulates the area of Square.

        Returns: the current Square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns: the size of a Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter for size.


        Args:
            value (int): size of a Square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
