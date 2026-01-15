class _Node():
    __slots__ = ("value", "next")
    def __init__(self, value: any, next: _Node | None):
        self.value: any = value
        self.next: _Node | None = next
    
    def __repr__(self):
        return f"value={self.value}\nnext={self.next.value if self.next else None}"