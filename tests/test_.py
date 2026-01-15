import pytest
from data_structures.stack import Stack

class TestStack:
    def setup_method(self):
        self.stack = Stack()
    

    @pytest.mark.parametrize(
            ("insertions", "last_value", "next_value"),
            [
        ((1, 2, 3, 4), 4, 3)
    ])
    def test_push(self, insertions, last_value, next_value):
        for i in insertions:
            self.stack.push(i)
        assert self.stack.last_value.value == last_value
        assert self.stack.last_value.next.value == next_value
        assert self.stack.length == len(insertions)