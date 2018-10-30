#include "aux.h"

void upgradeNode(Graph *graph,
                 ECostMap &upEdges,
                 NCostMap &cost,
                 float &budget,
                 NodeIt node)
{
  /* Dado um vertice. Se o custo de melhorá-lo for menor que
  budget, melhora o vértice */
  if (cost[node] <= budget)
  {
    budget -= cost[node];
    for (lemon::ListGraph::IncEdgeIt e(*graph, node); e != lemon::INVALID; ++e)
    {
      upEdges[e] += 1;
    }
  }
}