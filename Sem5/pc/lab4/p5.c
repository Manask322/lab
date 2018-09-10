#include <stdio.h>
#include <omp.h>
int main()
{
	int i,j;
	int total=0;
	int n=3;
	int emp[n][n];
	for(i=0;i<n;i++)		//initialise the array
	{
		for(j=0;j<n;j++)
		{
			emp[i][j]=4000*i*j;
			// printf("%d\n",emp[i][j]);
		}
	}
	double t1=omp_get_wtime();
	#pragma omp parallel num_threads(4) reduction(+:total)
	{
		#pragma omp for collapse(2)
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				int add=0.06*emp[i][j];
				emp[i][j]+=add;
				total+=add;

				if(emp[i][j]>5000)
				{
					int sub=0.02*emp[i][j];
					emp[i][j]-=sub;
					total-=sub;
				}
				// printf("Total= %d thread= %d\n",total,omp_get_thread_num());
			}
		}
	}
	printf("Total expenditure: %d\n",total);
	double t2=omp_get_wtime();
	printf("Total time taken: %lf",t2-t1);
}