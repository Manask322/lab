#include<stdio.h>
#include<omp.h>
int fibo(int n,int h);
void main()
{
	int n,fib;
	double t1,t2;
	printf("Enter the value of n:\n");
	scanf("%d",&n);
	t1=omp_get_wtime();
	#pragma omp parallel shared(n)
	{
		#pragma omp single
		{
			printf("Fn called by Thread %d\n",omp_get_thread_num());
			fib=fibo(n,0);
		}
	}
	t2=omp_get_wtime();
	printf("Fib is %d\n",fib);
	printf("Time taken is %f s \n",t2-t1);
}
int fibo(int n,int h)
{
	int a,b;
	if(n<2)
		return n;
	else
	{
		#pragma omp task shared(a)
		{
			printf("Task Created by Thread %d  n: %d \n",omp_get_thread_num(),n-1);
			a=fibo(n-1,h+1);
			printf("Task Executed by Thread %d \ta=%d h: %d  \n",omp_get_thread_num(),a,h+1);
		}
		#pragma omp task shared(b)
		{
			printf("Task Created by Thread %d  n: %d \n",omp_get_thread_num(),n-2);
			b=fibo(n-2,h+2);
			printf("Task Executed by Thread %d \tb=%d h: %d \n",omp_get_thread_num(),b,h+1);
		}
		#pragma omp taskwait
			return a+b;
	}
}
