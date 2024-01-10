#!/usr/bin/python3
"""module that inherits from a class"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
    from the specified class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
