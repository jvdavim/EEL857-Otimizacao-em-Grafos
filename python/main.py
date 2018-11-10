import graph_tool.all as gt
from numpy.random import random

# Import or create graph #
# graph
g = gt.Graph(directed=False)

# add nodes
v0 = g.add_vertex()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
v4 = g.add_vertex()

# add edges
e1 = g.add_edge(v0, v1)
e2 = g.add_edge(v2, v4)
e3 = g.add_edge(v2, v3)
e4 = g.add_edge(v2, v1)
e5 = g.add_edge(v0, v3)
e6 = g.add_edge(v3, v4)

# add costs to upgrade nodes
cost = g.new_vertex_property("double")
cost.get_array()[:] = random(g.num_vertices())

# add delays to edges
delay = g.new_edge_property("vector<double>")
for e in g.edges():
    delay[e] = [random(1)] + [random(1)] + [random(1)]

# set a budget
budget = 3


def brute_force_umst(g, d, c, b):
    upgrade = g.new_vertex_property("bool")
    delay = getDelay(g, d, upgrade)

    tree = gt.min_spanning_tree(g, weights=delay)
    treeDelay = 0
    for i in range(len(list(tree))):
        treeDelay += list(tree)[i]*list(delay)[i]
    # for v in g.vertices():
    #     for e in v.out_edges():

    return []

def getDelay(g, d, u):
    """ Given a upgrade property map, returns the matching delay property map """
    delay = g.new_edge_property("double")
    for v in g.vertices():
        for e in g.edges():
            delay[e] = d[e][u[v]]
    return delay


brute_force_umst(g, delay, cost, budget)
