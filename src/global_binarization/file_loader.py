import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from copy import deepcopy
import threading
from commons.tree_generation import generate_tree, populate_tree_with_thresholds

lock = threading.Lock()


def iterate_through_files(file_type):
    ths = []
    thr_f_measure = []

    # Choose the file to open based on the file_type
    if file_type == "test_file":
        file_name = "test_file.txt"
    elif file_type == "train_file":
        file_name = "train_file.txt"
    elif file_type == "validation_file":
        file_name = "validation_file.txt"
    else:
        raise ValueError("Invalid file type")

    # Read the file names from the chosen file
    with open(file_name, "r") as f:
        file_names = f.read().splitlines()

    # Iterate through the file names
    for filename in file_names:
        # Check if the file is a CSV file
        if filename.endswith(".CSV"):
            # Clone the tree and repopulate it
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)

    # Wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure

def parse_input(global_filename):
    # print(f"fin={global_filename}")

    with open(global_filename, 'r') as g_input:
        global_input = g_input.read()

    thresholds = ((global_input.split("\n"))[0]).split(",")
    f_measures = ((global_input.split("\n"))[1]).split(",")

    # print(f"thresholds= {thresholds}")
    return thresholds, f_measures


class FileLoader(threading.Thread):
    def __init__(self, filename, thr_f_measure):
        super(FileLoader, self).__init__()
        self.filename = filename
        self.thr_f_measure = thr_f_measure

    def run(self):
        thresholds, f_measures = parse_input(self.filename)
        lock.acquire()
        self.thr_f_measure.append((thresholds, f_measures))
        lock.release()
