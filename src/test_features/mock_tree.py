from commons.tree_utils.add_node import Add
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.multiply_node import Multiply


def build_mock_tree(thresholds):
    # model de alegere operatie random:
    # operations = ["ADD", "MULTIPLY", "SUBTRACT"]
    # op = random.choice(operations)
    # if op == "ADD":
    # return Add(Threshold(t1), Threshold(t2))
    return Add(
        Multiply(Add(Multiply(thresholds[0], thresholds[1]), Add(thresholds[2], thresholds[3])),
                 Multiply(Subtract(thresholds[4], thresholds[5]), Add(thresholds[6], thresholds[7])))
        , Subtract(Multiply(Add(thresholds[8], thresholds[9]), Multiply(thresholds[10], thresholds[11])),
                   Subtract(Add(thresholds[12], thresholds[13]), Add(thresholds[14], thresholds[15]))))