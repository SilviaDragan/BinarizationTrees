from enum import Enum
import random
import sys

from binarization import Add, Multiply, Subtract, Threshold, parse_input
from tree_evaluation import evaluate_tree

N = 1 # numarul de generari random

class Operators(Enum):
    ADD = 1
    MULTIPLY = 2
    SUBTRACT = 3

ops_list = [Operators.ADD, Operators.MULTIPLY, Operators.SUBTRACT];

def get_node(op):
     match op:
        case Operators.ADD:
            return Add(None, None)
        case Operators.MULTIPLY:
            return Multiply(None, None)
        case Operators.SUBTRACT:
            return Subtract(None, None)

def populate_tree_with_thresholds(queue, thresholds):
    index = 1
    #adaugam threshold urile pe frunze (mai putin pe cel de pe nivelul 4 pe care il completaseram anterior)
    while index < 15 :
        node = queue.pop(0)
        node.set_val1(Threshold(thresholds[index]))
        index = index + 1
        node.set_val2(Threshold(thresholds[index]))
        index = index + 1

def generate_trees(thresholds):
    for i in range(N):
        ops = []
        for j in range(14): #adaugam operatorii i (avem nevoie de 14 pentru cele 15 valori)
            ops.append(random.choice(ops_list))

        queue = []
        index = 0
        root = get_node(ops[index])
        queue.append(root)
        index = index + 1
        # incepem sa punem in tree operatorii pana completam primele 2 nivele si aproape tot nivelul 3 si 4(fara ultimul element pe 3 si ultimele 2 pe 4)
        # ultimul element de pe nivelul 3 va fi un operator cu un si copii vor fi un alt operator si un threshold
        while index < 13 :
            node = queue.pop(0)
            node.set_val1(get_node(ops[index]))
            index = index + 1
            node.set_val2(get_node(ops[index]))
            index = index + 1
            queue.append(node.get_val1())
            queue.append(node.get_val2())

        # adaugam ultimul element pe nivelul 3 si copii lor (operator si threshold)
        node = queue.pop(0)
        node.set_val1(get_node(ops[index]))
        queue.append(node.get_val1())
        node.set_val2(Threshold(thresholds[1]))
        populate_tree_with_thresholds(queue, thresholds)
        
        print("tree generation")
        print(root)
    
        final_threshold = evaluate_tree(root)
        print("final_threshold")
        print(final_threshold)

def main():
    # TODO: script prin care rulam codul cu toate fisierele pe rand
    argv = sys.argv

    # deci ca sa intelegeti acesti oameni au decis sa dea numele fiserelor CU SPATIU !!!!!! DOAMNE FERESTE
    # dar nu toate fisierele din input sunt cu spatiu, doar alea cu AVE.... sme :)
    if len(argv) == 3:
        fin = sys.argv[1] + " " + sys.argv[2]
    elif len(argv) == 2:
        fin = sys.argv[1]
    thresholds = parse_input(fin)

    generate_trees(thresholds)

if __name__ == '__main__':
    # ca sa rulati adaugati ca parametri din Edit Configurations: MPS-Global/[AVE_INT] 2_1.CSV (sau oricare alt fisier)
    main()