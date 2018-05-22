# DinoAI

DinoAI Is An Artificial Intellgent Neural Network
Which Can Play T-Rex Runner or Dino Runner Game

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Download this modules in order to run the project

```
pip intall numpy
pip install cv2
pip install keyboard
pip install tqdm
pip install tensorflow
pip install tflearn
pip install selenium
win32gui, win32ui, win32con, win32api
```

### Installing

A step by step series of examples that tell you have to get a development env running

The project itself dosen't come with pre-trained model or training data.
If you want a pre-trained model and training data, get it from here (link coming soon...).
First you will need to create training data.

#### Steps To Create Training Data

You can change value in config.py to you likings. Don't mess with settings you are not aware of


1. Create folder named Models, training_data and formatted_training_data
2. Open config.py change BROWSER_TO_USE to edge, chrome or safari. Any you wish
2. Open config.py make sure that AGENT is set to "user". If you change it to "model", DinoAI model will itself create training data for itself. You can set it to "model" if you either have a pre-trained model or have downloaded it from here (link coming soon..).
3. Open training_data_gen.py
4. Run the training_data_gen.py
5. Your browser will open. DONT RESIZE YOUR BROWSER.
5. When "you can start" appears on the shell, press up key and start playing, the program will record you. REMEBER DUCK ACTION IS NOT SUPPORTED, YOU CAN ONLY JUMP
6. Press q to stop. Press s to see how many frames are recorded. Press p to pause and up key to resume
7. Open format_data.py and run it, you will se training_data.npy file in formatted_training_data folder
8. Open and run train_model.py and you will see the model learning

If You Experience Any Errors, Contact To sonicroshan122@gmail.com

## Running the model

Once you have trained the model or have downloaded the pre-trained model from here (link coming soon...)
You can start the model

1. Open play_with_model.py
2. Run it. Once "you can start" appears, press up key and model will start

## Using The DinoAI.py

You can import DinoAI.py in your own script and use the AI.
You just jave to do this in your script.

```python
import DinoAI

DinoAI.get_action_by_user(SCREEN_DATA)
```

## DinoAI History

Currently the model has a high score of 772
### Version 0.1 (CURRENT)
Version 0.1 was trained on 10k frames recorded by DinoAI model itself, and 5k frames recorded by human

### Version beta
Version Beta was trained on 15k frames recorded by human

### Version Alpha

Version Alpha was trained on 10k frames recorded by human


## DinoAI Issues

* The model jumps early when starting the game
* The model jump slower as the game progresses
* The model can handle birds


## Built With

*[Tensorflow](https://www.tensorflow.org/) - The AI Framework
*[TFlearn] (https://ww.tflearn.org/) - The Abstraction layer on top of tensorflow


## Contributing
If you have any suggestion either contact sonicroshan122@gmail or send a pull request


## Authors

Roshan Jignesh Mehta - sonicroshan122@gmail


## License

see the [LICENSE.md](https://github.com/SonicRoshan/DinoAI/blob/master/LICENSE) file for details

## Acknowledgments

This project has been influenced by pygta project of Sentdex (https://github.com/Sentdex/pygta5)
