#include<bits/stdc++.h>
using namespace std;
class ds
{
    public:
    int n;
    vector<int>  rank;
    vector<int>  parent;
    vector< set<int> > sets;
    ds(int n){
        rank.resize(n);
        parent.resize(n);
        sets.resize(n);
        this->n=n;
    makeset();
    }
    void makeset()
    {
      for(int i=0;i<ds::n;i++){parent[i]=i;
       ds::sets[i].insert(i);} 
    }   
    void union_set(int x,int y)
    {
        
        int xRoot = find(x), yRoot = find(y);
        if (xRoot == yRoot)
            return;
        if (rank[xRoot] < rank[yRoot])
        {   
            ds::sets[yRoot].insert(xRoot);
            parent[xRoot] = yRoot;
        }
        else if (rank[yRoot] < rank[xRoot])
        {
                parent[yRoot] = xRoot;
                ds::sets[xRoot].insert(yRoot);
        }
        else 
        {
            
            parent[yRoot] = xRoot;
            ds::sets[yRoot].insert(xRoot);
            rank[xRoot] = rank[xRoot] + 1;
        }
    }
    int find(int x)
    {
        if (parent[x]!=x)
        {
            int temp = find(parent[x]);
            parent[x]=temp;
            ds::sets[temp].insert(x);
        }
 
        return parent[x];
    }
    void printsets()
    {   
        for(int i=0;i<ds::sets.size();i++)
        {   printf("Set : %d\n",i);
            for(set<int>::iterator j=ds::sets[i].begin();j!=ds::sets[i].end();j++)
            {
                printf("%d ",*j);
            }
            printf("\n");
       }
        
    }
};
// int main()
// {   int n=5;
//     ds ds1(n);
//     ds1.union_set(0, 2);
 
        
//         ds1.union_set(4, 2);
 
        
//         ds1.union_set(3, 1);
//         if (ds1.find(4) == ds1.find(0))
//             printf("Yes\n");
//         else
//             printf("No\n");
 
//         if (ds1.find(1) == ds1.find(0)   )
//             printf("Yes\n");
//         else
//             printf("No\n");
//         ds1.printsets();
// }