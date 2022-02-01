"""
Demo of best practices and explanation of PEP8
"""
EUR_USD_EXCHANGE_RATE = 1.13


# Variables
var = ""
data = ""
temp = ""
list = ""
l = ""
distance = ""
fname = ""

# Good examples
number_of_children = ...
age = 42
postal_code = 2000

# Two words
# camelCase
streetName = "Main Street"
# PascalCase
StreetName = ...
# kebab-case
#street-name = ...
# snake_case
street_name = ...

# Constants
STREET_NAME = ...


# Function names
def convert(amount):
    return amount * 1.13


def convert_eur_to_usd(amount):
    return amount * EUR_USD_EXCHANGE_RATE


# Classes
class RectangleShape:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length
