#include<omp.h>
#include<stdio.h>
int main()
{
	int x=0;
	#pragma omp parallel shared(x)
	{
		int tid=omp_get_thread_num();
		x=x+1;
		printf("thread [%d]\n value of x is %d",tid,x);
	}
}
