from typing import Optional


class SomeClass:
    a: Optional[str]

    def __init__(self, a: Optional[str]) -> None:
        self.a = a

    def b(self) -> str:
        return "b"

    c = 1
