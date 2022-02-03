"""
Demo of decorators. Examples:
@classmethod
@staticmethod
@property
"""

# def say_hello():
#     print("hello, how are you?")
#     return None
#
# # 1. Functions as objects
# greet = say_hello
# greet()
#
#
# # 2. Functions as arguments
# def my_simple_decorator(func):
#     print("decorating the function")
#     func()
#
# my_simple_decorator(say_hello)
#
#
# def my_decorator(func):
#     def wrapper():
#         print("before calling the function")
#         func()
#         print("after calling the function")
#     return wrapper
#
#
# say_hello = my_decorator(say_hello)
# say_hello()
#
#
# @my_decorator
# def say_hello():
#     print("hello, how are you?")
#
# say_hello()
#
# @my_decorator
# def say_bye():
#     print("bye bye")
#
# say_bye()

import time
from functools import wraps

def timer(func):
    print(func)
    def wrapper():
        """"""
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        print(f'Run time was {end_time-start_time} seconds.')
        return result
    return wrapper  # callable


@timer
def do_something():
    """Toy function to keep Python busy"""
    "-".join(str(n) for n in range(1000))


do_something()


do_something = timer(do_something)

