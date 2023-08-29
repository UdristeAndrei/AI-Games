import os
import sys
import numpy as np
sys.path.insert(0, 'evoman')
from environment import Environment
from NN_arhitecture import player_controller


name_experiment = "EvoManGame"

if not os.path.exists(name_experiment):
    os.makedirs(name_experiment)

env = Environment(experiment_name=name_experiment,
                  playermode="ai",
                  player_controller=player_controller(),
                  speed="normal",
                  enemymode="static")

env.play()

