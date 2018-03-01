#include "ds.h"
#include<bits/stdc++.h>
using namespace std;
bool sortcol( vector<int>v1, vector<int>v2 ) {
 return v1[2] < v2[2];
}
vector< vector<int> > mst(int n, vector < vector<int> > edges) {
    ds ds1(n);
    int weight=0;
    vector< vector<int> > tree;
    sort(edges.begin(), edges.end(),sortcol);
    for(int i=0;i<edges.size();i++)
    {
        if(ds1.find(edges[i][0])!=ds1.find(edges[i][1]))
        {  
            tree.push_back(edges[i]); 
            weight+=edges[i][2];ds1.union_set(edges[i][0],edges[i][1]);
        }
    }
    return tree;
}
int main()
{
    printf("Enter number of vertices and edges in the graph\n");
    int n,m;
    scanf("%d %d",&n,&m);
    vector< vector<int> > edges(m,vector<int>(3));
    printf("Enter edges\n");
    for(int edges_i = 0;edges_i < m;edges_i++){
       for(int edges_j = 0;edges_j < 3;edges_j++){
          cin >> edges[edges_i][edges_j];
       }
    }
    vector< vector<int> > tree=mst(n,edges);
    printf("The tree is:\n");
    for(int i=0;i<tree.size();i++)
    {
        printf("%d %d\n",tree[i][0],tree[i][1]);
    }
}
// 1 2 5
// 1 3 3
// 4 1 6
// 2 4 7
// 3 2 4
// 3 4 5