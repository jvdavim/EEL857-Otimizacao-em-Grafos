#include "aux.h"

using namespace std;
using namespace lemon;

ListGraph *umstBacktrack(ListGraph *graph,
                     ECostMap &delay,
                     NCostMap &cost,
                     float budget)
{
    return nullptr;
}

int main()
{
    //************************************************************//
    //********************* INICIALIZA GRAFO *********************//
    //************************************************************//
    // Grafo
    ListGraph g;

    // Vertices
    Node s = g.addNode();
    Node v1 = g.addNode();
    Node v2 = g.addNode();
    Node v3 = g.addNode();
    Node v4 = g.addNode();
    Node t = g.addNode();

    // Arestas
    Edge e1 = g.addEdge(s, v1);
    Edge e2 = g.addEdge(s, v2);
    Edge e3 = g.addEdge(v1, v2);
    Edge e4 = g.addEdge(v2, v1);
    Edge e5 = g.addEdge(v1, v3);
    Edge e6 = g.addEdge(v3, v2);
    Edge e7 = g.addEdge(v2, v4);
    Edge e8 = g.addEdge(v4, v3);
    Edge e9 = g.addEdge(v3, t);
    Edge e10 = g.addEdge(v4, t);

    // Matriz de atrasos
    ECostMap delay(g);
    delay.set(e1, {10, 5, 1});
    delay.set(e2, {9, 6, 3});
    delay.set(e3, {8, 4, 2});
    delay.set(e4, {7, 4, 2});
    delay.set(e5, {-6, -12, -20});
    delay.set(e6, {-23, -24, -25});
    delay.set(e7, {4, 1, -1});
    delay.set(e8, {31, 10, 9});
    delay.set(e9, {12, 4, 1});
    delay.set(e10, {-1, -5, -10});

    // Vetor de custos
    NCostMap cost(g);
    cost.set(s, 0.87865483);
    cost.set(v1, 0.76763708);
    cost.set(v2, 0.62930603);
    cost.set(v3, 0.06596205);
    cost.set(v4, 0.48245113);
    cost.set(t, 0.84153892);

    // Estimativa de custo
    float budget = 10;

    // ************************ Testes ***************************//
    typedef ListGraph::EdgeIt EdgeIt;
    typedef ListGraph::NodeIt NodeIt;
    NodeIt node(g, s);
    upgradeNode(&g, delay, cost, budget, node);
    for (EdgeIt e(g); e!=INVALID; ++e)
    {
        cout << "Edge " << g.id(e)+1 << ": " << delay[e][0] << endl;
    }
    cout << "Budget: " << budget << endl;


    //************************************************************//
    //********************* APLICA ALGORITMOS ********************//
    //************************************************************//
    // AGM RESULTANTE
    // typedef ListGraph::EdgeMap<bool> EBoolMap;
    // EBoolMap tree_map(g);

    // typedef ListGraph::NodeIt NodeIt;
    // typedef ListGraph::EdgeIt EdgeIt;
}