"""
Demo of dataclasses
"""
from dataclasses import dataclass, asdict


class RegularClassCustomer:
    """Class for a customer."""

    def __init__(self, name: str, email: str, is_active: bool = False):
        self.name = name
        self.email = email
        self.is_active = is_active


@dataclass
class DataClassCustomer:
    """Class for a customer."""
    name: str
    email: str
    is_active: bool = False


def func(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

func(100, 200, 200, "abc", debug=True, extra="graag")

