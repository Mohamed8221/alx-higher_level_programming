#!/user/bin/python3
""" Module: 1-write_file """


def write_file(filename="", text=""):
    """ Function that writes a string to a text file """

    with open(filename, 'w', encoding'utf-8') as f:
        return f.write(text)
