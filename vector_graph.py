import math


class VectorGraph:
    def __init__(self) -> None:
        self.graph = dict()

    def does_node_exist(self, node):
        return self.graph.get(node, False)

    def add_edge(self, src, dst, weight):
        if not self.does_node_exist(src):
            self.graph[src] = {dst: weight}
        else:
            self.graph[src][dst] = weight

        if not self.does_node_exist(dst):
            self.graph[dst] = dict()

    def dijkstra(self, start):
        def find_lowest_cost_node(costs, processed):
            lowest_cost = math.inf
            lowest_cost_node = None
            for node in costs:
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node
            return lowest_cost_node

        nodes_except_start = [node for node in self.graph.keys() if node != start]
        costs = {node: math.inf for node in nodes_except_start}
        parents = {node: None for node in nodes_except_start}
        processed = list()

        start_neighbors = self.graph[start].keys()
        for node in start_neighbors:
            parents[node] = start
            costs[node] = self.graph[start][node]

        current_node = find_lowest_cost_node(costs, processed)
        while current_node is not None:
            cost = costs[current_node]
            neighbors = self.graph[current_node]

            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = current_node
            processed.append(current_node)
            current_node = find_lowest_cost_node(costs, processed)

        print(parents)
        print(costs)


if __name__ == "__main__":
    v = VectorGraph()
    v.add_edge("start", "a", 6)
    v.add_edge("start", "b", 2)
    v.add_edge("a", "fin", 1)
    v.add_edge("b", "a", 3)
    v.add_edge("b", "fin", 1)

    v.dijkstra("start")
