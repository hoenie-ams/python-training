"""
Demo Test Driven Development & pytest
"""

def multiply(x, y):
    result = x * y
    return result


def divide(x, y):
    result = x / y
    return round(result)


def round_up(x):
    result = int(x) + int((x > 0) and (x - int(x)) > 0)
    return result
