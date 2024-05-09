import random


class VectorGraph:
    def __init__(self) -> None:
        self.connections = dict()
        self.weights = dict()

    def add_edge(self, src, dst, weight):
        does_node_exist = self.connections.get(src, False)

        if not does_node_exist:
            self.connections[src] = list()
            self.weights[src] = list()
            self.connections[src].append(dst)
            self.weights[src].append(weight)
            print(f"Added a path between {src} and {dst} with a distance {weight}.")

        else:
            if not dst in self.connections[src]:
                self.connections[src].append(dst)
                self.weights[src].append(weight)
                print(f"Added a path between {src} and {dst} with a distance {weight}.")

            else:
                print(f"A path already exists between {src} and {dst}.")

    def remove_edge(self, src, dst):
        does_node_exist = self.connections.get(src, False)

        if does_node_exist:
            if dst in self.connections[src]:
                index = self.connections[src].index(dst)
                self.connections[src].remove(dst)
                self.weights[src].pop(index)
                print(f"Removed path between {src} and {dst}.")

                if not self.connection[src]:
                    del self.connections[src]
                    del self.weights[src]
                    print(f"{src} is not longer a source.")

        else:
            print(f"{src} is not a source.")

    def change_weight(self, src, dst, new_weight):
        does_node_exist = self.connections.get(src, False)

        if does_node_exist:
            if dst in self.connections[src]:
                index = self.connections[src].index(dst)
                self.weights[src][index] = new_weight
                print(f"Distance between {src} and {dst} is now {new_weight}.")

            else:
                print(f"There is no path between {src} and {dst}.")

        else:
            print(f"{src} is not a source.")


if __name__ == "__main__":
    vectors = VectorGraph()
    random.seed(42)

    for _ in range(15):
        source = chr(random.randint(65, 74))
        destination = chr(random.randint(65, 74))
        while source == destination:
            destination = chr(random.randint(65, 74))
        distance = random.randint(1, 20)
        vectors.add_edge(source, destination, distance)
