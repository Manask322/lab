#include<stdio.h>
void swap(int *a,int *b,int c,int d)
{
int t;
t=*a;*a=*b;*b=t;t=c;c=d;d=t;
}
int main()
{
int a ;int b;int c;int d;
a=1;b=2;c=3;d=4;
int *p1;int *p2;
p1=&a;p2=&b;
printf("before swapping a:%d\nb:%d\nc:%d\nd:%d\n",*p1,*p2,c,d);
swap(p1,p2,c,d);
printf("after swapping a and b by reference,c,d by value \na:%d\nb:%d\nc:%d\nd:%d\n",*p1,*p2,c,d);

}
