import os
import sys
import pickle
import numpy as np
sys.path.insert(0, 'evoman')
from environment import Environment
from controllers import player_controller_NN, player_controller_NEAT

enemy = 1
name_experiment = "results/EvoManGame_run"
controller_path = "results/train_neat/agent_enemy-1_fitness-94.pkl"

if not os.path.exists(name_experiment):
    os.makedirs(name_experiment)

env = Environment(experiment_name=name_experiment,
                  enemies=[enemy],
                  playermode="ai",
                  player_controller=player_controller_NEAT(),
                  enemymode="static",
                  randomini="yes",
                  level=2,
                  speed="normal",
                  # savelogs="no",
                  logs="off")

with open(controller_path, "rb") as file:
    net = pickle.load(file)
    env.play(net)

