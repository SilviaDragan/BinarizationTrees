import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
from commons.tree_evaluation import evaluate_tree
from file_loader import iterate_through_files

data = []

def main():
    data = iterate_through_files()

if __name__ == '__main__':
    main()
