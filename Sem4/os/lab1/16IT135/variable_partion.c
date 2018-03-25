#include<stdio.h>
#include<stdlib.h>
struct block
{  
   int size;//The Size of the block that is free.
   int end;//end address of the block
   int start;//Start address of the block.
   int is_free;//A flag to see if the block is free.
};
//The functions for allocating the blocks are:
//1.Best Fit.
//2.First Fit.
//3.Worst Fit.

//Allocation for best fit
void  best_allocate(struct block blocks[],int m,int process[],int n)
{
  int al_process[n];
  int i,j;
  for(i=0;i<n;i++)al_process[i]=-1;
  for(i=0;i<n;i++)
  {
    int min_j=-1;
    for(j=0;j<m;j++)
    {
      if(blocks[j].size>=process[i])
        if(min_j==-1)min_j=j;
        else if(blocks[min_j].size>blocks[j].size)min_j=j;
      }
    if(min_j!=-1)
    { 
      al_process[i]=min_j;
      blocks[min_j].size-=process[i];
      blocks[min_j].is_free=0;
      blocks[min_j].end+=process[i];
    }
  }
  for(i=0;i<n;i++)
  { if(al_process[i]!=-1)
    printf(" Process size:%d  From:%d to %d  \n",process[i],blocks[al_process[i]].end-process[i],blocks[al_process[i]].end);
    else
    printf("  Process size:%d  Block:Not allocated \n",process[i]);
  }
}
//Allocation for first fit
void first_allocate(struct block blocks[],int m,int process[],int n)
{
  int al_process[n];
  int i,j;
  for(i=0;i<n;i++)al_process[i]=-1;
  for(i=0;i<n;i++)
  {
    for(j=0;j<m;j++)
    {
      if(blocks[j].size>=process[i])
      {
        al_process[i]=j;
        blocks[j].size-=process[i];
        blocks[j].is_free=0;
        break;
      }
    }
  }
  for(i=0;i<n;i++)
  { if(al_process[i]!=-1)
    printf("  Process size:%d  From:%d to %d  \n",process[i],blocks[al_process[i]].start,blocks[al_process[i]].start+process[i]);
    else
    printf(" Process size:%d  Block:Not allocated \n",process[i]);
  }
}
//Allocation for worst fit
void worst_allocate(struct block blocks[],int m,int process[],int n)
{
   int al_process[n];
   int i,j;
   for(i=0;i<n;i++)al_process[i]=-1;
   for(i=0;i<n;i++)
   {
     int worst_j=-1;
     for(j=0;j<m;j++)
     {
       if(blocks[j].size>=process[i])
       {
         if(worst_j==-1)worst_j=j;
         else if(blocks[worst_j].size>=process[i])worst_j=j;
       }
     }
     if (worst_j != -1)
        {
            al_process[i] = worst_j;
            blocks[worst_j].size -= process[i];
            blocks[worst_j].is_free=0;
        }
   }
  for(i=0;i<n;i++)
  { if(al_process[i]!=-1)
    printf("  Process size:%d  From:%d to %d  \n",process[i],blocks[al_process[i]].start,blocks[al_process[i]].start+process[i]);
    else
    printf(" Process size:%d  Block:Not allocated \n",process[i]);
  }
}
int main()
{

  printf("Enter the number of processes\n");
  int n;
  scanf("%d",&n);
  printf("Enter the process\n");
  int i;
  //Creating blocks of equal size.
  struct block blocks[n];
  //An array containing process size.
  int process[n];
  for(i=0;i<n;i++){scanf("%d",&process[i]);blocks[i].size=0;}
  //Initializing the first block properties.
  blocks[0].start=0;
  blocks[0].end=blocks[0].start+process[0];
  //Setting the start and end values for the block "block[i].start=block[i-1].start+process[i-1]".
  //Setting the the end value for the block "blocks[i].end=blocks[i].start+process[i]"
  for(i=1;i<n;i++){blocks[i].start=blocks[i-1].start+process[i-1];blocks[i].end=blocks[i].start+process[i];}
  printf("Memory allocated to all!\n");
  //Display the values. 
 for(i=0;i<n;i++)
  { 
    printf("Process no.:%d  Process size:%d  From:%d to %d  \n",i+1,process[i],blocks[i].start,blocks[i].start+process[i]);
  }
  int o;
  while(1)
  {
      printf("Enter -1 to exit or anyother to continue\n");
      scanf("%d",&o);
      if(o==-1)break;
      printf("Enter the process you want to free(indexed at 0) if you dont want to free anything enter -1\n");
      int p;
      scanf("%d",&p);
      //Deleting a block.
      //Reducing the size of free block to its original size.	
      //Reducing the end pointer of the blocks.	
      if(p!=-1){blocks[p].size=process[p];blocks[p].end-=process[p];}
      printf("Enter the process size you want to enter");
      int p1[1];
      scanf("%d",&p1[0]);
      printf("Which fit?\n1.Best\n2.First\n3.worst\n");
      int op;
      scanf("%d",&op);
      switch(op)
      {
       case 1: best_allocate(blocks,n,p1,1);
            break;
       case 2: first_allocate(blocks,n,p1,1);
            break;  
       case 3:worst_allocate(blocks,n,p1,1);
            break;  
      }
      
    }

}
