import time
import graph_tool.all as gt
from aux import get_delay, get_instance


# graph
g = gt.Graph(directed=False)

# vertex list, cost map, delay map
v_list, cost, delay = get_instance(g)

# add budget
budget = 30

best = [float('Inf'), None]

def greedy(graph, delay, cost, budget):
    # set number of vertices
    n = len(graph.get_vertices())
    # set upgrades vector
    upgrade = [0]*n

    while (True):
        vu = graph.vertex(0)
        mincost = cost[vu]
        for v in graph.vertices():
            if (cost[v] <= budget):
                if (cost[v] < mincost and upgrade[int(v)] == 0):
                    mincost = cost[v]
                    vu = graph.vertex(v)
        if (mincost > budget):
            break
        else:
            upgrade[int(vu)] = 1
            budget -= cost[vu]

    d = get_delay(graph, delay, upgrade)
    tree = gt.min_spanning_tree(graph, weights=d)
    tdelay = sum([a*b for a,b in zip(list(tree),list(d))])
    
    best[0] = tdelay
    best[1] = upgrade

    return 0


#********************************** GREEDY  **********************************#
print("Running greedy algorithm...")
start = time.time()
greedy(g, delay, cost, budget)
end = time.time()
print("MST delay: ", best[0])
#print("Upgraded nodes: ", best[1])
print("Elapsed time: ", end-start)
#*****************************************************************************#


