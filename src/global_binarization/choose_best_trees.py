import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import math
import copy
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
from commons.tree_evaluation import evaluate_tree

# N = 100 se misca destul de repede, 500 ceva mai mult
N = 100  # number of trees to generate
NO_LEAVES = 15  # number of leaves in each global binarization tree
MIN_F_MEASURE = 90  # minimum f-measure score for a threshold to be considered a match
NO_TREES_RETURNED = 50
NO_FINAL_TREES = 3


def choose_best_trees(files):
    best_trees = []  # unordered list of tuples (no_matches, tree)
    skip_current_tree = False  # if True, skip the current tree and generate a new one

    # generate N trees
    for i in range(N):
        skip_current_tree = False
        no_matches = 0  # number of evaluated thresholds that match with the targetted threshold
        tree_skeleton = generate_tree(NO_LEAVES)  # only has operators and no thresholds

        for j in range(len(files)):
            thresholds, f_measures = files[j]
            tree = populate_tree_with_thresholds(copy.deepcopy(tree_skeleton), thresholds)
            final_threshold = evaluate_tree(tree)

            if final_threshold < 0 or final_threshold >= 1:
                skip_current_tree = True
                break
            else:
                interval_index = math.floor(255 * final_threshold)
                f_measure_score = float(f_measures[interval_index])

                if f_measure_score > MIN_F_MEASURE:
                    no_matches += 1

        if skip_current_tree:
            continue
        # add the success rate and the tree to the list of candidate trees
        best_trees.append((no_matches / len(files), tree_skeleton))

    # sort the list of trees by the success rate in reverse order
    best_trees.sort(key=lambda a: a[0], reverse=True)
    if len(best_trees) > NO_TREES_RETURNED:
        best_trees = best_trees[:NO_TREES_RETURNED]

    return best_trees


def compare_final_trees(files, trees):
    best_trees = []  # unordered list of tuples (no_matches, tree)
    skip_current_tree = False  # if True, skip the current tree and generate a new one
    # generate N trees
    for i in range(len(trees)):
        skip_current_tree = False
        no_matches = 0  # number of evaluated thresholds that match with the targetted threshold
        tree_skeleton = trees.pop()
        print("tree skeleton", str(tree_skeleton))
        for j in range(len(files)):
            thresholds, f_measures = files[j]
            tree = populate_tree_with_thresholds(copy.deepcopy(tree_skeleton), thresholds)
            final_threshold = evaluate_tree(tree)

            if final_threshold < 0 or final_threshold >= 1:
                skip_current_tree = True
                break
            else:
                interval_index = math.floor(255 * final_threshold)
                f_measure_score = float(f_measures[interval_index])

                if f_measure_score > MIN_F_MEASURE:
                    no_matches += 1

        if skip_current_tree:
            continue
        # add the success rate and the tree to the list of candidate trees
        best_trees.append((no_matches / len(files), tree_skeleton))

    # sort the list of trees by the success rate in reverse order
    best_trees.sort(key=lambda a: a[0], reverse=True)
    if len(best_trees) > NO_FINAL_TREES:
        best_trees = best_trees[:NO_FINAL_TREES]

    return best_trees
