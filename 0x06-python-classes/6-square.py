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
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) == tuple and len(position) == 2:
            for i in position:
                if type(i) != int and i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            for i in value:
                if type(i) != int and i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
            prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print("")
        else:
            a = self.__size
            b = self.__position
            space = " " * b[0]
            for i in range(0, a):
                for j in range(0, a):
                    
                    print('#', end='')
                print("")
