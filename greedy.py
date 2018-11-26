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

def greedy(g, d, c, b):
#    # set number of vertices
#    n = len(g.get_vertices())
#    # set upgrades vector
#    upgrade = [0]*n
#
#    while (b >= 0):
#        nextUpgrade = g.vertex(0)
#        minTotalDelay = float('inf')
#        cost = 0
#        for v in g.vertices():
#            totalDelay = 0
#            for e in v.out_edges():
#                totalDelay += d[e][upgrade[int(v)]]
#            if (totalDelay < minTotalDelay and (b-c[v]) >= 0):
#                cost = c[v]
#                minTotalDelay = totalDelay
#                nextUpgrade = v
# 
#        if (cost > 0):
#            b -= cost
#            upgrade[int(nextUpgrade)] += 1
#        else:
#            break
#
#    delay = get_delay(g, d, upgrade)
#    tree = gt.min_spanning_tree(g, weights=delay)
#    treeDelay = 0
#    for e in g.edges():
#        treeDelay += delay[e]*tree[e]

    return []


 #******************************** BACKTRACK  *********************************#
print("Running greedy algorithm...")
start = time.time()
# CHAMAR A FUNCAO
end = time.time()
print("MST delay: ", best[0])
print("Upgraded nodes: ", best[1])
print("Elapsed time: ", end-start)
 #*****************************************************************************#


