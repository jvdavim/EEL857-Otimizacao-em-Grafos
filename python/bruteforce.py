from aux import gt, getDelay, comb


def brute_force_umst(g, d, c, b):
    # set n as number of nodes
    n = len(g.get_vertices())
    # set all possible upgrade combinations
    domain = comb([0, 1, 2], n)
    # current budget = budget
    cb = b

    # first value ------------------------------------------
    delay = getDelay(g, d, domain[0])

    minTree = gt.min_spanning_tree(g, weights=delay)
    minDelay = 0
    for i in range(len(list(minTree))):
        minDelay += list(minTree)[i]*list(delay)[i]
    minSol = domain[0]
    # -------------------------------------------------------

    for sol in domain[1:]:
        cb = b
        for i in range(n):
            cb -= c[g.vertex(i)]*sol[i]

        delay = getDelay(g, d, sol)

        tree = gt.min_spanning_tree(g, weights=delay)
        treeDelay = 0
        for e in g.edges():
            treeDelay += delay[e]*tree[e]

        if (treeDelay <= minDelay and cb >= 0):
            minDelay = treeDelay
            minTree = tree
            minSol = sol

    g.set_edge_filter(minTree)
    return [minDelay, g, minSol]
