#include<bits/stdc++.h>
using namespace std;
int** fw(int** adj_matrix,int n)
{
    int **prev=adj_matrix;
    int **next= (int **)malloc(n * sizeof(int *));
    for (int i=0; i<n; i++)
         next[i] = (int *)malloc(n * sizeof(int));
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                next[i][j]=min(prev[i][k]+prev[k][j],prev[i][j]);
            }
        }
        prev=next;
    }
    return prev;
}
int main()
{
    printf("Enter number of vertices,edges\n");
    int n,m;
    scanf("%d %d",&n,&m);
    int **adj_matrix = (int **)malloc(n * sizeof(int *));
    for (int i=0; i<n; i++)
         adj_matrix[i] = (int *)malloc(n * sizeof(int));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(i==j)
            {
                adj_matrix[i][j]==0;
            }
            else{
                adj_matrix[i][j]=INT_MAX/2;
            }
        }
    }
    printf("Enter edge and weights\n");
    for(int i=0;i<m;i++)
    {   int a,b,w;
        scanf("%d %d %d",&a,&b,&w);
        adj_matrix[a-1][b-1]=w;
    }
    int **path=fw(adj_matrix,n);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%d to %d : %d\n",i+1,j+1,path[i][j]);
        }
    }

}
