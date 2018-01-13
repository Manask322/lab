#include<stdio.h>
#include<stdlib.h>
struct block
{
   int size;
   int is_free;
};
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
      {
        if(min_j==-1)min_j=j;
        else if(blocks[min_j].size>blocks[j].size)min_j=j;
      }
    }
    if(min_j!=-1)
    {
      al_process[i]=min_j;
      blocks[min_j].size-=process[i];
      blocks[min_j].is_free=0;
    }
  }
  for(i=0;i<n;i++)
  { if(al_process[i]!=-1)
    printf("Process no.:%d  Process size:%d  Block:%d Free memory in block:%d \n",i+1,process[i],al_process[i]+1,blocks[al_process[i]].size);
    else
    printf("Process no.:%d  Process size:%d  Block:Not allocated \n",i+1,process[i]);
  }
}
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
    printf("Process no.:%d  Process size:%d  Block:%d Free memory in block:%d \n",i+1,process[i],al_process[i]+1,blocks[al_process[i]].size);
    else
    printf("Process no.:%d  Process size:%d  Block:Not allocated \n",i+1,process[i]);
  }
}
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
    printf("Process no.:%d  Process size:%d  Block:%d Free memory in block:%d \n",i+1,process[i],al_process[i]+1,blocks[al_process[i]].size);
    else
    printf("Process no.:%d  Process size:%d  Block:Not allocated \n",i+1,process[i]);
  }
}
int main()
{
  // int blockSize[] = {100, 500, 200, 300, 600};
  //   int processSize[] = {212, 417, 112, 426};
  int n;
  printf("How many partitions\n");
  scanf("%d",&n);
  int i;
  struct block blocks[n];
  printf("Enter sizes\n");
  for(i=0;i<n;i++)
  { blocks[i].is_free=1;
    scanf("%d",&blocks[i].size);
  }
  printf("How many process you want\n");
  int m;
  scanf("%d",&m);
  int process[m];
  printf("Enter process\n");
  for(i=0;i<m;i++)
  {
  scanf("%d",&process[i]);  
  } 
  printf("Which fit?\n1.Best\n2.First\n3.worst\n");
  int o;
  scanf("%d",&o);
  switch(o)
  {
   case 1: best_allocate(blocks,n,process,m);
          break;
   case 2: first_allocate(blocks,n,process,m);
           break;  
    case 3:worst_allocate(blocks,n,process,m);
           break;  
  //  case 4:best_allocate(blocks,n,process,m);
  //         printf("********************\n");
  //         first_allocate(blocks,n,process,m);
  //         printf("********************\n");
  //         worst_allocate(blocks,n,process,m);
  }
}