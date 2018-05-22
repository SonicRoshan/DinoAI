'''

* Game class: Selenium interfacing between the python and browser

* __init__():  Launch the broswer window using the attributes in chrome_options

* get_crashed() : return true if the agent as crashed on an obstacles. Gets javascript variable from game decribing the state

* get_playing(): true if game in progress, false is crashed or paused

* restart() : sends a signal to browser-javascript to restart the game

* press_up(): sends a single to press up get to the browser

* get_score(): gets current game score from javascript variables.

* pause(): pause the game

* resume(): resume a paused game if not crashed

* end(): close the browser and end the game

'''


import os
import direct_keys
import time
from selenium import webdriver
import numpy as np
from config import *

class Game:

    def __init__(self):

    
        if BROWSER_TO_USE == "edge":
            self._driver = webdriver.Edge()
        elif BROWSER_TO_USE == "chrome":
            self._driver = webdriver.Chrome()
        elif BROWSER_TO_USE == "safari":
            self._driver = webdriver.Safari()
        else:
            print("Invalid BROWSER_TO_USE. Using chrome")
            self._driver = webdriver.Chrome()
            
            

        self._driver.set_window_position(x=-10,y=0)

        self._driver.set_window_size(800, 700)

        self._driver.get(os.path.abspath("t-rex-runner-gh-pages/index.html"))

        

    def get_crashed(self):

        return self._driver.execute_script("return Runner.instance_.crashed")

    def get_playing(self):

        return self._driver.execute_script("return Runner.instance_.playing")

    def restart(self):

        self._driver.execute_script("Runner.instance_.restart()")

        

        time.sleep(0.25)# no actions are possible 

                        # for 0.25 sec after game starts, 

                        # skip learning at this time and make the model wait

    def press_up(self):

        self._driver.find_element_by_tag_name("body").send_keys('\ue013')#Up Arrow Key Code
        

    def get_score(self):

        score_array = self._driver.execute_script("return Runner.instance_.distanceMeter.digits")

        score = ''.join(score_array) # the javascript object is of type array with score in the formate[1,0,0] which is 100.
   
        try:
            score = int(score)
        except Exception as e:
            score = 0


        return score

    def pause(self):

        return self._driver.execute_script("return Runner.instance_.stop()")

    def resume(self):

        return self._driver.execute_script("return Runner.instance_.play()")

    def end(self):

        self._driver.close()

class DinoAgent:

    def __init__(self,game): #takes game as input for taking actions

        self._game = game; 

    def get_score(self):
        return self._game.get_score()

    def is_running(self):

        return self._game.get_playing()

    def is_crashed(self):

        return self._game.get_crashed()

    def jump(self):

        self._game.press_up()

    def duck(self):

        self._game.press_down()
    def reset(self):
        self._game.restart()
