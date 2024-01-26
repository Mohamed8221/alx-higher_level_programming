#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This is a class Square that defines a square by size and position,
       and has methods to calculate its area and print its representation.
    """
    def __init__(self, size=0, position=(0, 0)):
        """This is a method that initializes the size and
           position of the square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square in 2D space.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is a getter for size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a setter for size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This is a getter for position.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This is a setter for position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2
        or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This is a method that calculates and returns
           the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """This is a method that prints in stdout the
           square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """This is a method that returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result
