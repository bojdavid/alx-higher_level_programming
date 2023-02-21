#!/usr/bin/python3
"""
    Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
"""


class Square:
    """
        class documentation
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            returns the current square area
        """
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
            prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print("")
        else:
            a = self.__size
            for i in range(0, a):
                for j in range(0, a):
                    print('#', end='')
                print("")
