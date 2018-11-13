import graph_tool.all as gt
import itertools


def comb(a, n):
    return list(map(list, itertools.product(a, repeat=n)))


def getDelay(g, d, u):
    """ Given a upgrade property map, returns the matching delay property map """
    delay = g.new_ep("double")
    for e in g.edges():
        delay[e] = d[e][min(u[g.vertex_index[e.target()]] +
                            u[g.vertex_index[e.source()]], 2)]
    return delay
