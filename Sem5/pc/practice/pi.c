#include<stdio.h>
#include<omp.h>
static long num_steps=1000000;
double step;
int main()
{
    int nthreads;double x,pi,sum[nthreads];
    step=1.0/(double)num_steps;
    #pragma omp parallel
    {
        int  i,id=omp_get_thread_num();
        for(i=id,sum[id]=0;i<num_steps;i+=nthreads)
        {   
            
                x=(i+0.5)*step;
                sum[id]+=4.0/(1.0+x*x);
            
        }
    }
    for(int i=0,pi=0;i<nthreads;i++)pi+=sum[i];
}