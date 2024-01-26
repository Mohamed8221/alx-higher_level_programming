#!/usr/bin/python3
""" Square module """


class Node:
    """This is a class Node that defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """This is a method that initializes the data
           and next_node of the node.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the linked list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node
            is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is a getter for data.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """This is a setter for data.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """This is a getter for next_node.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This is a setter for next_node.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """This is a class SinglyLinkedList that defines a singly linked list.
    """
    def __init__(self):
        """This is a method that initializes the head of the linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """This is a method that inserts a new Node
           into the correct sorted position in the list.

        Args:
            value (int): The data of the new node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """This is a method that returns a string
           representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        current = self.__head
        result = ""
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
