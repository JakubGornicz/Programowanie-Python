from AiSD.Graph import EdgeType, Graph, Vertex
import networkx as nx
import matplotlib.pyplot as plt


class GraphPath(object):
    graph: Graph
    start: Vertex
    end: Vertex

    def __init__(self, graph, start, end):
        self.graph = graph
        self.graph = start
        self.graph = end
        if graph.is_weighted:
            self.dijkstra_algorithm(graph, start, end)
        else:
            self.unweighted_shortest_path(graph, start, end)

    def unweighted_shortest_path(self, graph: Graph, start: Vertex, end: Vertex):
        current: Vertex
        if start == end:
            return
        visited = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            print(path, type(path), ": path")
            current = path[-1]
            print(current, type(current), ": current")
            print(visited, ": visited:")
            if current not in visited:
                neighbours = graph.graph_dict[current]
                print(neighbours, type(neighbours), ": neighbours")
                for neighbour in neighbours:
                    new_path = list(path)
                    print(new_path, ": new_path1")
                    new_path.append(neighbour.destination)
                    print(new_path, ": new_path2")
                    queue.append(new_path)
                    print(queue, ": queue")
                    if neighbour.destination == end:
                        print("###" * 10)
                        print("Shortest path: ", new_path)
                        graph.show(new_path)
                        return
                visited.append(current)
        print("Error: There's no path between chosen nodes")
        return

    def dijkstra_algorithm(self, graph: Graph, start: Vertex, end: Vertex):
        shortest_paths = {start: (None, 0)}
        current = start
        visited = []
        while current is not end:
            visited.append(current)
            print(visited, ": visited")
            neighbours = graph.graph_dict[current]
            print(neighbours, ": neighbours")
            weight_to_current = shortest_paths[current][1]
            print(weight_to_current, type(weight_to_current), ": weight_to_current")

            for neighbour in neighbours:
                weight = neighbour.weight + weight_to_current
                print(weight, ": weight")
                if neighbour.destination not in shortest_paths:
                    shortest_paths[neighbour.destination] = (current, weight)
                else:
                    current_shortest_weight = shortest_paths[neighbour.destination][1]
                    if current_shortest_weight > weight:
                        shortest_paths[neighbour.destination] = (current, weight)

            next_neighbours = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            print(next_neighbours, ": next_neighbours")
            if not next_neighbours:
                return "Error: There's no path between chosen nodes"
            current = min(next_neighbours, key=lambda k: next_neighbours[k][1])
            print(current, ": current")
            print(shortest_paths, ": shortest_paths")

        path = []
        while current is not None:
            path.append(current)
            neighbour = shortest_paths[current][0]
            print(shortest_paths[current], ": shortest_paths")
            current = neighbour
        print(path, ": path")
        path = path[::-1]
        print("###"*10)
        print("Shortest path: ", path)
        graph.show(path)


g = Graph()
v0 = g.create_vertex("v0")
v1 = g.create_vertex("v1")
v2 = g.create_vertex("v2")
v3 = g.create_vertex("v3")
v4 = g.create_vertex("v4")
v5 = g.create_vertex("v5")

g.add_directed_edge(v0, v1, 25)
g.add_undirected_edge(v0, v5, 5)
g.add(EdgeType(1), v5, v2, 5)
g.add(EdgeType(1), v2, v1, 5)
g.add(EdgeType(2), v2, v3, 4)
g.add(EdgeType(1), v3, v4, 3)
g.add(EdgeType(1), v4, v1, 10)
g.add(EdgeType(1), v4, v5, 3)

nW_g = Graph()
a = nW_g.create_vertex("a")
b = nW_g.create_vertex("b")
c = nW_g.create_vertex("c")
d = nW_g.create_vertex("d")
e = nW_g.create_vertex("e")
f = nW_g.create_vertex("f")
nW_g.add_directed_edge(a, b)
nW_g.add_undirected_edge(a, f)
nW_g.add(EdgeType(1), f, c)
nW_g.add(EdgeType(1), c, b)
nW_g.add(EdgeType(2), c, d)
nW_g.add(EdgeType(1), d, e)
nW_g.add(EdgeType(1), d, b)
nW_g.add(EdgeType(1), d, e)

GraphPath(g, v0, v1)
# GraphPath(nW_g, a, e)

# gp.unweighted_shortest_path(v0, v4)
# gp.dijkstra_algorithm(v0, v1)
