from controller import Controller
import numpy as np


class player_controller_random(Controller):
    def control(self, inputs, controller):
        return np.random.randint(0, 2, 5)


class player_controller_intuition(Controller):
    def control(self, inputs, controller):
        act1 = 0
        act2 = 0
        act3 = 1
        act4 = 1
        act5 = np.random.randint(0, 2)
        return [act1, act2, act3, act4, act5]

