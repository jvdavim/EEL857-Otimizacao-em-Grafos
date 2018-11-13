from aux import gt, getInstance
from bruteforce import brute_force_umst
from backtrack import backtrack_umst
import time


# graph
g = gt.Graph(directed=False)

# vertex list, cost map, delay map
v_list, cost, delay = getInstance(g)

# add budget
budget = 2

print("\n")
#******************************* BRUTE FORCE  ********************************#
print("Running brute force algorithm...")
start = time.time()
result = brute_force_umst(g, delay, cost, budget)
end = time.time()

print("MST delay: ", result[0])
print("Upgraded nodes: ", result[2])
print("Elapsed time: ", end-start)
#*****************************************************************************#
print("\n")
#******************************** BACKTRACK  *********************************#
print("Running backtrack algorithm...")
start = time.time()
result = backtrack_umst(g, delay, cost, budget)
end = time.time()

print("MST delay: ", result[0])
print("Upgraded nodes: ", result[2])
print("Elapsed time: ", end-start)
#*****************************************************************************#
print("\n")