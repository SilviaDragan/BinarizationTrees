from .node import Node

class Threshold(Node):
    _val: float

    def __init__(self, val: float):
        super().__init__()
        self._val = val

    def set_val(self, val):
        self._val = val

    def get_val(self):
        return self._val

    def __str__(self):
        return self._val.__str__()