"""Creates Training Data For Model"""
from os import listdir
import keyboard
import numpy as np
import cv2
from grabscreen import grabscreen
import game
#import DinoAI
from config import *

DINO_AGENT = game.DinoAgent(game.Game(speed_up=True))

def get_action_user():
    """Gets action pressed by the user"""
    #[1,0] Do Nothing
    #[0,1] Jump
    if keyboard.is_pressed("up") or keyboard.is_pressed("space"):
        action = [0, 1]
    else:
        action = [1, 0]
    return action





def create_training_data(agent):
    """Starts Creating Training Data"""
    if agent == "model":
        import DinoAI 
    training_data = []
    start_recording = True
    pause = True
    prev_paused = False

    print("You can start")

    while start_recording:
        if keyboard.is_pressed("up"):
            #Start recording or unpauses when up key is pressed
            if not prev_paused:
                #Game was'nt previuosly paused
                print("Started the game")
                pause = False
            else:
                #Game was previousy paused
                print("Resuming")
                pause = False

        while not pause:
            if len(training_data) % 1000 == 0 and len(training_data) > 1:
                #Prints and tells you how many frames were rcorded every one thousand frames
                print("{} frames were over".format(len(training_data)))

            #Takes action and screen
            screen = grabscreen()
            
            if agent == "user":
                #Gets action by user
                action = get_action_user()
            elif agent == "model":
                #Gets action by model. Used to generate training data by the model
                action = DinoAI.get_action_by_model(screen)
                if action == 1:
                    DINO_AGENT.jump()
                    action = [0, 1]
                else:
                    action = [1, 0]




            if not DINO_AGENT.is_crashed():
                #Only records data if dino is not in crashed position
                if DINO_AGENT.get_score() >= SCORE_REQUIREMENT:
                    #Only starts adding game data when score was higher than 75
                    #Append  action and current screen pixel data to training data
                    training_data.append([screen, action])

            else:
                #If dino crashes it will hump automatically
                DINO_AGENT.jump()

            if keyboard.is_pressed("p"):
                #Pause when p is pressed
                pause = True
                DINO_AGENT._game.pause()
                prev_paused = True
                print("paused")

            if keyboard.is_pressed("s"):
                #Shows the training data length
                print("Training Data Len {}".format(len(training_data)))

            if keyboard.is_pressed("q"):
                #Stop recording when q is pressed
                np.save("{}/training_data_{}.npy".format(
                    TRAINING_DATA_DIR,
                    len(listdir("training_data"))+1),
                        training_data)

                start_recording = False
                pause = True

if __name__ == '__main__':
    create_training_data("user")
