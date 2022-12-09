import os
import threading
lock = threading.Lock()
import tree_generator
from binarization import parse_input

def iterate_through_files():
    ths = []
    thr_f_measure = []
    for filename in os.listdir("MPS-global"):
        if filename.endswith(".CSV"):
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)
    # wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure

class FileLoader(threading.Thread):
    def __init__(self, filename, thr_f_measure):
        super(FileLoader, self).__init__()
        self.filename = filename
        self.thr_f_measure = thr_f_measure

    def run(self):
        print("Loading file: " + self.filename)
        thresholds, f_measures = parse_input(self.filename)
        lock.acquire()
        self.thr_f_measure.append((thresholds, f_measures))
        lock.release()
        tree_generator.generate_trees(thresholds)
