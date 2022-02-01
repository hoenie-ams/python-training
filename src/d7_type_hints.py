"""
Demo type hints
"""
from typing import Optional, List, Dict, Union

a: int = 42
b: float = 2.0
c: bool = True
d: str = "hello world"


def add(x: int, y: int) -> int:
    return x + y


print(add(4, 5))


def greet(name: Optional[str] = None) -> str:
    if name is None:
        name = "stranger"
    return f"Hello {name}"


print(greet(100))


e: List[int] = [1, 2, 3]
f: Dict[str, float] = {"locatie": 4.8, "service": 5.0, "quality": 4.8}
g: Union[int, str] = 1
h: List[Union[int, str]] = [1, 2, "c", "d"]


class MyClass:
    value: int = 42

    def __init__(self) -> None:
        ...

    def add(self, x: int, y: int) -> int:
        return x + y
