#include<bits/stdc++.h>
using namespace std;
int** fw(int** adj_matrix,int n)
{   int ***pred=(int ***)malloc(n*sizeof(int **));
    for(int k=0;k<n;k++)
    {
        pred[k]=(int **)malloc(n * sizeof(int *));
        for (int i=0; i<n; i++)
            pred[k][i] = (int *)malloc(n * sizeof(int));
    }
    int **prev=adj_matrix;
    int **next= (int **)malloc(n * sizeof(int *));
    for (int i=0; i<n; i++)
         next[i] = (int *)malloc(n * sizeof(int));
    int **pred_initial= (int **)malloc(n * sizeof(int *));
    for (int i=0; i<n; i++)
         pred_initial[i] = (int *)malloc(n * sizeof(int));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            pred_initial[i][j]=-1;
        }
    }
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                next[i][j]=min(prev[i][k]+prev[k][j],prev[i][j]);
                if(prev[i][k]+prev[k][j]>prev[i][j])
                {
                    pred[k][i][j]=pred[k-1][i][j];
                }
                else{
                    pred[k][i][j]=pred[k-1][k][j];
                }
            }
        }
        prev=next;
    }
    printf("path from 1 to 4\n");
    for(int k=0;k<n;k++)
    {
        printf("%d",pred[k][0][3]);
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
