#include<stdio.h>
#include<omp.h>
void main()
{
	int x=0,i,n;
	printf("Enter the value of n");
	scanf("%d",&n);
	int a[n];
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	#pragma omp parallel
	{
		int id=omp_get_thread_num();
		#pragma omp for
		for(i=0;i<n;i++)
		{
			printf("Thread %d : value of i: %d\n",id,i);
			x+=a[i];
			printf("Thread %d : x is %d\n",id,x);
		}
	}
	printf("sum is %d\n",x);
	//printf("i is %d\n",i);
}

