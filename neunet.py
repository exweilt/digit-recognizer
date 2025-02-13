import numpy as np
from typing import *

class Link:
    def __init__(self) -> None:
        self.origin: Neuron
        self.destination: Neuron
        self.weight: float = 1

class Neuron:
    def __init__(self) -> None:
        self.bias: float = 0
        self.links: list[Link] = []
        self.visual_pos: tuple[float, float] = (0, 0)
        self.visual_layer: int = -1

    def register_link(self, destination: 'Neuron'):
        pass

    @staticmethod
    def activation(input: float) -> float:
        pass

class NeuralNetwork:
    def __init__(self) -> None:
        # input_neurons: List[Neuron] = []
        self.neuron_layers: List[Neuron] = []
        self.layers: List['DenseLayer'] = []

    # @staticmethod
    # def init_layered_network(layers_sizes: list[int]) -> 'NeuralNetwork':
    #     """
    #     The first layer does not contain neurons
    #     """
    #     assert len(layers_sizes) >= 2

    #     nn = NeuralNetwork()

    #     nn.neuron_layers = [[]] * len(layers_sizes)

    #     for layer_idx in range(len(layers_sizes)):
    #         for neuron_idx in range(layers_sizes[layer_idx]):
    #             new_neuron = Neuron()

    #             nn.neuron_layers[layer_idx].append(new_neuron)

    #             new_neuron.visual_pos = (10 * neuron_idx, 50 * layer_idx)
    #             new_neuron.visual_layer = layer_idx



            

    #     # for node_idx in range(layers_sizes[0]):
    #     #     nn.register_input_neuron()
    #     # for node_idx in range(layers_sizes[-1]):
    #     #     nn.register_output_neuron()

    # @staticmethod
    # def load_network_from_json() -> 'NeuralNetwork':
    #     pass

    # def save_network_to_json() -> None:
    #     pass

    def infere(self, input: list) -> list:

        return []
    
    # # if index = -1, adds it to the end
    # def register_input_neuron(self, neuron: Neuron, index: int = -1) -> None:
    #     self.input_neurons.append(neuron)

    # # if index = -1, adds it to the end
    # def register_output_neuron(self, neuron: Neuron, index: int = -1) -> None:
    #     pass

    @staticmethod
    def init_using_layers(layers: list['DenseLayer']) -> 'NeuralNetwork':
        nn = NeuralNetwork()
        nn.layers = layers

class DenseLayer:
    def __init__(self, neuron_num: int):
        self.w = np.random.randn(neuron_num)
        self.b = 0

    # def predict(input_x: np.Array) -> np.Array:
    #     a_out = np.zeros(self.w)
    #     for n in        

    # Sigmoid
    def activate(x, k=1.0):
        return 1 / (1 + np.exp(-k*x))