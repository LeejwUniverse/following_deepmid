# This is sample code for Deep Reinforcement Learning testing environment 

# Import modules
import sys 
import numpy as np
import random

# Import games
sys.path.append("DQN_GAMES/")

# add as game the one that you want to play!! 
import pong
import dot  
import dot_test  
import tetris  
import wormy as game
import breakout 

# Get Number of action and name of game from the game code
Num_action = game.Return_Num_Action()
game_name = game.ReturnName()

# Get game state class from game code
game_state = game.GameState()

while True:
    # Choose random action
    action = np.zeros([Num_action])
    action[random.randint(0, Num_action - 1)] = 1.0

    # You can get next observation, reward and terminal after action
    observation_next, reward, terminal = game_state.frame_step(action)
