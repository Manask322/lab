#include<stdio.h>
#include<string.h>
#include<omp.h>
#include<stdlib.h>
int main()
{
	int n=1000;
	// scanf("%d",&n);
	// int a[n][n];
	// int b[n][n];
	int **a=(int **)malloc(n*sizeof(int *));
	for(int i=0;i<n;i++)
	{
	    a[i]=(int *)malloc(n*sizeof(int));
	}
	int **b=(int **)malloc(n*sizeof(int *));
	for(int i=0;i<n;i++)
	{
	    b[i]=(int *)malloc(n*sizeof(int));
	}
	for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i][j]=1;
	for(int i=0;i<n;i++)for(int j=0;j<n;j++)b[i][j]=1;	
	// int result[n][n];
	// for(int i=0;i<n;i++)for(int j=0;j<n;j++)result[i][j]=0;
	int **result=(int **)malloc(n*sizeof(int *));
	for(int i=0;i<n;i++)
	{
	    result[i]=(int *)malloc(n*sizeof(int));
		memset(result[i],0,n*sizeof(int));
	}
	// memset(result, 0, sizeof(result[0][0]) *n * n);
	double t1=omp_get_wtime();
	#pragma omp parallel num_threads(4)
	{
		#pragma omp for collapse(3)
		for(int i=0; i<n; ++i)
			for(int j=0; j<n; ++j)
				for(int k=0; k<n; ++k)	
            {
                result[i][j]+=a[i][k]*b[k][j];
            }
	}
	double t2=omp_get_wtime();
	printf("Time taken :%f\n",t2-t1);
}
