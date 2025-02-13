import numpy as np
from typing import *

class NeuralNetwork:
    def __init__(self, layers: list['DenseLayer']) -> None:
        self.layers: List['DenseLayer'] = layers

    def predict(self, x: np.ndarray) -> np.ndarray:
        assert x.shape[0] == self.layers[0].W.shape[1]

        previous_a: np.ndarray = x
        for layer in self.layers:
            previous_a = layer.compute_a(previous_a)

        return previous_a

    # @staticmethod
    # def init_using_layers(layers: list['DenseLayer']) -> 'NeuralNetwork':
    #     nn = NeuralNetwork()
    #     nn.layers = layers

class DenseLayer:
    def __init__(self, neuron_num: int, input_number: int):
        self.W = np.random.randn(neuron_num, input_number)
        self.b = np.zeros(neuron_num)

    # def predict(input_x: np.Array) -> np.Array:
    #     a_out = np.zeros(self.w)
    #     for n in        

    # Sigmoid
    def activate(self, x, k=1.0):
        return 1 / (1 + np.exp(-k*x))
    
    def compute_a(self, x: np.ndarray) -> np.ndarray:
        a_out = np.zeros(self.W.shape[0])
        
        z = np.dot(self.W, x) + self.b
        a_out = self.activate(z)

        return a_out