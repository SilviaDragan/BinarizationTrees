import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from global_binarization.file_loader import get_test_files
from global_binarization.choose_best_trees import choose_best_trees
from commons.tree_utils.add_node import Add
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.multiply_node import Multiply
from commons.tree_utils.threshold_node import Threshold

# TODO: REDO THIS
# NU MERGE TREBUIE SA REFAC :(
def build_tree_from_str(tree):
    if tree[0] == 'A':
        tree = tree[4:-1]
        lr = tree.split(',')
        print(lr)
        return Add(build_tree_from_str(lr[0]), build_tree_from_str(lr[1]))
    if tree[0] == 'S':
        print("sub", tree)
        tree = tree[4:-1]
        lr = tree.split(',')
        print(lr)
        return Subtract(build_tree_from_str(lr[0]), build_tree_from_str(lr[1]))
    if tree[0] == 'M':
        tree = tree[4:-1]
        lr = tree.split(',')
        print(lr)
        return Multiply(build_tree_from_str(lr[0]), build_tree_from_str(lr[1]))
    else:
        print(tree)
        return Threshold(tree)


def parse_trees_from_file(filename):
    with open(filename, 'r') as fin:
        trees_str = [line.rstrip() for line in fin]
    trees_parsed = []
    for tree in trees_str:
        t = build_tree_from_str(tree)
        trees_parsed.append(t)
        print(str(t))

    return trees_parsed



def choose_final_trees():
    test_files = get_test_files()
    trees = []

    # parse_trees_from_file("best_trees_results/tmp")

    for filename in os.listdir("best_trees_results"):
        parse_trees_from_file("best_trees_results/" + filename)
        trees.append()

    for f in test_files:
        # TODO: evaluate trees on test files and choose finals
        pass


if __name__ == '__main__':
    choose_final_trees()
