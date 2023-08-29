from controller import Controller
import numpy as np


def normalize(data):
    return (data - min(data)) / (max(data) - min(data))


def sigmoid(activations):
    return 1/(1 + np.exp(-activations))


class player_controller(Controller):

    def control(self, inputs, controller):
        inputs_nn = normalize(inputs)
        for weights in controller:
            activations = np.matmul(inputs_nn.T, weights)
            inputs_nn = sigmoid(activations)

        outputs = [0 if (x <= 0.5) else 1 for x in inputs_nn]
        return outputs

