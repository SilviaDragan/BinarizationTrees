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
def build_tree(tree_list):
    while tree_list:
        current = tree_list.pop()
        if current == "ADD":
            return Add(build_tree(tree_list), build_tree(tree_list))
        elif current == "MUL":
            return Multiply(build_tree(tree_list), build_tree(tree_list))
        elif current == "SUB":
            return Subtract(build_tree(tree_list), build_tree(tree_list))
        else:
            return Threshold(current)


def parse_trees_from_file(filename):
    with open(filename, 'r') as fin:
        trees_str = [list(reversed(line.split(" "))) for line in fin]
    trees_parsed = []
    for tree in trees_str:
        t = build_tree(tree)
        trees_parsed.append(t)
        print(str(t))

    return trees_parsed


def choose_final_trees():
    test_files = get_test_files()
    trees = []

    for filename in os.listdir("best_trees_results"):
        trees.append(parse_trees_from_file("best_trees_results/" + filename))

    for f in test_files:
        # TODO: evaluate trees on test files and choose finals
        pass


if __name__ == '__main__':
    choose_final_trees()
