#!/usr/bin/python3
""" Module: 11-student """


class Student:
    """
    Class Student that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance.

        Args:
            attrs (list): A list of strings
            representing attribute names. Defaults to None.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where the key is
            the public attribute name and the value is
            the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
