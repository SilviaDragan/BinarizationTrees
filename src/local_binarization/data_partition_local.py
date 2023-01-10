import os
from random import shuffle
from math import trunc


def shuffle_data(files):
    # Amestecam datele
    new_list = list(files)
    shuffle(new_list)
    return new_list


def get_train_files(files):
    # Luam 70% din lista
    index = trunc(0.7 * len(files))
    return files[:index]


def get_validation_files(files):
    # Luam urmatorii 25%
    index = trunc(0.7 * len(files))
    index1 = trunc(0.95 * len(files))
    return files[index:index1]


def get_test_files(files):
    # Luam ultimii 5%
    index = trunc(0.95 * len(files))
    return files[index:]


def file_writer(name_list, file_to_write):
    for line in name_list:
        file_to_write.write(f"{line}\n")


def main():
    files_list = []
    for filename in os.listdir("MPS-Local"):
        if filename.endswith(".CSV"):
            files_list.append(filename)
    shuffled_files_list = shuffle_data(files_list)

    train_files_list = get_train_files(shuffled_files_list)
    train_file = open("train_file.txt", "w")
    file_writer(train_files_list, train_file)

    validation_files_list = get_validation_files(shuffled_files_list)
    validation_file = open("validation_file.txt", "w")
    file_writer(validation_files_list, validation_file)

    test_files_list = get_test_files(shuffled_files_list)
    test_file = open("test_file.txt", "w")
    file_writer(test_files_list, test_file)


if __name__ == '__main__':
    main()