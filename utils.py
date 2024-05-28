"""
utils.py

This module provides basic arithmetic operations including addition, subtraction,
multiplication, and division. Each function takes two integer arguments and returns
the result of the respective operation. The division function handles division by zero
by raising a ZeroDivisionError.

Functions
---------
add(a: int, b: int) -> int
    Returns the sum of a and b.
subtract(a: int, b: int) -> int
    Returns the difference between a and b.
multiply(a: int, b: int) -> int
    Returns the product of a and b.
divide(a: int, b: int) -> float
    Returns the division of a by b. Raises ZeroDivisionError if b is zero.
"""


def add(a: int, b: int) -> int:
    """
    Return the sum of a and b.

    Parameters
    ----------
    a : int
        First number to add.
    b : int
        Second number to add.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Return the difference between a and b.

    Parameters
    ----------
    a : int
        The number to be subtracted from.
    b : int
        The number to subtract.

    Returns
    -------
    int
        The difference between a and b.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Return the product of a and b.

    Parameters
    ----------
    a : int
        First number to multiply.
    b : int
        Second number to multiply.

    Returns
    -------
    int
        The product of a and b.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Return the division of a by b.

    Parameters
    ----------
    a : int
        The dividend.
    b : int
        The divisor.

    Returns
    -------
    float
        The result of the division.

    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
