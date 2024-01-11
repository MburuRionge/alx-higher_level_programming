#!/usr/bin/python3
"""module for Rectangle class."""
BaseGeometry = __import__('8-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass represnting a rectangle."""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method which returns an area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """string represention method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
