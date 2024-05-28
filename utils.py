"""
utils.py

This module provides basic arithmetic operations including addition, subtraction,
multiplication, and division. Each function takes two integer arguments and returns
the result of the respective operation. The division function handles division by zero
by raising a ZeroDivisionError.

Functions
---------
add(first_num: int, second_num: int) -> int
    Returns the sum of first_num and second_num.
subtract(first_num: int, second_num: int) -> int
    Returns the difference between first_num and second_num.
multiply(first_num: int, second_num: int) -> int
    Returns the product of first_num and second_num.
divide(first_num: int, second_num: int) -> float
    Returns the division of first_num by second_num. Raises ZeroDivisionError if second_num is zero.
"""


def add(first_num: int, second_num: int) -> int:
    """
    Return the sum of first_num and second_num.

    Parameters
    ----------
    first_num : int
        First number to add.
    second_num : int
        Second number to add.

    Returns
    -------
    int
        The sum of first_num and second_num.
    """
    return first_num + second_num


def subtract(first_num: int, second_num: int) -> int:
    """
    Return the difference between first_num and second_num.

    Parameters
    ----------
    first_num : int
        The number to be subtracted from.
    second_num : int
        The number to subtract.

    Returns
    -------
    int
        The difference between first_num and second_num.
    """
    return first_num - second_num


def multiply(first_num: int, second_num: int) -> int:
    """
    Return the product of first_num and second_num.

    Parameters
    ----------
    first_num : int
        First number to multiply.
    second_num : int
        Second number to multiply.

    Returns
    -------
    int
        The product of first_num and second_num.
    """
    return first_num * second_num


def divide(first_num: int, second_num: int) -> float:
    """
    Return the division of first_num by second_num.

    Parameters
    ----------
    first_num : int
        The dividend.
    second_num : int
        The divisor.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ZeroDivisionError
        If second_num is zero.
    """
    if second_num == 0:
        raise ZeroDivisionError("division by zero")
    return first_num / second_num
