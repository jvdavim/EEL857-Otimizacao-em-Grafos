from aux import gt, get_instance
from bruteforce import brute_force_umst
from backtrack import backtrack_umst
from greedy import greedy_umst
import time


# graph
g = gt.Graph(directed=False)

# vertex list, cost map, delay map
v_list, cost, delay = get_instance(g)

# add budget
budget = 2

# print("\n")
# #******************************* BRUTE FORCE  ********************************#
# print("Running brute force algorithm...")
# start = time.time()
# result = brute_force_umst(g, delay, cost, budget)
# end = time.time()

# print("MST delay: ", result[0])
# print("Upgraded nodes: ", result[2])
# print("Elapsed time: ", end-start)
# #*****************************************************************************#
# print('\n')
# #******************************** BACKTRACK  *********************************#
# print("Running backtrack algorithm...")
# start = time.time()
# result = backtrack_umst(g, delay, cost, budget)
# end = time.time()

# print("MST delay: ", result[0])
# print("Upgraded nodes: ", result[2])
# print("Elapsed time: ", end-start)
# #*****************************************************************************#
print('\n')
#********************************* GREEDY  ***********************************#
print("Running greedy algorithm...")
start = time.time()
result = greedy_umst(g, delay, cost, budget)
end = time.time()

print("MST delay: ", result[0])
print("Upgraded nodes: ", result[2])
print("Elapsed time: ", end-start)
#*****************************************************************************#
print('\n')