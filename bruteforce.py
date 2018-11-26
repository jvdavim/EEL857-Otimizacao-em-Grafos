import time
import graph_tool.all as gt
from aux import get_delay, get_instance


# graph
g = gt.Graph(directed=False)

# vertex list, cost map, delay map
v_list, cost, delay = get_instance(g)

# add budget
budget = 10

best = [float('Inf'), None, None]

def brute_force(graph, delay, cost, budget, upgrade, i, pcost):
    global best
    if (i == len(list(graph.vertices()))):
        d = get_delay(graph, delay, upgrade)
        tree = gt.min_spanning_tree(graph, weights=d)
        pdelay = sum([a*b for a,b in zip(list(tree),list(d))])

        if (pdelay < best[0] and pcost <= budget):
            best[0] = pdelay
            best[1] = upgrade

    else:
        upgrade2 = upgrade.copy()
        upgrade[i] = 0
        brute_force(graph, delay, cost, budget, upgrade, i+1, pcost)
        upgrade2[i] = 1
        brute_force(graph, delay, cost, budget, upgrade2, i+1, pcost+cost[i])

    return 0


 #******************************** BACKTRACK  *********************************#
print("Running brute force algorithm...")
start = time.time()
brute_force(g, delay, cost, budget, [-1]*len(list(g.vertices())), 0, 0)
end = time.time()
print("MST delay: ", best[0])
print("Upgraded nodes: ", best[1])
print("Elapsed time: ", end-start)
 #*****************************************************************************#