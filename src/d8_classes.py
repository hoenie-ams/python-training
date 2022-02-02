"""
Demo of classes & objects
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 20)


class Square(Rectangle):
    def __init__(self, length):
        # Rectangle.__init__(self, length, length)
        super().__init__(length, length)  # replaces the previous line


class BankAccount:
    def __init__(self, owner: str, balance: int = 0, account_number="8888"):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance = self.balance + amount

    def withdraw(self, amount: int):
        self.balance = self.balance - amount

    def show_balance(self):
        print(f"{self.owner} has EUR {self.balance}.")


class Parent:
    ...

class Child(Parent):
    ...


class Vehicle:
    def brake(self):
        return "Braking!"

    def drive(self):
        return "Let's go"


class Car(Vehicle):
    wheels = 4


class Truck(Vehicle):
    wheels = 8


