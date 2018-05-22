"""Loads data from training_data folder then formats it and saves it to formatted_data folder"""
from os import listdir
from random import shuffle
import numpy as np
from tqdm import tqdm
from config import *

def load_data_files():
    """Loads all training data from all files in training_data folder"""
    training_files_data = []
    for file in tqdm(listdir(TRAINING_DATA_DIR), position=1):
        data = np.load("{}/{}".format(TRAINING_DATA_DIR, file))
        training_files_data.append(data)

    return np.concatenate(training_files_data)

def balance_data(training_data):
    """Balances the data"""
    jumps = []
    nothing = []
    for data in training_data:
        obs = data[0]
        action = data[1]

        if action == 0:
            nothing.append([obs, [1, 0]])
        elif action == 1:
            jumps.append([obs, [0, 1]])
        elif action == [1, 0]:
            nothing.append([obs, action])
        elif action == [0, 1]:
            jumps.append([obs, action])
            
        else:
            raise Exception("Invalid Action {}".format(action))

    #Make sures that jump action and nothing action are equal
    nothing = nothing[:len(jumps)]
    jumps = jumps[:len(nothing)]

    print("{} nothing actions".format(len(nothing)))
    print("{} jump action".format(len(jumps)))
    new_training_data = nothing + jumps
    return new_training_data

def main():
    """MAIN"""
    training_data = load_data_files()
    shuffle(training_data)
    training_data = balance_data(training_data)
    shuffle(training_data)
    print("Final Length of data {}".format(len(training_data)))
    np.save("{}/{}".format(FORMATTED_TRAINING_DATA_DIR,
                           FORMATTED_TRAINING_DATA_NAME),
            training_data)


if __name__ == '__main__':
    main()
