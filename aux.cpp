#include "aux.h"

void upgradeNode(Graph *graph, ECostMap &delay, NCostMap &cost, float &budget, NodeIt node)
{
  /* Dado um vertice. Se o custo de melhorá-lo for menor que
  budget, diminui os atrasos delay das arestas incidentes */
  if (cost[node] <= budget)
  {
    budget -= cost[node];
    for (lemon::ListGraph::IncEdgeIt e(graph[0], node); e != lemon::INVALID; ++e)
    {
      //delay[e][0] = delay[e][1];
      // DIMINUI O DELAY DA ARESTA e.
    }
  }
}