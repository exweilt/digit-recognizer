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

    def register_link(self, destination: 'Neuron'):
        pass

    @staticmethod
    def activation(input: float) -> float:
        pass

class NeuralNetwork:
    def __init__(self) -> None:
        pass

    @staticmethod
    def init_layered_network(layers_sizes: list[int]) -> 'NeuralNetwork':
        assert len(layers_sizes) >= 2

        nn = NeuralNetwork()

        for node_idx in range(layers_sizes[0]):
            nn.register_input_neuron()
        for node_idx in range(layers_sizes[-1]):
            nn.register_output_neuron()


        
        

    @staticmethod
    def load_network_from_json() -> 'NeuralNetwork':
        pass

    def save_network_to_json() -> None:
        pass

    def compute(self, input: list) -> list:
        return []
    
    # if index = -1, adds it to the end
    def register_input_neuron(self, neuron: Neuron, index: int = -1) -> None:
        pass

    # if index = -1, adds it to the end
    def register_output_neuron(self, neuron: Neuron, index: int = -1) -> None:
        pass

