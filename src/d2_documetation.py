"""
Demo of documentation in Python files
"""


def multiply(x, y):
    """
    Return the product of x and y.
    """
    return x * y


print(multiply.__name__)
print(multiply.__doc__)


class Rectangle:
    """
    A class used to represent a rectangle.
    """

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.length
