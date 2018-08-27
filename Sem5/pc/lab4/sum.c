#include<stdio.h>
#include<omp.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a[n][n];
	for(int i=0;i<n;i++)for(int j=0;j<n;j++)scanf("%d",&a[i][j]);
		int row[n];
		int column[n];
		for(int i=0;i<n;i++){row[i]=0;column[i]=0;}
	#pragma omp parallel
	{
		#pragma omp for collapse(2)
		for(int id=0;id<n;id++)
		{
			for(int i=0;i<n;i++)
			{
				row[id]+=a[id][i];
				column[id]+=a[i][id];
			}
		}
	}
	for(int i=0;i<n;i++)
	{
		printf("%d  %d %d \n",i,row[i],column[i]);
	}

}