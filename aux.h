#include <lemon/list_graph.h>
#include <lemon/maps.h>
#include <lemon/core.h>

typedef lemon::ListGraph Graph;
typedef lemon::ListGraph::Node Node;
typedef lemon::ListGraph::Edge Edge;
typedef lemon::ListGraph::NodeMap<float> NCostMap;
typedef lemon::ListGraph::EdgeMap<std::vector<int>> ECostMap;
typedef lemon::ListGraph::NodeIt NodeIt;

void upgradeNode(Graph *graph, ECostMap &delay, NCostMap &cost, float &budget, NodeIt node);