import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from global_binarization.file_loader import parse_input

def main():
    # TODO: script prin care rulam codul cu toate fisierele pe rand
    argv = sys.argv
    print(argv)

    # deci ca sa intelegeti acesti oameni au decis sa dea numele fiserelor CU SPATIU !!!!!! DOAMNE FERESTE
    # dar nu toate fisierele din input sunt cu spatiu, doar alea cu AVE.... sme :)
    fin = sys.argv[1]
    if len(argv) == 3:
        fin = sys.argv[1] + " " + sys.argv[2]
    thresholds, _ = parse_input(os.path.join(sys.path[0],fin))
    print(thresholds)

if __name__ == '__main__':
    main()