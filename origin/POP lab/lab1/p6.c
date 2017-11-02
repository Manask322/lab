#include<stdio.h>
int main()
{
int n,a[67];
scanf("%d",&n);
int max=0,min=56000,max_i,min_i;
for(int i=0;i<n;i++)
{scanf("%d",&a[i]);
if(a[i]>max){max=a[i];max_i=i;}
if(a[i]<min)min=a[i];min_i=i;}

//printf("%d %d",max,min);
int t;
t=a[max_i];
a[max_i]=a[min_i];
a[min_i]=t;printf("\n");
for(int i=0;i<n;i++)printf("%d ",a[i]);
}
