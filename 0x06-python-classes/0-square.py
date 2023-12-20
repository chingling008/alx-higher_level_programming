#!/usr/bin/python3
"""This is code prints a makes a empty Square """

class Square:
    """An empty class Square."""
    pass


if __name__ == '__main__':
    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
