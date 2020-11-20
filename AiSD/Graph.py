from enum import Enum
from typing import Any, Optional, Dict, List


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex(object):
    data: Any
    index: int

    def __init__(self, data, index=0):
        self.data = data
        self.index = index


class Edge(object):
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight=None):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph(object):
    graph_dict: Dict[Vertex, List[Edge]]
    staticIndex = 0

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def __repr__(self):
        result = []
        for key, values in self.graph_dict.items():
            result.append(f"-{key.index}: {key.data} ----> {[values]}\n")
        return result

    def create_vertex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data, index=Graph.staticIndex)
        Graph.staticIndex += 1
        self.graph_dict[new_vertex] = []
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_dir_edge = Edge(source, destination, weight)
        if source in self.graph_dict:
            self.graph_dict[source].append(new_dir_edge)
        else:
            self.graph_dict[source] = [new_dir_edge]

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        from_edge = Edge(destination, source, weight)
        if destination in self.graph_dict:
            self.graph_dict[source].append(from_edge)
        else:
            self.graph_dict[source] = [from_edge]

        to_edge = Edge(source, destination, weight)
        if source in self.graph_dict:
            self.graph_dict[source].append(to_edge)
        else:
            self.graph_dict[source] = [to_edge]

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        pass


v1 = Vertex("Katowice", 0)
v2 = Vertex("Stavanger", 1)
e1 = Edge(v1, v2)
edge_list = [v1, v2]

graph = Graph(edge_list)
print(graph)

"""

routes = [
    ("Katowice", "Stavanger"),
    ("Katowice", "Warszawa"),
    ("Stavanger", "Oslo"),
    ("Warszawa", "Oslo"),
    ("Warszawa", "Londyn"),
    ("Oslo", "Londyn"),
    ("Oslo", "Sztokholm")
]

routes_graph = Graph(routes)
"""


