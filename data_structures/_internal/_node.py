from typing import Any

class _Node():
    __slots__ = ("value", "next")
    def __init__(self, value: Any, next: _Node | None) -> None:
        self.value: Any = value
        self.next: _Node | None = next
    
    def __repr__(self) -> str:
        return f"value={self.value}\nnext={self.next.value if self.next else None}"