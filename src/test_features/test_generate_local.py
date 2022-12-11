import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from commons.tree_generation import generate_trees

def main():
    root = generate_trees(9)
    print(root)
if __name__ == '__main__':
    main()