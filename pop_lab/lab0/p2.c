#include<stdio.h>
int reverse(int *n)
{
int b,num=*n,d=0;
while(num!=0)
{
b=num%10;
d=d*10+b;
num=num/10;
}
return d;
}
int main()
{
int n;
scanf("%d",&n);
int *p;
p=&n;
printf("%d",reverse(p));
}
