#include<stdio.h>
int main()
{
int a[56],b[67],c[45];
int n1,n2,t;
printf("Enter size of two array:\n");
scanf("%d %d",&n1,&n2);
printf("Enter array 1\n");
for(int i=0;i<n1;i++)scanf("%d",&a[i]);
printf("Enter array 2\n");
for(int i=0;i<n2;i++)scanf("%d",&b[i]);
for(int i=0;i<n1-1;i++)
{
for(int j=i+1;j<n1;j++)
{
if(a[i]<a[j])
{
t=a[i];a[i]=a[j];a[j]=t;
}
}
}
for(int i=0;i<n1-1;i++)
{
for(int j=i+1;j<n1;j++)
{
if(b[i]<b[j])
{
t=b[i];b[i]=b[j];b[j]=t;
}
}
}
for(int i=0;i<n1;i++)printf("%d ",a[i]);
printf("\n");
for(int i=0;i<n2;i++)printf("%d ",b[i]);
int i=0,j=0,k=0;
while(i<n1 && j<n2)
{
if(a[i]>b[j])
{
c[k]=a[i];
i++;
}
else 
{
c[k]=b[j];j++;
}
k++;
}
if(i==n1)
{
while(j<n2)
{
c[k]=b[j];j++;k++;
}
}
if(j==n2)
{
while(i<n1)
{
c[k]=a[i];i++;k++;
}
}
printf("\nmerged array:\n");
for(i=0;i<n1+n2;i++)printf("%d ",c[i]);
}

