#!/user/bin/python3
""" Module: 1-write_file """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding'utf-8') as f:
        return f.write(text)
