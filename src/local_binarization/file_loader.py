import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from copy import deepcopy
import threading
from commons.tree_generation import generate_tree, populate_tree_with_thresholds
lock = threading.Lock()

def iterate_through_files():
    ths = []
    thr_f_measure = []
    
    tree = generate_tree(9)
    for filename in os.listdir("MPS-local"):
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("MPS-local/" + filename, thr_f_measure, tree)
            th.start()
            ths.append(th)
    # wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure

def parse_input(global_filename):
    print(f"fin={global_filename}")
    with open(global_filename, 'r') as l_input:
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
        print("Loading file: " + self.filename)
        all_pixels = parse_input(self.filename)
        #trebuie iterat si populat pentru fiecare totusi
        result = populate_tree_with_thresholds(self.tree, all_pixels[0])
        lock.acquire()
        # self.thr_f_measure.append((thresholds, f_measures))
        lock.release()
