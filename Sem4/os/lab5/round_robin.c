#include<stdio.h>
int block[20];
int bottom=-1;
void swap(int *bt,int *at,int *pr_id,int i,int j)
{
    int t=at[i];at[i]=at[j];at[j]=t;
    t=bt[i];bt[i]=bt[j];bt[j]=t;
    t=pr_id[i];pr_id[i]=pr_id[j];pr_id[j]=t;
}
int findWaitingTime( int n,int bt[], int wt[],int at[], int quantum,int pr_id[])
{   int cs=-1;
	int rem_bt[n];
	for (int i = 0 ; i < n ; i++)
		rem_bt[i] = bt[i];
	int t = 0; 
	while (1)
	{
		int done = 1;
		for (int i = 0 ; i < n; i++)
		{
			if (rem_bt[i] > 0)
			{  bottom+=1;
                block[bottom]=pr_id[i];
				done = 0;
                cs+=1; 
				if (rem_bt[i] > quantum)
				{   
					t += quantum;
					rem_bt[i] -= quantum;
				}

				else
				{
					t = t + rem_bt[i];
					wt[i] = t - at[i]-bt[i];

					rem_bt[i] = 0;
				}
			}
		}
		if (done ==1)
		break;
	}
return cs;
}
void findTurnAroundTime( int n,int bt[], int wt[], int tat[])
{
	for (int i = 0; i < n ; i++)
		tat[i] = bt[i] + wt[i];
}
void findavgTime( int pr_id[],int n, int bt[],int quantum,int at[])
{
	int wt[n], tat[n], total_wt = 0, total_tat = 0;

	int cs=findWaitingTime(n, bt, wt,at ,quantum,pr_id);

	findTurnAroundTime( n, bt, wt, tat);
    printf("Process   Waiting-time tot  \n");
	for (int i=0; i<n; i++)
	{
		total_wt = total_wt + wt[i];
		total_tat = total_tat + tat[i];
        
        printf("%d             %d         %d\n",pr_id[i],wt[i],tat[i]);
	}
    float ans1=total_wt/n;
    float ans2=total_tat/n;
    printf("Average waiting time :%f Average tat : %f\n",ans1,ans2);
    printf("Context switches:%d\n",cs);
}
void sort_at(int *at,int *bt,int *pr_id,int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(at[j]>at[j+1])
            {
                swap(bt,at,pr_id,j,j+1);
            }
        }
    }
}
int main()
{   for(int i=0;i<20;i++)block[i]=-1;
    int n=4;
	int bt[] = {9, 5, 3,4};
    int pr_id[]={1,2,3,4};
	int quantum = 5;
    int at[]={0,1,2,3};
    sort_at(at,bt,pr_id,n);
	findavgTime(pr_id,n, bt, quantum,at);
    printf("BLock:\n");
    for(int i=0;;i++)
    {
        if(block[i]==-1){break;}
        printf("%d ",block[i]);
    }
	return 0;
}   