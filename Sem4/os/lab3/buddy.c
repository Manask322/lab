#include<stdio.h>
#include<math.h>
#define left_child(index) ((index) * 2 + 1)
#define right_child(index) ((index) * 2 + 2)
#define parent(index) ( ((index) + 1) / 2 - 1)
int Mem_total;
int nodes(int level)
{
	
}
int left_most(int level)
{

}
void main()
{   printf("Enter the total memory size");
    scanf("%d",&Mem_total);
	double k=log(Mem_total)/log(2)+1
	int head=(int)(log(Mem_total)/log(2));
	k=log(size)/log(2)+1
	int n=(int)(pow(k+1,2)-1);
	int tree[n];
	for(int i=1;i<n;i++)tree[i]=0;
    int process;
    scanf("%d",&process);
    process=ceil(log(process)/log(2))
    for(int i=0;i<k;i++)
    {   int level=i;
    	int val=(int)(head/pow(2,i));
    	if(val<=process)
    	{
    	    
    	}
    }
}