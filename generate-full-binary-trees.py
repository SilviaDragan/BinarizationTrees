from enum import Enum
import random
import sys
import math

from binarization import Add, Multiply, Subtract, Divide, Threshold, parse_input_global, parse_input_local
from tree_evaluation import evaluate_tree

N = 1 # numarul de generari random
MIN_F_MEASURE = 90 # scorul minim pentru ca un tree sa fie considerat valid

class Operators(Enum):
    ADD = 1
    MULTIPLY = 2
    SUBTRACT = 3
    DIVIDE = 4

ops_list = [Operators.ADD, Operators.MULTIPLY, Operators.SUBTRACT, Operators.DIVIDE];

def get_node(op):
     match op:
        case Operators.ADD:
            return Add(None, None)
        case Operators.MULTIPLY:
            return Multiply(None, None)
        case Operators.SUBTRACT:
            return Subtract(None, None)
        case Operators.DIVIDE:
            return Divide(None, None)

def populate_tree_with_thresholds(queue, thresholds):
    index = 1
    #adaugam threshold urile pe frunze (mai putin pe cel de pe nivelul 4 pe care il completaseram anterior)
    while index < 15 :
        node = queue.pop(0)
        node.set_val1(Threshold(thresholds[index]))
        index = index + 1
        node.set_val2(Threshold(thresholds[index]))
        index = index + 1

def generate_trees(thresholds, f_measures):
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
        
        # print("tree generation")
        # print(root)
    
        final_threshold = evaluate_tree(root)
      
        # formula e luata din excelul cu legenda_global
        interval_index = 0
        # pentru thresholds > 1 vom iesi din tabel
        if final_threshold <= 1:
            interval_index = math.floor(255 * final_threshold)
        
        # scorul corespunzator luat de pe linia a 2 a
        f_measure_score = 0
        if (interval_index <= 255):
            f_measure_score = float(f_measures[interval_index])

        if (f_measure_score > MIN_F_MEASURE):
            print("close")
        else:
            print("bad")

def main():
    # TODO: script prin care rulam codul cu toate fisierele pe rand
    argv = sys.argv

    # deci ca sa intelegeti acesti oameni au decis sa dea numele fiserelor CU SPATIU !!!!!! DOAMNE FERESTE
    # dar nu toate fisierele din input sunt cu spatiu, doar alea cu AVE.... sme :)
    if len(argv) == 3:
        fin = sys.argv[1] + " " + sys.argv[2]
    elif len(argv) == 2:
        fin = sys.argv[1]
    
    thresholds, f_measures = parse_input_global(fin)
    generate_trees(thresholds, f_measures)

    #pixelsData = parse_input_local(fin)
    #for p in pixelsData:
    #    generate_trees(p[2:], p[1])

if __name__ == '__main__':
    # ca sa rulati adaugati ca parametri din Edit Configurations: MPS-Global/[AVE_INT] 2_1.CSV (sau oricare alt fisier)
    main()