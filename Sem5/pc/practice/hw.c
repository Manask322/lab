#include<stdio.h>
#include<omp.h>
int main()
{   int id;
    #pragma omp parallel num_threads(6) private(id)
    {  id=omp_get_thread_num();
        printf("Hello World: %d\n ",id);
    }
}