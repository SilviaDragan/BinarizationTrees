import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import math
import copy
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
from commons.tree_evaluation import evaluate_tree
from file_loader import iterate_through_files

N = 100 # number of trees to generate
NO_LEAVES = 15 # number of leaves in each global binarization tree
MIN_F_MEASURE = 90 # minimum f-measure score for a threshold to be considered a match

files = [] # looks like: [(thresholds-file1, f_measures-file1), (thresholds-file2, f_measures-file2), ...]
best_tree = None

def main():
    files = iterate_through_files()
    skip_current_tree = False # if True, skip the current tree and generate a new one
    max_no_matches = -1 # current maximum of matches between a threshold after tree evaluation and the targetted threshold

    # generate N trees
    for i in range(N):
        skip_current_tree = False
        no_matches = 0 # number of evaluated thresholds that match with the targetted threshold
        tree_skeleton = generate_tree(NO_LEAVES) # only has operators and no thresholds

        for j in range(len(files)):
            thresholds, f_measures = files[j]
            tree = populate_tree_with_thresholds(copy.deepcopy(tree_skeleton), thresholds)
            final_threshold = evaluate_tree(tree)

            if (final_threshold < 0 or final_threshold >= 1):
                skip_current_tree = True
                break
            else:
                interval_index = math.floor(255 * final_threshold)
                f_measure_score = float(f_measures[interval_index])

                if (f_measure_score > MIN_F_MEASURE):
                    no_matches += 1

        if (skip_current_tree == True):
            continue
            
        if (no_matches > max_no_matches):
            max_no_matches = no_matches
            best_tree = tree_skeleton

    if (best_tree == None):
        print("No tree found")
    else:
        print(f"Best tree: {best_tree} + {max_no_matches} / {len(files)}")

if __name__ == '__main__':
    main()
