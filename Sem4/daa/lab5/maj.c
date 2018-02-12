#include<stdio.h>
int cmp(int x,int y)
{
	return x==y? x:-1;
}
int maj(int *a,int low,int high)
{
   if(high-low==0) return a[0];
   if(high-low==1) return cmp(a[0],a[1]);
   else
   {  int mid=(low+high)/2;
   	  int x=maj(a,low,mid);
   	  int c=0;
      for(int i=low;i<=high;i++)
      	if(cmp(x,a[i])!=-1)c++;
      if(c>((high-low)+1)/2)return x;
      int y=maj(a,mid+1,high);
   	  c=0;
      for(int i=low;i<=high;i++)
      	if(cmp(y,a[i])!=-1)c++;
      if(c>((high-low)+1)/2)return y;
      return -1;
   }
}
int main()
{
   int a[]={1,2,0,1,2,4,1,1,1,2,1,1};
   printf("%d\n", maj(a,0,11));
}
