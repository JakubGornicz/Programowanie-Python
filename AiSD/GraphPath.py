from AiSD import Graph


class GraphPath(object):
    graph: Graph
    start: Graph.Vertex
    end: Graph.Vertex

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

