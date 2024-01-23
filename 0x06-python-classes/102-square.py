#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 5-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            __size (int): size of the square (1 side).
            __position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Rich comparison operator to compare if square area is less
        than another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Rich comparison operator to compare if square area is less
        than or equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Rich comparison operator to compare if square area is equal to
        another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Rich comparison operator to compare if square area is not
        equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Rich comparison operator to compare if square area is greater
        than another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Rich comparison operator to compare if square area is greater
        than or equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false
        """
        return self.__size >= other.__size
