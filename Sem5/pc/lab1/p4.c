#include<stdio.h>
#include<omp.h>
int main()
{
	int i=10;
	printf("Value before pragma i=%d\n",i);
	#pragma omp parallel num_threads(4) firstprivate(i)
	{
		printf("value after entering pragma i=%d tid=%d\n",i,omp_get_thread_num());
		i=i+omp_get_thread_num();
		printf("value after changing value i=%d tid=%d",i,omp_get_thread_num());
	}
}