import pytest
from data_structures.stack import Stack

class TestStack:
    def setup_method(self):
        self.stack = Stack()
    

    @pytest.mark.parametrize(
            ("insertions", "last_value"),
            [
        ((1, 2, 3, 4), 4,),
        ((4,53,23,121,23), 23,),
        ((), None,),
    ])
    def test_push_last_value_length(self, insertions, last_value):
        for i in insertions:
            self.stack.push(i)
        assert self.stack.last_value == last_value
        assert self.stack.length == len(insertions)
    
   
    def test_is_empty_true(self):
        assert self.stack.is_empty
    
    def test_is_empty_false(self):
        self.stack.push(10)
        assert not self.stack.is_empty