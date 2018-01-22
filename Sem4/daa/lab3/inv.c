#include<stdlib.h>
#include<stdio.h>
int count=0;
void split_inv(int *arr, int l, int m, int r)
{   

    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    i = 0; 
    j = 0; 
    k = l; 
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {   count+=n1-i;
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
   
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
   
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
    // printf("%d %d %d\n",count,l,r);
    // return count;
}
void sort_inv(int *arr, int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
        sort_inv(arr, l, m);
        sort_inv(arr, m+1, r);
        split_inv(arr, l, m, r);
        // printf("%d %d %d",il,ir,is );
        // return il+ir+is;
    }
}
void main()
{
    int a[5]={1,2,3,5,4};
    sort_inv(a,0,5);
    printf("%d",count);

}