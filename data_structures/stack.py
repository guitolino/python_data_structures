from ._node import _Node

class Stack:
    __slot__ = ("__last_node", "__length")
    def __init__(self):
        self.__last_node: _Node | None = None
        self.__length: int = 0
    
    # --- public API ---
    def push(self, value: any):
        new_node = _Node(value, self.__last_node)
        self.__last_node = new_node
        self.__length += 1
    
    @property
    def last_value(self) -> _Node | None:
        return self.__last_node 

    @property
    def length(self) -> int:
        return self.__length