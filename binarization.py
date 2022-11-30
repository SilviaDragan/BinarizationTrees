import sys
import random
from typing import Set, Dict, Tuple, List


class Node:
    def __init__(self):
        pass


class Threshold(Node):
    _val: float

    def __init__(self, val: float):
        super().__init__()
        self._val = val

    def set_val(self, val):
        self._val = val

    def get_val(self):
        return self._val

    def __str__(self):
        return self._val.__str__()

""" TODO: adauga/scoate operatii in acealasi stil ca astea existente"""
class Add(Node):
    _val1: Node
    _val2: Node

    def __init__(self, val1: Node, val2: Node):
        super().__init__()
        self._val1 = val1
        self._val2 = val2

    def __str__(self):
        return "ADD(" + self._val1.__str__() + ", " + self._val2.__str__() + ")" # reprezentare lininara
        # return "  ADD\n" + "  /  \\ \n" + self._val1.__str__() + "   " + self._val2.__str__() + "\n" # ba desenatul asta nu mi-a iesit facem alta functie de desenare frumos
    
    def set_val1(self, val):
        self._val1 = val

    def set_val2(self, val):
        self._val2 = val

    def get_val1(self):
        return self._val1

    def get_val2(self):
        return self._val2
    

class Multiply(Node):
    _val1: Node
    _val2: Node

    def __init__(self, val1: Node, val2: Node):
        super().__init__()
        self._val1 = val1
        self._val2 = val2

    def __str__(self):
        return "MUL(" + self._val1.__str__() + ", " + self._val2.__str__() + ")"
        # return "  MUL\n" + "  /  \\ \n" + self._val1.__str__() + "   " + self._val2.__str__() + "\n"
    def set_val1(self, val):
        self._val1 = val

    def set_val2(self, val):
        self._val2 = val

    def get_val1(self):
        return self._val1

    def get_val2(self):
        return self._val2


"""Mi-e frica ca asta o sa faca evaluarea sa dea cu minus
Oh well anyway
"""
class Subtract(Node):
    _val1: Node
    _val2: Node

    def __init__(self, val1: Node, val2: Node):
        super().__init__()
        self._val1 = val1
        self._val2 = val2

    def __str__(self):
        return "SUB(" + self._val1.__str__() + ", " + self._val2.__str__() + ")"
        # return "  SUB\n" + "  /  \\ \n" + self._val1.__str__() + "   " + self._val2.__str__() + "\n" # ba desenatul asta nu mi-a iesit facem alta functie de desenare frumos
    
    def set_val1(self, val):
        self._val1 = val

    def set_val2(self, val):
        self._val2 = val
    
    def get_val1(self):
        return self._val1

    def get_val2(self):
        return self._val2

def build_mock_tree(thresholds):
    # model de alegere operatie random:
    # operations = ["ADD", "MULTIPLY", "SUBTRACT"]
    # op = random.choice(operations)
    # if op == "ADD":
    # return Add(Threshold(t1), Threshold(t2))
    return Add(
            Multiply(Add(Multiply(thresholds[0], thresholds[1]), Add(thresholds[2], thresholds[3])),
                        Multiply(Subtract (thresholds[4], thresholds[5]), Add(thresholds[6], thresholds[7])))
            ,Subtract(Multiply(Add(thresholds[8], thresholds[9]), Multiply(thresholds[10],thresholds[11])),
                      Subtract(Add(thresholds[12], thresholds[13]), Add(thresholds[14], thresholds[15]))))


def parse_input(global_filename):
    """Momentan doar pentru global"""
    print(f"fin={global_filename}")
    with open(global_filename, 'r') as g_input:
        global_input = g_input.read()

    thresholds = ((global_input.split("\n"))[0]).split(",")
    print(f"thresholds= {thresholds}")

    # nu mai tin minte la ce folosea asta asa ca nu stiu ce nume sa ii dau
    ceva_urmatoarea_linie = ((global_input.split("\n"))[1]).split(",")
    return thresholds


def main():
    # TODO: script prin care rulam codul cu toate fisierele pe rand
    argv = sys.argv
    print(argv)

    # deci ca sa intelegeti acesti oameni au decis sa dea numele fiserelor CU SPATIU !!!!!! DOAMNE FERESTE
    # dar nu toate fisierele din input sunt cu spatiu, doar alea cu AVE.... sme :)
    if len(argv) == 3:
        fin = sys.argv[1] + " " + sys.argv[2]
    elif len(argv) == 2:
        fin = sys.argv[1]
    thresholds = parse_input(fin)

    # print(build_mock_tree(thresholds))
    # print(Add(Threshold(1.5), Threshold(2.4)))

if __name__ == '__main__':
    # ca sa rulati adaugati ca parametri din Edit Configurations: MPS-Global/[AVE_INT] 2_1.CSV (sau oricare alt fisier)
    main()
