#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a clas"""
    return type(obj) == a_class
