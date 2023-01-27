import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import threading

lock = threading.Lock()


def iterate_through_files():
    ths = []
    thr_f_measure = []

    for filename in os.listdir("MPS-Global"):
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)

    # wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure


def get_training_files():
    ths = []
    thr_f_measure = []

    with open("train_file.txt", 'r') as f_in:
        train_files = [line.rstrip() for line in f_in]

    for filename in train_files:
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)

    # wait for all threads to finish
    for th in ths:
        th.join()
    return thr_f_measure


def get_test_files():
    ths = []
    thr_f_measure = []

    with open("test_file.txt", 'r') as f_in:
        train_files = [line.rstrip() for line in f_in]

    for filename in train_files:
        if filename.endswith(".CSV"):
            # trebuie sa clonam tree ul la fiecare folosire, si sa refacem si popularea sa nu mai tina cont de coada
            th = FileLoader("MPS-Global/" + filename, thr_f_measure)
            th.start()
            ths.append(th)

    # wait for all threads to finish
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
