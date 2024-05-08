class WeightedGraph:
    def __init__(self) -> None:
        self.connections = dict()
        self.weights = dict()

    def add_edge(self, src, dst, weight):
        does_node_exist = self.connections.get(src, False)

        if not does_node_exist:
            self.connections[src] = set()
            self.weights[src] = set()

        self.connections[src].add(dst)
        self.weights[src].add(weight)

    
