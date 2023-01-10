import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from commons.tree_utils.divide_node import Divide
from global_binarization.choose_best_trees import compare_final_trees

from global_binarization.file_loader import get_test_files
from commons.tree_utils.add_node import Add
from commons.tree_utils.subtract_node import Subtract
from commons.tree_utils.multiply_node import Multiply
from commons.tree_utils.threshold_node import Threshold


def build_tree(tree_list):
    while tree_list:
        current = tree_list.pop()
        if current == "ADD":
            return Add(build_tree(tree_list), build_tree(tree_list))
        elif current == "MUL":
            return Multiply(build_tree(tree_list), build_tree(tree_list))
        elif current == "SUB":
            return Subtract(build_tree(tree_list), build_tree(tree_list))
        elif current == "DIV":
            return Divide(build_tree(tree_list), build_tree(tree_list))
        else:
            return Threshold(current)


def parse_trees_from_file(filename):
    with open(filename, 'r') as fin:
        trees_str = [list(reversed(line.split(" "))) for line in fin]
    trees_parsed = []
    for tree in trees_str:
        t = build_tree(tree)
        trees_parsed.append(t)

    return trees_parsed


def choose_final_trees():
    test_files = get_test_files()
    trees = []

    for filename in os.listdir("best_trees_results"):
        trees.append(parse_trees_from_file("best_trees_results/" + filename))

    winners = compare_final_trees(test_files, trees)
    f = open("winners/winners", "w")
    for w in winners:
        format_float = "{:.3f}".format(w[0])
        f.write(str(w[1]) + " ")
        f.write(f"Tree {w[1]} with {format_float}% success rate")


if __name__ == '__main__':
    choose_final_trees()
