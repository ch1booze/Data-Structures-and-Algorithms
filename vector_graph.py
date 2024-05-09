from collections import deque
import math


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

    def get_nodes(self):
        nodes = list()
        for node_list in self.connections.values():
            nodes += node_list
        nodes = list(set(nodes))
        return nodes

    def get_sources(self):
        return set(self.connections.keys())


if __name__ == "__main__":
    vectors = VectorGraph()

    vectors.add_edge("Book", "LP", 5)
    vectors.add_edge("Book", "Poster", 0)
    vectors.add_edge("LP", "Guitar", 15)
    vectors.add_edge("LP", "Drum", 20)
    vectors.add_edge("Poster", "Guitar", 30)
    vectors.add_edge("Poster", "Drum", 35)
    vectors.add_edge("Guitar", "Piano", 20)
    vectors.add_edge("Drum", "Piano", 10)

    nodes = vectors.get_nodes()
    sources = vectors.get_sources()
    start_node = "Book"
    end_node = "Piano"
    dijkstra_distances = {node: math.inf for node in nodes if node != start_node}
    dijkstra_parents = {node: None for node in nodes if node != start_node}
    current_node = start_node
    processed_nodes = set()
    q = deque()

    while sources.intersection(processed_nodes) != sources:
        distances = vectors.weights[current_node]
        connections = vectors.connections[current_node]

        shortest_distance = min(distances)
        index_for_shortest_dist = distances.index(shortest_distance)
        node_for_shortest_dist = connections[index_for_shortest_dist]

        if shortest_distance < dijkstra_distances[node_for_shortest_dist]:
            dijkstra_distances[node_for_shortest_dist] = shortest_distance
            dijkstra_parents[node_for_shortest_dist] = current_node

        for node in connections:
            if node in sources:
                q.append(node)

        processed_nodes.add(current_node)
        current_node = q.pop()

    print(dijkstra_distances)
    print()
    print(dijkstra_parents)
