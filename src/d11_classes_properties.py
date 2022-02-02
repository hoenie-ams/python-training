"""
Demo of properties and their use cases
"""


class Person:
    def __init__(self, name):
        self.name = name

person = Person("Daniel")
person.name = "Danny"
print(person.name)


class Person:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, value):
        if len(value) <= 1:
            raise ValueError("Name is too short")
        self._name = value

    def get_name(self):
        return self._name

person = Person("Daniel")
person.set_name("Danny")


class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, value):
        if len(value) <= 1:
            raise ValueError("Name is too short")
        self._name = value

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

person = Person("Daniel")
person.name = "Danny"
print(person.name)


class Person:
    def __init__(self, name):
        self.name = name

    @property   # getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 1:
            raise ValueError("Name is too short")
        self._name = value

person = Person("Daniel")
person.name = "Danny"
print(person.name)
