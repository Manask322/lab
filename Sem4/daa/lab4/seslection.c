#include<stdio.h>
int kthelem(int *arr,int l,int r,int k);
int swap(int *a,int *b)
{
    int t=*a;*a=*b;*b=t;
}
int findmed(int *arr,int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i-1;j++)
        {
            if(arr[j] >arr[j+1])
            {
                swap(&arr[j],&arr[j+1]);
            }
        }
    }
    return arr[(int)n/2];
}
int partition(int * arr,int l,int r,int x)
{   int i; 
    for(i=l;i<=r;i++)
    {if (arr[i]==x) break;}
    swap(&arr[i],&arr[r]);  
    i=l;
    for(int j=l;j<=r-1;j++)
    {
        if(arr[j]<=x)
        {
            swap(&arr[j],&arr[i]);
            i++;
        }
    }
    swap(&arr[i],&arr[r]);
    return  i;
}
int kthelem(int *arr,int l,int r,int k)
{
    if(k>0 && k<=r-l+1)
    {
        int n=r-l+1;
        int i,median[(n+5)/5];
        for(int i=0;i<n/5;i++)
        median[i]=findmed(arr+l+i*5,5);
        if(i*5<n)
        {
            median[i]=findmed(arr+l+i*5,n%5);
            i++;
        }
        int medofmed = (i==1)? median[i-1] : kthelem(median,0,i-1,i/2);
        int pos=partition(arr,l,r,medofmed);
        if(pos-l+1==k)return arr[pos];
        else if(pos-l>k-1)return kthelem(arr,l,pos-1,k);
        else return  kthelem(arr,pos+1,r,k-pos+l-1);

    }
}
int main()
{   
    int arr[] = {12, 3, 5, 7, 4, 19, 26};
    int n = sizeof(arr)/sizeof(arr[0]), k = 3;
    printf("%d\n",kthelem(arr, 0, n-1, k));
    return 0;
}