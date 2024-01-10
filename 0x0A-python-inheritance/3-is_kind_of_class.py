#!/usr/bin/python3
"""Module for is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """determine if object a class or a subclass"""
    return isinstance(obj, a_class)
