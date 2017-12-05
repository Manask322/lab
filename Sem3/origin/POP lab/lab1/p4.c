#include<stdio.h>
int main()
{
int i,k,j,r1,c1,r2,c2;
printf("Enter row and column for two matrices");
scanf("%d %d %d %d",&r1,&c1,&r2,&c2);
if(c1!=r2)printf("Matrix multiplication cannot be done");
else
{
int a[45][45],b[45][45],c[45][45];
printf("Enter elements of matrix 1");
for(i=0;i<r1;i++)
for(j=0;j<c1;j++)
scanf("%d",&a[i][j]);
printf("Enter elements of matrix 2");
for(i=0;i<r2;i++)
for(j=0;j<c2;j++)
scanf("%d",&b[i][j]);
for(i=0;i<r1;i++)
{
for(j=0;j<c2;j++)
{
   c[i][j]=0;
   for(k=0;k<c1;k++)
   {
    c[i][j]+=a[i][k]*b[k][j];
   }
}
}
for(i=0;i<r1;i++)
{
for(j=0;j<c2;j++)
printf("%d ",c[i][j]);
printf("\n");
}

}
}
