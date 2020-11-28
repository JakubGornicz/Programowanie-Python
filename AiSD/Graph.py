from enum import Enum
from typing import Any, Optional, Dict, List
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex(object):
    data: Any
    index: int

    def __init__(self, data, index=0):
        self.data = data
        self.index = index

    def __repr__(self):
        return str(self.data)


class Edge(object):
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight=None):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.destination.index}: {self.destination.data}"


class Graph(object):
    graph_dict: Dict[Vertex, List[Edge]]
    weight: bool
    edge_weights: Dict[tuple, int]

    def __init__(self, weight=False):
        self.graph_dict = dict()
        self.weight = weight
        self.index = 0

    def __repr__(self):
        result = []
        for key, values in self.graph_dict.items():
            result.append(f"- {key.index}: {key.data} ----> {values}")
        return "\n".join(result)

    def create_vertex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data=data, index=self.index)
        self.graph_dict.update(dict.fromkeys([new_vertex], []))
        self.index += 1
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_directed_edge = Edge(source, destination, weight)
        self.graph_dict[source].append(new_directed_edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        undirected_edge1 = Edge(source, destination, weight)
        self.graph_dict[source].append(undirected_edge1)

        undirected_edge2 = Edge(destination, source, weight)
        self.graph_dict[destination].append(undirected_edge2)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge.value == 1:
            new_directed_edge = Edge(source, destination, weight)
            self.graph_dict[source].append(new_directed_edge)
        elif edge.value == 2:
            undirected_edge1 = Edge(source, destination, weight)
            self.graph_dict[source].append(undirected_edge1)

            undirected_edge2 = Edge(destination, source, weight)
            self.graph_dict[destination].append(undirected_edge2)
        else:
            return

    def traverse_breadth_first(self, visited=None) -> None:
        if visited is None:
            visited = []
        queue = []
        start = list(self.graph_dict.keys())[0]
        visited.append(start)
        queue.append(start)
        while queue:
            current = queue.pop(0)

            for neighbour in self.graph_dict[current]:
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    queue.append(neighbour.destination)
        print(visited)

    def dfs(self, v: Vertex, visited: List[Vertex]):
        visited.append(v)
        for neighbour in self.graph_dict[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited)

    def traverse_depth_first(self, visited=None) -> None:
        if visited is None:
            visited = []
        start = list(self.graph_dict.keys())[0]
        self.dfs(start, visited)
        print(visited)

    def show(self):
        graph = nx.DiGraph()
        start = list(self.graph_dict.keys())[0]
        queue = [start]
        visited = [start]
        edge_weights = {}
        while queue:
            current = queue.pop(0)
            for neighbour in self.graph_dict[current]:
                graph.add_edge(current.data, neighbour.destination.data)
                curr_weight = {(current.data, neighbour.destination.data): neighbour.weight}
                edge_weights.update(curr_weight)
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    queue.append(neighbour.destination)
                    graph.add_edge(current.data, neighbour.destination.data)

        pos = nx.spectral_layout(graph)
        nx.draw(graph, pos, edge_color='black', width=1, linewidths=1, node_size=3000, node_color='pink', alpha=0.7,
                labels={node: node for node in graph.nodes()})
        if self.weight is True:
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weights, font_color='red')
        plt.axis('off')
        plt.show()


if __name__ == "__main__":

    g = Graph(weight=True)
    v0 = g.create_vertex("v0")
    v1 = g.create_vertex("v1")
    v2 = g.create_vertex("v2")
    v3 = g.create_vertex("v3")
    v4 = g.create_vertex("v4")
    v5 = g.create_vertex("v5")

    g.add_directed_edge(v0, v1, 10)
    g.add_undirected_edge(v0, v5, 5)
    g.add(EdgeType(1), v5, v2, 20)
    g.add(EdgeType(1), v2, v1, 9)
    g.add(EdgeType(2), v2, v3, 4)
    g.add(EdgeType(1), v3, v4, 3)
    g.add(EdgeType(1), v4, v1, 10)
    g.add(EdgeType(1), v4, v5, 3)

    print(g.graph_dict)
    print(g)

    g.traverse_breadth_first()
    g.traverse_depth_first()
    g.show()
