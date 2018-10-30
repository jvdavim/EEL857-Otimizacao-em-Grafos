#include <lemon/list_graph.h>
#include <lemon/maps.h>
#include <lemon/core.h>
#include <lemon/kruskal.h>

// Grafo
typedef lemon::ListGraph Graph;
// Vértices e arestas
typedef lemon::ListGraph::Node Node;
typedef lemon::ListGraph::Edge Edge;
// Mapa de vértices float
typedef lemon::ListGraph::NodeMap<float> NCostMap;
// Mapa de arestas vetor de inteiros
typedef lemon::ListGraph::EdgeMap<std::vector<int>> EDelayMap;
// Mapa de arestas inteiro
typedef lemon::ListGraph::EdgeMap<int> ECostMap;
// Mapa de arestas booleano
typedef lemon::ListGraph::EdgeMap<bool> EBoolMap;
// Iteradores
typedef lemon::ListGraph::NodeIt NodeIt;
typedef lemon::ListGraph::EdgeIt EdgeIt;

void upgradeNode(Graph *graph,
                 ECostMap &upEdges,
                 NCostMap &cost,
                 float &budget,
                 NodeIt node);