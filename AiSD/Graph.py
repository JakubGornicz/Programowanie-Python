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
        return f"{self.destination.index} : {self.destination.data}"


class Graph(object):
    graph_dict: Dict[Vertex, List[Edge]]
    weight: bool

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


if __name__ == "__main__":

    g = Graph()
    v1 = g.create_vertex("Stavanger")
    v2 = g.create_vertex("New York")
    g.add_directed_edge(g.create_vertex("Katowice"), v1)
    g.add_undirected_edge(v1, g.create_vertex("Warszawa"))
    g.add(EdgeType(1), v2, g.create_vertex("Washington"))
    g.add(EdgeType(2), v2, g.create_vertex("Los Angeles"))

    print(g.graph_dict)
    print(g)
