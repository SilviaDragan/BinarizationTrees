from .node import Node

class Subtract(Node):
    _val1: Node
    _val2: Node

    def __init__(self, val1: Node, val2: Node):
        super().__init__()
        self._val1 = val1
        self._val2 = val2

    def __str__(self):
        return "SUB(" + self._val1.__str__() + ", " + self._val2.__str__() + ")"
        # return "  SUB\n" + "  /  \\ \n" + self._val1.__str__() + "   " + self._val2.__str__() + "\n" # ba desenatul
        # asta nu mi-a iesit facem alta functie de desenare frumos

    def set_val1(self, val):
        self._val1 = val

    def set_val2(self, val):
        self._val2 = val

    def get_val1(self):
        return self._val1

    def get_val2(self):
        return self._val2