from commons.tree_utils.add_node import Add
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.multiply_node import Multiply
from commons.tree_utils.divide_node import Divide
from commons.tree_utils.threshold_node import Threshold

def evaluate_tree(root):
    if root.__class__.__name__ == Threshold.__name__:
        return float(root.get_val())

    val_subtree1 = evaluate_tree(root.get_val1())
    val_subtree2 = evaluate_tree(root.get_val2())

    if root.__class__.__name__ == Add.__name__:
        return val_subtree1 + val_subtree2

    if root.__class__.__name__ == Subtract.__name__:
        return abs(val_subtree1 - val_subtree2)

    if root.__class__.__name__ == Multiply.__name__:
        return val_subtree1 * val_subtree2

    if root.__class__.__name__ == Divide.__name__:
        # avoid dividing by 0 by replacing it with  1:)
        return val_subtree1 / (val_subtree2 if val_subtree2 != 0 else 1)
