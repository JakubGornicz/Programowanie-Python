import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
nodes = [("v0", {"color": "green"}),
         ("v1", {"color": "black"}),
         ("v2", {"color": "black"}),
         ("v3", {"color": "black"}),
         ("v4", {"color": "black"}),
         ("v5", {"color": "red"})]
cities = {"v0": "Toronto", "v1": "London", "v2": "Berlin", "v3": "New York"}
edges = [("v0", "v1", 0.1),
         ("v0", "v5", 0.5),
         ("v5", "v2", 1),
         ("v2", "v1", 0.75),
         ("v2", "v3", 10),
         ("v3", "v4", 9),
         ("v4", "v1", 7),
         ("v4", "v5", 40),
         ("v5", "v4", 40),
         ]

G.add_nodes_from(nodes)

G.add_weighted_edges_from(edges)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

print(list(G.neighbors("v0")))



plt.tight_layout()
nx.draw_networkx(G, arrows=True)
plt.savefig("g1.png", format="PNG")

plt.show()
plt.clf()