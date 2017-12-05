#include <stdio.h>
#include <unistd.h>
int pfork(int);
int main()
{
        int i;
        printf("i : %d ",i);
        i=pfork(3);
        if(i==0)
        {
                printf("Parent \n");
                printf("i when 0 \n");
                printf("Getpid : %d getppid : %d\n",getpid(),getppid());
                printf("\n");
        }
        else if(i==1)
        {
                printf("Child \n");
                printf("i when 1 \n");
                printf("Getpid : %d getppid : %d\n",getpid(),getppid());
                printf("\n");

        }
        else if(i==2)
        {
                printf("Child \n");
                printf("i when 2 \n");
                printf("The Getpid is : %d getppid : %d\n",getpid(),getppid());
                printf("\n");
        }
}
int pfork(int x)
{
        int j;
        for(j=1;j<x;j++)
        {
                if(fork()==0)
                {
                        return j;
                }
        }
        return 0;
}