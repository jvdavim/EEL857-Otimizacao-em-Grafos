import graph_tool.all as gt
import itertools


def get_instance(g):
    # open instance file
    file = open("instance.in", "r")
    line = file.readline().split(" ")

    n_vertices = int(line[0])
    n_edges = int(line[1])

    # add nodes
    v_list = list(g.add_vertex(n_vertices))

    # add edges
    for i in range(n_edges):
        line = file.readline().split(" ")
        g.add_edge(v_list[int(line[0])], v_list[int(line[1])])

    # add costs
    cost = g.new_vp("int")
    for i in range(n_vertices):
        line = file.readline()
        cost[g.vertex(i)] = int(line)

    file.close()
    file = open("instance.in", "r")
    line = file.readline()

    # add delay
    delay = g.new_ep("vector<int>")
    for i in range(n_edges):
        line = file.readline().split(" ")
        delay[g.edge(int(line[0]), int(line[1]))] = [
            int(line[2]), int(line[3]), int(line[4][:-1])]

    return [v_list, cost, delay]


def comb(a, n):
    return list(map(list, itertools.product(a, repeat=n)))


def get_delay(g, d, u):
    """ Given a upgrade property map, returns the matching delay property map """
    delay = g.new_ep("double")
    for e in g.edges():
        delay[e] = d[e][min(u[g.vertex_index[e.target()]] +
                            u[g.vertex_index[e.source()]], 2)]
    return delay
