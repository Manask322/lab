#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
int a[n];
int i;
for(i=0;i<n;i++)printf("%p\n",&a[i]);
}
