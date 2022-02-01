"""
Demo Test Driven Development & pytest
"""

def multiply(x, y):
    result = x * y
    return result


def divide(x, y):
    result = x / y
    return round(result, 1)


def round_up(x):
    result = int(x) + int((x > 0) and (x - int(x)) > 0)
    return result


def hypotenuse(a, b):
    import math
    return math.sqrt(a ** 2 + b ** 2)
