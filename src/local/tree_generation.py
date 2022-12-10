#TODO: ADAPTEAZA LA LOCAL 
from enum import Enum
import random
from commons.tree_utils.add_node import Add
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.multiply_node import Multiply
from commons.tree_utils.divide_node import Divide
from commons.tree_utils.threshold_node import Threshold

N = 1 # numarul de generari random

class Operators(Enum):
    ADD = 1
    MULTIPLY = 2
    SUBTRACT = 3

ops_list = [Operators.ADD, Operators.MULTIPLY, Operators.SUBTRACT];

def get_node(op):
     match op:
        case Operators.ADD:
            return Add(None, None)
        case Operators.MULTIPLY:
            return Multiply(None, None)
        case Operators.SUBTRACT:
            return Subtract(None, None)

def populate_tree_with_thresholds(queue, thresholds):
    index = 1
    #adaugam threshold urile pe frunze (mai putin pe cel de pe nivelul 4 pe care il completaseram anterior)
    while index < 15 :
        node = queue.pop(0)
        node.set_val1(Threshold(thresholds[index]))
        index = index + 1
        node.set_val2(Threshold(thresholds[index]))
        index = index + 1
    node = queue.pop(0)
    if (node is Threshold):
        node.set_val(thresholds[0])

def generate_trees():
    for _ in range(N):
        ops = []
        for j in range(14): #adaugam operatorii i (avem nevoie de 14 pentru cele 15 valori)
            ops.append(random.choice(ops_list))

        queue = []
        index = 0
        root = get_node(ops[index])
        queue.append(root)
        index = index + 1
        # incepem sa punem in tree operatorii pana completam primele 2 nivele si aproape tot nivelul 3 si 4(fara ultimul element pe 3 si ultimele 2 pe 4)
        # ultimul element de pe nivelul 3 va fi un operator cu un si copii vor fi un alt operator si un threshold
        while index < 13 :
            node = queue.pop(0)
            node.set_val1(get_node(ops[index]))
            index = index + 1
            node.set_val2(get_node(ops[index]))
            index = index + 1
            queue.append(node.get_val1())
            queue.append(node.get_val2())

        # adaugam ultimul element pe nivelul 3 si copii lor (operator si threshold)
        node = queue.pop(0)
        node.set_val1(get_node(ops[index]))
        queue.append(node.get_val1())
        node.set_val2(Threshold(-1))
        queue.append(node.get_val2())
        return root