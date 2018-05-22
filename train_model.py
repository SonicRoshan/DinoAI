"""Trains The Model"""
from os import listdir
import numpy as np
from models import alexnet2
from config import *



def train_model():
    """Trains The Model"""
    training_data = np.load("{}/{}".format(FORMATTED_TRAINING_DATA_DIR,
                                           FORMATTED_TRAINING_DATA_NAME))
    len_of_training_data = len(training_data) #Used to detect if numpy reshaping was invalid
    X = np.array([i[0] for i in training_data]).reshape([-1,
                                                         training_data[0][0].shape[1],
                                                         training_data[0][0].shape[0],
                                                         1])
    y = [i[1] for i in training_data]

    if len(X) != len_of_training_data or len(y) != len_of_training_data:
        #Detects if reshaping was invalid
        raise Exception("Invalid Reshaping. X len was {}, y len was {}, training data len was {}"
                        .format(len(X), len(y), len_of_training_data))

    model = alexnet2(training_data[0][0].shape[1],
                     training_data[0][0].shape[0],
                     LR,
                     output=2)

    if len(listdir("Models")) >= 1:
        #If there is a pre-trained model then load that
        model.load("Models/{}/{}".format(MODEL_NAME, MODEL_NAME))
        print("Model Loaded")
    else:
        print("Could'nt find a model")

    model.fit({'input': X},
              {'targets': y},
              n_epoch=N_EPOCHS,
              snapshot_step=500,
              show_metric=True,
              run_id='{}-{}'.format(MODEL_NAME, len(listdir("log"))+1))

    model.save("Models/{}/{}".format(MODEL_NAME, MODEL_NAME))
    return model
