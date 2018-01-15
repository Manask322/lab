#include<stdio.h>
#include<stdlib.h>
void bestfit(int blocks[],int n)
{ 
    int process;
    printf("Enter process size");
    scanf("%d",&process);
    int min_i=-1;int min=56000;
    for(int i=0;i<n;i++)
    {   
    	if(blocks[i]>process)
    	{
                 if(blocks[i]<min)
                 {min=blocks[i];min_i=i;}
    	}
    }
}