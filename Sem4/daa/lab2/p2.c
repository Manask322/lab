#include<stdio.h>
#include<stdlib.h>
// int peak(int a[],int low,int high);
int peak(int *a,int low,int high)
{   if(low==high)return a[low];
	if(low<=high)
	{
		int mid=(low+high)/2;
		if(mid-1<0)return a[high];
		if(a[mid]>a[mid-1])return peak(a,mid,high);
		else
		{   
			if(a[mid-1]>a[mid])return peak(a,low,mid-1);
			else return a[mid];
		}
	}
	return -1;
}
void  main()
{
	int a[]={2,4,6,8,7,5,3};
	int b[]={10, 12, 8, 4 , -3, -15};
	int a1=peak(a,0,6);
	printf("%d\n",a1);
	printf("%d",peak(b,0,5));
}