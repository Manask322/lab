#include<mpi.h>
#include<stdio.h>
int main(int argc,char *argv[ ])
{
    int size,myrank,x,i,flag;
    MPI_Status status;
    MPI_Request request;
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    MPI_Comm_rank(MPI_COMM_WORLD,&myrank);

    if(myrank==0)
    {
        x=10;
        MPI_Send(&x,1,MPI_INT,1,25,MPI_COMM_WORLD); // Tag is different at reciever
        for(i=0;i<5;i++)
        MPI_Send(&i,1,MPI_INT,1,i,MPI_COMM_WORLD);
        printf("p0 done");
    } 
    else if(myrank==1)
    {
        printf("Value of x is : %d\n",x);
        MPI_Recv(&x,1,MPI_INT,0,25,MPI_COMM_WORLD,&status);
        MPI_Test(&request,&flag,&status);
        printf("Test %d %d %d\n",flag,status.MPI_SOURCE,status.MPI_TAG);
        printf("Process %d of %d, Value of x is %d\n",myrank,size,x);
        printf("Source %d Tag %d \n",status.MPI_SOURCE,status.MPI_TAG);
        for(i=0;i<5;i++)
        {
            MPI_Recv(&i,1,MPI_INT,0,i,MPI_COMM_WORLD,&status);
            
            printf("Received i : %d\n",i);
            printf("Test1 %d %d %d\n",flag,status.MPI_SOURCE,status.MPI_TAG);
        }
    }
    MPI_Finalize();
    return 0;
}