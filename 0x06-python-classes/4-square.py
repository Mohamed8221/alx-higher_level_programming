#!/usr/bin/python3
class Square:
    """This is a class Square that defines a square by size and has a method
       to calculate its area.
    """
    def __init__(self, size=0):
        """This is a method that initializes the size of the square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

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

    def area(self):
        """This is a method that calculates and returns the
           current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
