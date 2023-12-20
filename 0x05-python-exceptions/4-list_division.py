#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        Anew list of length list_length containingall the divisions.
    """

    new_list = []
    for i in range(0, list_length):

        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("Division by zero")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            new_list.append(div_result)

    return new_list
