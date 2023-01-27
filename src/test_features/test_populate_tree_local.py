import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
from global_binarization.file_loader import parse_input

def main():
    root = generate_tree(9)
    print(root)
    argv = sys.argv
    print(argv)
    fin = sys.argv[1]
    if len(argv) == 3:
        fin = sys.argv[1] + " " + sys.argv[2]
    thresholds, _ = parse_input(os.path.join(sys.path[0],fin))
    root = populate_tree_with_thresholds(root, thresholds)
    print(root)
if __name__ == '__main__':
    main()