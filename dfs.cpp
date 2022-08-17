#include <bits/stdc++.h>
#include <stack>
#include <vector>

using namespace std;

class graph
{
    int vertices;
    list<int> *adj;
public:
    graph(int vertices);
    void addEdge(int v, int w);
    void DFS(int s);
};

graph ::graph(int vertices)
{   this->vertices = vertices;
    adj = new list<int>[vertices];
}

void graph::addEdge(int v, int w)
{adj[v].push_back(w);}

void graph::DFS(int s)
{
    vector<bool> Visited(vertices, false);
    stack<int> stack;
    stack.push(s);
    while (!stack.empty())
    {
        int s = stack.top();
        stack.pop();

        if (!Visited[s])
        {
            cout << s << " ";
            Visited[s] = true;
        }
        for (auto i = adj[s].begin(); i != adj[s].end(); ++i)
        {   if (!Visited[*i])
            {stack.push(*i);}
        }
    }
}
int main()
{
    cout <<"_____________depth first search_____________\n";

    int size_of_graph , input1 , input2;
    cout<<"enter size of graph \n";
    cin >> size_of_graph;
    graph g(size_of_graph);

    for(int i = 0; i<size_of_graph; i++){
        cout<<"enter inputs :: ";
        cin>>input1 >>input2;
        g.addEdge(input1,input2);
    }
 
    cout<<"\n give a starting point :: ";
    cin>>input1;
 
    g.DFS(input1);
    _sleep(50000);

    return 0;
}