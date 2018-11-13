from aux import gt
from bruteforce import brute_force_umst
from backtrack import backtrack_umst
import time


# graph
g = gt.Graph(directed=False)

# add nodes
v0 = g.add_vertex()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
v4 = g.add_vertex()
v5 = g.add_vertex()

# add edges
e1 = g.add_edge(v0, v1)
e2 = g.add_edge(v0, v3)
e3 = g.add_edge(v2, v4)
e4 = g.add_edge(v2, v3)
e5 = g.add_edge(v2, v1)
e6 = g.add_edge(v3, v4)
e7 = g.add_edge(v5, v3)
e8 = g.add_edge(v5, v1)

# add costs to upgrade nodes
cost = g.new_vp("double")
cost.get_array()[:] = [1, 1, 1, 1, 1, 1]

# add delays to edges
delay = g.new_ep("vector<double>")
delay[e1] = [10, 5, 0]
delay[e2] = [2, 1, -2]
delay[e3] = [5, 0, -20]
delay[e4] = [12, 3, -7]
delay[e5] = [18, 1, -23]
delay[e6] = [20, 18, 9]
delay[e7] = [10, 8, -2]
delay[e8] = [30, 29, 21]

# set a budget
budget = 4

#******************************* BRUTE FORCE TEST *****************************#
start = time.time()
umst = backtrack_umst(g, delay, cost, budget)
end = time.time()
gt.graph_draw(umst[1], vertex_text=g.vertex_index, vertex_font_size=18,
              output_size=(200, 200), output="mst.png")

print("Custo da mst: ", umst[0])
print("Nós que foram melhorados: ", umst[2])
print("Tempo de execução: ", end-start)
#******************************************************************************#

#******************************** BACKTRACK TEST ******************************#
#******************************************************************************#
