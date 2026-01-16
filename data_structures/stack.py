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
    
    def pop(self):
        if not self.__last_node:
            return None
        
        aux = self.last_value
        self.__last_node = self.__last_node.next
        return aux

    @property
    def last_value(self) -> any | None:
        return self.__last_node.value if self.__last_node else None

    @property
    def length(self) -> int:
        return self.__length
    
    # --- public API ---