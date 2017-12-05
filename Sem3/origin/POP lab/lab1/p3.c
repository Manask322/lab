#include<stdio.h>
int main()
{
int i,j,a[67][45];
int n;scanf("%d",&n);
for(i=0;i<n;i++)
 for(j=0;j<n;j++)  
  scanf("%d",&a[i][j]);
 for(i=0;i<n;i++)
{
for(j=0;j<n;j++)  
{
if(j<=i)
printf("%d",a[i][j]);

}
printf("\n"); 
}



}
