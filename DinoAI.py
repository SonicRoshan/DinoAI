"""
The Main DinoAI File
If you want to use the model, import this file
"""
import numpy as np
import cv2
from models import alexnet2
from config import *

#Loading Model
MODEL = alexnet2(SCREEN_TO_RESIZE[0],
                SCREEN_TO_RESIZE[1],
                LR,
                output=2)
MODEL.load("{}/{}/{}".format(MODEL_DATA_DIR, MODEL_NAME, MODEL_NAME))
print("DinoAI Loaded")

def get_action_by_model(obs):
    """Gets action by the model"""
    obs = process_img(obs)
    prediction = MODEL.predict(np.array(obs).reshape(-1, SCREEN_TO_RESIZE[0], SCREEN_TO_RESIZE[1], 1))
    return np.argmax(prediction)


def process_img(screen):
    """Converts image to grayscale and resize it"""
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, SCREEN_TO_RESIZE) #Downscales the image 5 times
    return screen

