import time
import random
import graph_tool.all as gt
from aux import get_delay, get_instance, takeSecond


# graph
g = gt.Graph(directed=False)

# vertex list, cost map, delay map
v_list, cost, delay = get_instance(g)

# add budget
budget = 30

best = [float('Inf'), None]

def random_greedy(graph, delay, cost, budget):
    # set number of vertices
    n = len(graph.get_vertices())
    # set upgrades vector
    upgrade = [0]*n

    while (True):
        vu = []
        for v in graph.vertices():
            if (cost[v] <= budget and upgrade[int(v)] == 0):
                vu += [(v,cost[v])]
        vu.sort(key=takeSecond)
        if (len(list(graph.vertices())) >= 3):
            vu = vu[:3]
        if (vu):
            sample = random.sample(vu, 1)[0]
        else:
            break
        vu = sample[0]
        mincost = sample[1]
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

#****************************** RANDOM GREEDY  *******************************#
print("Running random greedy algorithm...")
start = time.time()
random_greedy(g, delay, cost, budget)
end = time.time()
print("MST delay: ", best[0])
#print("Upgraded nodes: ", best[1])
print("Elapsed time: ", end-start)
#*****************************************************************************#