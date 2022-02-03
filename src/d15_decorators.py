"""
Demo of decorators. Examples:
@classmethod
@staticmethod
@property
"""

def say_hello():
    print("hello, how are you?")
    return None

# 1. Functions as objects
greet = say_hello
greet()


# 2. Functions as arguments
def my_simple_decorator(func):
    print("decorating the function")
    func()

my_simple_decorator(say_hello)


def my_decorator(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    return wrapper


say_hello = my_decorator(say_hello)
say_hello()


@my_decorator
def say_hello():
    print("hello, how are you?")

say_hello()

@my_decorator
def say_bye():
    print("bye bye")

say_bye()
