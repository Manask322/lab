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
        if(min_j==-1){min_j=j;}
        else if(blocks[min_j].size>blocks[j].size)min_j=j;
      }
    }
    
    if(min_j!=-1 && blocks[min_j].is_free==1)
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
      if(blocks[j].size>=process[i] && blocks[j].is_free==1)
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
     if (worst_j != -1 && blocks[worst_j].is_free==1)
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
  int n;
  printf("How many partitions\n");
  scanf("%d",&n);
  int i;
  struct block blocks[n];
  int block_size[n];
  printf("Enter block sizes\n");
  for(i=0;i<n;i++)
  { blocks[i].is_free=1;
    scanf("%d",&blocks[i].size);
    block_size[i]=blocks[i].size;
  }
  printf("How many process you want\n");
  int m;
  scanf("%d",&m);
  int process[m];
  printf("Enter process size\n");
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
  }
  while(1)
  {
      printf("Enter any number to continue to delete process or -1 to exit \n");
      scanf("%d",&o);
      if(o==-1)break;
      printf("Enter the block you want to free(indexed at 0) if you dont want to free anything enter -1\n");
      int p;
      scanf("%d",&p);
      if(p!=-1){blocks[p].size=block_size[p];blocks[p].is_free=1;}
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