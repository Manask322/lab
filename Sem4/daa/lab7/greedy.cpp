#include<bits/stdc++.h>
void merge(int arr[][2], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
   
    int L[n1][2], R[n2][2];
 
    for (i = 0; i < n1; i++)
        {L[i][0] = arr[l + i][0];L[i][1]=arr[l+i][1];}
    for (j = 0; j < n2; j++)
        {R[j][0] = arr[m + 1+ j][0];R[j][1]=arr[m+1+j][1];}

    i = 0;
    j = 0; 
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i][1] <= R[j][1])
        {
            arr[k][0] = L[i][0];
            arr[k][1]=L[i][1];
            i++;
        }
        else
        {
            arr[k][0] = R[j][0];
            arr[k][1]=R[j][1];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k][0] = L[i][0];
        arr[k][1]=L[i][1];
        i++;
        k++;
    }
 
    while (j < n2)
    {
        arr[k][0] = R[j][0];
        arr[k][1]=R[j][1];
        j++;
        k++;
    }
}
void mergeSort(int arr[][2], int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}
int main()
{    int n=8;
     int intervals[8][2]={{1 ,3},{2 ,8},{2 ,5},{3 ,7},{4, 8},{4, 6},{6 ,12},{7 ,10}};
     mergeSort(intervals,0,7);
    //  for(int i=0;i<8;i++)
    //  {
    //      printf("%d %d\n",intervals[i][0],intervals[i][1]);
    //  }
     int count=0;
     printf("%d %d\n",intervals[0][0],intervals[0][1]);
    for(int i=count;i<8;i++)
    {   
         if(intervals[i][0]>intervals[count][1])
         {    
             printf("%d %d\n",intervals[i][0],intervals[i][1]);
             count=i;
         }
    }
}