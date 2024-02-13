#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x coordinate of the square.
            Defaults to 0.
            y (int, optional): The y coordinate of the square.
            Defaults to 0.
            id (int, optional): The identity of the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = self.height = value

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
