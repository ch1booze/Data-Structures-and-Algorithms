class LocationGraph:
    def __init__(self) -> None:
        self.connections = dict()
        self.weights = dict()

    def add_edge(self, src, dst, weight):
        does_node_exist = self.connections.get(src, False)

        if not does_node_exist:
            self.connections[src] = list()
            self.weights[src] = list()

        if not dst in self.connections[src]:
            self.connections[src].append(dst)
            self.weights[src].append(weight)

    def remove_edge(self, src, dst):
        does_node_exist = self.connections.get(src, False)

        if does_node_exist:
            index = self.connections[src].index(dst)
            self.connections[src].remove(dst)
            self.weights[src].pop(index)

        if not self.connection[src]:
            del self.connections[src]
            del self.weights[src]

    def change_weight(self, src, dst, new_weight):
        does_node_exist = self.connections.get(src, False)

        if does_node_exist:
            if dst in self.connections[src]:
                index = self.connections[src].index(dst)
                self.weights[src][index] = new_weight
