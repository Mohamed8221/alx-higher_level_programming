#!/usr/bin/python3
import math


class MagicClass:
    """This is a class MagicClass that defines a
     circle by radius and has methods to calculate its area and circumference.
    """
    def __init__(self, radius=0):
        """This is a method that initializes the radius of the circle.

        Args:
            radius (int or float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This is a method that calculates and
           returns the current circle area.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This is a method that calculates and returns
           the current circle circumference.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
