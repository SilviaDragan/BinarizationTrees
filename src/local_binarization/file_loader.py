import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import threading
from commons.tree_evaluation import evaluate_tree
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
lock = threading.Lock()

NO_TREES_RETURNED = 50

def iterate_through_files():
    ths = []
    thr_f_measure = []

    # Generate one tree per file
    tree = generate_tree(9)

    with open("D:\Facultate\MPS\Proiect\src\local_binarization\\train_file.txt", 'r') as f_in:
        train_files = [line.rstrip() for line in f_in]

    for filename in train_files:
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("D:\Facultate\MPS\Proiect\src\local_binarization\MPS-Local\\" + filename, thr_f_measure, tree)
            th.start()
            ths.append(th)

    # wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure

def parse_input(local_filename):
    print(f"fin={local_filename}")
    with open(local_filename, 'r') as l_input:
        local_input = l_input.read()

    allPixels = []

    pixelsInfo = local_input.split("\n")
    for p in pixelsInfo:
        pixelThresholds = p.split(",")
        allPixels.append(pixelThresholds)

    return allPixels

class FileLoader(threading.Thread):
    def __init__(self, filename, thr_f_measure, tree):
        super(FileLoader, self).__init__()
        self.filename = filename
        self.thr_f_measure = thr_f_measure
        self.tree = tree

    def run(self):
        tree_result_map = []
        all_trees = []
        skip_current_tree = False
        print("Loading file: " + self.filename)
        all_pixels_data = parse_input(self.filename)
        print(all_pixels_data)
        for pixel in all_pixels_data:
            if len(pixel) >= 3:
                # tree resulted from one pixel -> to choose best tree on file
                pixel_measures = pixel[2:]
                pixel_class = float(pixel[1])
                pixel_value = float(pixel[0])
                tree = populate_tree_with_thresholds(self.tree, pixel_measures)
                result = evaluate_tree(tree)
                if (pixel_class == 0 and pixel_value > result >= 0) or \
                    (pixel_class == 1 and pixel_value < result <= 1):
                    all_trees.append(tree)
                    tree_result_map.append([result, tree])
        tree_result_map.sort(key=lambda a: a[0], reverse=True)
        lock.acquire()
        self.thr_f_measure = tree_result_map[:(min(NO_TREES_RETURNED, len(tree_result_map)))][1]
        lock.release()