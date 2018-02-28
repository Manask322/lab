#include "ds.h"
#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> adjlist(vector<vector<int>> edges,int n)
{   
    vector<vector<int>> alist(n);
    for(int i=0;i<edges.size();i++)
    {
        alist[edges[i][0]].push_back(edges[i][1]);
        alist[edges[i][1]].push_back(edges[i][0]);
    }
    return alist;
}

int main()
{
    printf("Enter number of vertices and edges in the graph");
    int n_v,n_e;
    scanf("%d %d",&n_v,&n_e);
    vector<vector<int>> edges {};
    ds ds1(n_v);
    
}