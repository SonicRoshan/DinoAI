"""Plays with the MODEL"""
import numpy as np
import cv2
import keyboard
import game
from grabscreen import grabscreen
import DinoAI

DINO_AGENT = game.DinoAgent(game.Game())


print("you can start")
TRAINING_DATA = []
START_RECORDING = False
STOP_GEN_DATA = False

while not STOP_GEN_DATA:
    PREV_ACTION = None
    if keyboard.is_pressed("up"):
        #Start recording when up key is pressed
        print("stated recording")
        START_RECORDING = True
    while START_RECORDING:
        if keyboard.is_pressed("q"):
            #Start recording when up key is pressed
            print("stated recording")
            START_RECORDING = False

        if DINO_AGENT.is_crashed():
            #If dino crashes then jump
            DINO_AGENT.jump()
        #Takes ACTION and SCREEN
        SCREEN = grabscreen()
        ACTION = DinoAI.get_action_by_model(SCREEN)
        if ACTION == 1:
            DINO_AGENT.jump()
