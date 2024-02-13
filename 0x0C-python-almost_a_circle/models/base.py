#!/usr/bin/python3
"""Module for Base class."""
import json
import os
import csv
import turtle


class Base:
    """Base class.

    Attributes:
        __nb_objects (int): The number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The identity of the instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            list_dicts = cls.from_json_string(file.read())
        return [cls.create(**dict_obj) for dict_obj in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is not None and len(list_objs) > 0:
                writer = csv.DictWriter(csvfile,
                                        list_objs[0].to_dictionary().keys())
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".csv"
        list_objs = []
        if os.path.exists(filename):
            with open(filename, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    list_objs.append(cls.create(**row))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares."""
        turtle.penup()
        turtle.speed(1)
        for rect in list_rectangles:
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.penup()

        turtle.color("red")
        for square in list_squares:
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.penup()

        turtle.done()
