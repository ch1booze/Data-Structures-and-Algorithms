class WeightedGraph:
    def __init__(self) -> None:
        self.connections = dict()
        self.weights = dict()

    def create_edge(self, src, dst, weight):
        self.connections[src] = set()
        self.connections[src] = set()