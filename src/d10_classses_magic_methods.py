"""
Demo of magic methods
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Bank account of {self.owner}"

    def __gt__(self, other):
        return self.balance > other.balance


account_sjoerd = BankAccount("Sjoerd", 100)
account_ronald = BankAccount("Ronald", 50)

print(account_sjoerd > account_ronald)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person named {self.name}"

    def __repr__(self):
        return f'Person(name="{self.name}")'

person = Person("Brian")
print(person)