import os

from file_loader import FileLoader


# Function that iterates through all files from MPS-global folder
def iterate_through_files():
    ths = []
    for filename in os.listdir("MPS-global"):
        if filename.endswith(".CSV"):
            th = FileLoader("MPS-Global/" + filename)
            th.start()
            ths.append(th)
    # wait for all threads to finish
    for th in ths:
        th.join()


def main():
    iterate_through_files()


if __name__ == '__main__':
    main()
