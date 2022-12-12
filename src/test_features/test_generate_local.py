import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from commons.tree_generation import generate_tree

def main():
    root = generate_tree(9)
    print(root)
if __name__ == '__main__':
    main()