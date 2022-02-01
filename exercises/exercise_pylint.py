"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""
import statistics, os


def main():
   name = input("What is your name? ")
   greet(name)


def greet(name):
    local_variable = 42
    print(f"Hello %s, how are you?" % name);
    return

def make_percentage():
    percentage = number / 100
    pass
    return f"{percentage}%"


if __name__ == "__main__":
    main()