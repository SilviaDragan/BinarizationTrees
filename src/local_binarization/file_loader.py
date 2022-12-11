import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from copy import deepcopy
import threading
from commons.tree_generation import generate_trees, populate_tree_with_thresholds
lock = threading.Lock()

tree_list = []

def iterate_through_files():
    ths = []
    thr_f_measure = []
    
    for filename in os.listdir("MPS-local"):
        print(filename)
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("MPS-local/" + filename, thr_f_measure)
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

    all_pixels_in_file = []

    pixels_info = local_input.split("\n")
    for p in pixels_info:
        pixel_data = p.split(",")
        all_pixels_in_file.append(pixel_data)

    return all_pixels_in_file

class FileLoader(threading.Thread):
    def __init__(self, filename, thr_f_measure):
        super(FileLoader, self).__init__()
        self.filename = filename
        self.thr_f_measure = thr_f_measure

    def run(self):
        print("Loading file: " + self.filename)
        all_pixels_in_file = parse_input(self.filename)
        for pixel_line in all_pixels_in_file:
            tree = generate_trees(9)
            result = populate_tree_with_thresholds(tree, pixel_line[2:])
            tree_list.append(result)
        lock.acquire()
        # self.thr_f_measure.append((thresholds, f_measures))
        lock.release()