# TODO NU mai functioneaza, o sa ii fac un update
import random
from enum import Enum

from commons.tree_utils.add_node import Add
from commons.tree_utils.multiply_node import Multiply
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.threshold_node import Threshold


class Operators(Enum):
    ADD = 1
    MULTIPLY = 2
    SUBTRACT = 3


ops_list = [Operators.ADD, Operators.MULTIPLY, Operators.SUBTRACT]


def get_node(op):
    if op == Operators.ADD:
        return Add(None, None)
    if op == Operators.MULTIPLY:
        return Multiply(None, None)
    if op == Operators.SUBTRACT:
        return Subtract(None, None)


def populate_tree_with_thresholds(root, thresholds):
    queue = []
    index = 0
    queue.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        if isinstance(node, Threshold):
            node.set_val(thresholds[index])
            index += 1
        else:
            queue.append(node.get_val1())
            queue.append(node.get_val2())
    return root


def generate_tree(number_of_thresholds):
    ops = []
    for _ in range(number_of_thresholds - 1):
        ops.append(random.choice(ops_list))

    queue = []
    index = 0
    root = get_node(ops[index])
    number_of_thresholds_available = 2
    queue.append(root)
    index += 1

    while len(queue) != 0:
        node = queue.pop(0)
        if number_of_thresholds_available < number_of_thresholds:
            node.set_val1(get_node(ops[index]))
            index += 1
            number_of_thresholds_available += 1
            queue.append(node.get_val1())

            if number_of_thresholds_available < number_of_thresholds:
                node.set_val2(get_node(ops[index]))
                index += 1
                number_of_thresholds_available += 1
                queue.append(node.get_val2())
            else:
                node.set_val2(Threshold(-1))

        else:
            node.set_val1(Threshold(-1))
            node.set_val2(Threshold(-1))
    return root
