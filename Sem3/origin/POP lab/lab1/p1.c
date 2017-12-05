#include<stdio.h>
int main()
{
for(int i=1;i<=5;i++)
{
for(int s=1;s<=6-i;s++)
printf(" ");
for(int j=1;j<=2*i-1;j++)
printf("%d",j);
printf("\n");
}
for(int i=4;i>=1;i--)
{
for(int s=1;s<=6-i;s++)
printf(" ");
for(int j=1;j<=2*i-1;j++)
printf("%d",j);
printf("\n");
}

}
