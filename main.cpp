#include "aux.h"

using namespace std;
using namespace lemon;

int umstBacktrack(ListGraph *graph,
                  EDelayMap &delay,
                  NCostMap &cost,
                  EBoolMap &tree,
                  float budget)
{
    // Inicializa custo minimo e custo atual
    float minCost = 3.402823 * pow(10, 38);
    float curCost;

    // Inicializa mapa de arestas melhoradas
    ECostMap upEdges(*graph);
    for (EdgeIt e(*graph); e != INVALID; ++e)
    {
        upEdges[e] = 0;
    }

    // Inicializa árvore geradora atual
    EBoolMap curTree(*graph);

    // Iterador
    int it = 0;

    while (it < 2)
    {
        for (NodeIt n(*graph); n != INVALID; ++n)
        {
            upgradeNode(graph, upEdges, cost, budget, n);
            ECostMap curDelay(*graph);
            for (EdgeIt e(*graph); e != INVALID; ++e)
            {
                curDelay[e] = delay[e][upEdges[e]];
            }

            curCost = kruskal(*graph, curDelay, curTree);
            if (curCost < minCost)
            {
                minCost = curCost;
                mapCopy(*graph, curTree, tree);
            }
        }
        it++;
    }
    return minCost;
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
    Edge e4 = g.addEdge(v1, v3);
    Edge e5 = g.addEdge(v3, v2);
    Edge e6 = g.addEdge(v2, v4);
    Edge e7 = g.addEdge(v4, v3);
    Edge e8 = g.addEdge(v3, t);
    Edge e9 = g.addEdge(v4, t);

    // Matriz de atrasos
    EDelayMap delay(g);
    delay.set(e1, {10, 5, 1});
    delay.set(e2, {-50, -60, -81});
    delay.set(e3, {8, 4, 2});
    delay.set(e4, {-6, -12, -20});
    delay.set(e5, {-23, -24, -25});
    delay.set(e6, {4, 1, -1});
    delay.set(e7, {31, 10, 9});
    delay.set(e8, {12, 4, -200});
    delay.set(e9, {-4, -8, -13});

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

    // Árvore geradora mínima onde ficará armazenado o resultado
    EBoolMap mst(g);

    // ************************ Testes ***************************//
    // typedef ListGraph::EdgeIt EdgeIt;
    // typedef ListGraph::NodeIt NodeIt;
    // NodeIt node(g, s);
    // upgradeNode(&g, delay, cost, budget, node);
    // upgradeNode(&g, delay, cost, budget, node);
    // upgradeNode(&g, delay, cost, budget, node);
    // for (EdgeIt e(g); e!=INVALID; ++e)
    // {
    //     cout << "Edge " << g.id(e)+1 << ": " << delay[e][0] << endl;
    // }
    // cout << "Budget: " << budget << endl;

    float minCost = umstBacktrack(&g, delay, cost, mst, budget);
    cout << "COST: " << minCost << endl;
    for (EdgeIt e(g); e != INVALID; ++e)
    {
        cout << "Edge " << g.id(e) + 1 << ": " << mst[e] << endl;
    }
    // cout << minCost << endl;

    //************************************************************//
    //********************* APLICA ALGORITMOS ********************//
    //************************************************************//
    // AGM RESULTANTE
    // typedef ListGraph::EdgeMap<bool> EBoolMap;
    // EBoolMap tree_map(g);

    // typedef ListGraph::NodeIt NodeIt;
    // typedef ListGraph::EdgeIt EdgeIt;
}