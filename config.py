"""This file contains all the settings"""



#Global settings
TRAINING_DATA_DIR = "training_data" #Where training data is saves
FORMATTED_TRAINING_DATA_DIR = "formatted_training_data" #Where formatted training data is stored
FORMATTED_TRAINING_DATA_NAME = "training_data.npy" #File where data is contained



#Train Model Config
LR = 1e-3 #Learning rate
MODEL_NAME = "DinoAI-{}-{}-{}".format(LR, "v0.1", "alexnet2") #Model Name
MODEL_DATA_DIR = "Models" #Where models are saved
OUTPUTS = 2 #Outputs by the model
N_EPOCHS = 5 #The epochs

#Training Data Gen Config
SCREEN_SIZE_RECORD_SIZE = (130,250,780,400) #Region to record
SCREEN_TO_RESIZE = (int((int(SCREEN_SIZE_RECORD_SIZE[2]) - int(SCREEN_SIZE_RECORD_SIZE[0]))/5),
                    int((int(SCREEN_SIZE_RECORD_SIZE[3]) - int(SCREEN_SIZE_RECORD_SIZE[1]))/5)) #Resizing size
SCORE_REQUIREMENT = 100 #Score required for recording to start. Increasing this creates better AI, but less training data is generated
