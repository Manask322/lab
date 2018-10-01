#include <stdio.h>
#include <sys/time.h>
#include <omp.h>
#include <stdlib.h>
#include<limits.h>
struct timeval TimeValue_Start;
struct timezone TimeZone_Start;
struct timeval TimeValue_Final;
struct timezone TimeZone_Final;
long time_start, time_end;
double time_overhead;
int main()
{
    int n=10000000;
    int *a;
    a=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++)a[i]=i;
    int min1=INT_MAX;
    gettimeofday(&TimeValue_Start, &TimeZone_Start);
    #pragma omp parallel
    {   
        #pragma omp for reduction(min:min1)
        for(int i=0;i<n;i++)
        {
            if(a[i]<min1)min1=a[i];
        }
    }
    printf("%d",min1);
    gettimeofday(&TimeValue_Final, &TimeZone_Final);
    time_start = TimeValue_Start.tv_sec * 1000000 + TimeValue_Start.tv_usec;
    time_end = TimeValue_Final.tv_sec * 1000000 + TimeValue_Final.tv_usec;
    time_overhead = (time_end - time_start)/1000000.0;
    printf("\n\n\tTime in Seconds (T) : %lf\n",time_overhead);
}