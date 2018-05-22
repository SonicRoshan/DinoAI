"""Views the training data. Only for debugging purposes"""
import cv2
import numpy as np


def get_action():
    return [0,0]
def view_data(training_data):
    for data in training_data:
        frame = data[0]
        frame = cv2.resize(frame, (750,150)) #Upscaling just for debugging and better view of data
        action = data[1]
        cv2.imshow("frame", frame)
        cv2.waitKey(1)



view_data(np.load("training_data/training_data_10042.npy"))

        
