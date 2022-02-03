"""
Demo context managers
"""

# Good
file = open("zen.txt", "w")
file.write("Simple is better than complex")
file.close()

# Better
file = open("zen.txt", "w")
try:
    file.write("Simple is better than complex")
finally:
    file.close()

# Best
with open("zen.txt", "w") as f:
    f.write("Simple is better than complex")

print(f.closed)


# Demo of context manager
class DemoContextManager:

    def __enter__(self):
        print("entering the context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting the context")



with DemoContextManager():
    print("within the context")


from contextlib import contextmanager

@contextmanager
def opened(filename, mode="r"):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with opened("zen.txt", "r") as file:
    for line in file:
        print(line)