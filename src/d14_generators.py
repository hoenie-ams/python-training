"""
Demo and use cases of generators
"""

# Iterables
numbers = [1, 2, 3]
for n in numbers:
    print(n)

# Iterator: infinite counter
class MyCounter:
    def __init__(self, value=0):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.value += 1
        return value


def my_generator():
    a = "hello from A"
    yield a
    b = "hello from B"
    yield b


# infinite counter (generator)
def my_counter(value=0):
    while True:
        yield value
        value += 1

counter = my_counter(0)


ingredients = ["SPAM", "bACon", "ham", "EggS"]

# For loop
ingredients_lower = []
for i in ingredients:
    ingredients_lower.append(i.lower())
print(ingredients_lower)

# List comprehension
ingredients_lower = [i.lower() for i in ingredients]


import sys
list_comp = [x for x in range(1000000)]
generator = (x for x in range(1000000))
print(sys.getsizeof(list_comp))
print(sys.getsizeof(generator))

with open("zen.txt") as f:
    for line in f:
        print(line)
