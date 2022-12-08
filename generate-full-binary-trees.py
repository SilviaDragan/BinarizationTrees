import os
from asyncio import Lock
from enum import Enum
import random
import sys
import math

from binarization import Add, Multiply, Subtract, Divide, Threshold, parse_input
from file_loader import FileLoader
from tree_evaluation import evaluate_tree

N = 1  # numarul de generari random
MIN_F_MEASURE = 90  # scorul minim pentru ca un tree sa fie considerat valid
lock = Lock()
thr_f_measure = []
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



def iterate_through_files():
    ths = []
    for filename in os.listdir("MPS-global"):
        if filename.endswith(".CSV"):
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)
    # wait for all threads to finish
    for th in ths:
        th.join()


def main():
    # TODO: script prin care rulam codul cu toate fisierele pe rand
    iterate_through_files()
    for thresholds, f_measures in thr_f_measure:
        print("thresholds: " + str(thresholds) + " f_measures: " + str(f_measures))

if __name__ == '__main__':
    # ca sa rulati adaugati ca parametri din Edit Configurations: MPS-Global/[AVE_INT] 2_1.CSV (sau oricare alt fisier)
    main()
