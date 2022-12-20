import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from global_binarization.file_loader import get_training_files
from global_binarization.choose_best_trees import choose_best_trees


# no_runs = numarul de rulari ale lui choose_best_trees
# se vor face no_runs fisere in care avem arborii
# momentan se vor suprascrie la fiecare rulare, o sa modific eu sa pastram toate rezultatele daca vreti
def run_global(no_runs):
    files = get_training_files()

    base_filename = "best_trees_results/result"

    for i in range(no_runs):
        fname = base_filename + str(i)
        f = open(fname, "w")

        best_trees = choose_best_trees(files)
        if len(best_trees) == 0:
            print("No trees found")
        else:
            for j in range(len(best_trees)):
                # doar arborii
                f.write(str(best_trees[j][1]) + "\n")
                # format_float = "{:.3f}".format(best_trees[i][0])
                # f.write(f"Tree {i} with {format_float}% succes rate: {best_trees[i][1]}")


if __name__ == '__main__':
    argv = sys.argv
    print(argv)
    no_runs = int(argv[1])
    run_global(no_runs)
