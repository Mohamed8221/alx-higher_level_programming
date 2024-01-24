#!/usr/bin/python3
class Square:
    """This is a class Square that defines a square by
       size and has a method to calculate its area.
    """
    def __init__(self, size=0):
        """This is a method that initializes the size of the square.

        Args:
            size (int or float): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """This is a getter for size.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a setter for size.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This is a method that calculates and returns
           the current square area.

        Returns:
            int or float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """This is a method that checks if two squares are equal in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are equal in area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """This is a method that checks if two squares are not equal in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """This is a method that checks if a square is
           less than another square in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is less than the
            other square in area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """This is a method that checks if a square is less
           than or equal to another square in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is less than or equal to
            the other square in area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """This is a method that checks if a square is
           greater than another square in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is greater than the
            other square in area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """This is a method that checks if a square is
           greater than or equal to another square in area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square is greater than or
            equal to the other square in area, False otherwise.
        """
        return self.area() >= other.area()
