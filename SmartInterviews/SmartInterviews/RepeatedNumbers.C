#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void merge(int a[],int lo,int mid,int hi)
{
    int c[hi-lo+1],i = lo,j=mid+1,k=0;
    while(i<=mid && j<=hi)
    {
        if(a[i]>a[j])
            c[k++]=a[j++];
        else
            c[k++]=a[i++];
    }
    while(i<=mid)
        c[k++]=a[i++];
    while(j<=hi)
        c[k++]=a[j++];
    for(int i=lo,k=0;i<=hi;i++,k++)
        a[i]=c[k];
}
void mergeSort(int a[],int lo,int hi)
{
    if(lo == hi)
        return;
    int mid = (lo+hi)/2;
    mergeSort(a,lo,mid);
    mergeSort(a,mid+1,hi);
    merge(a,lo,mid,hi);
}

int main() {
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        int arr[n];
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);
        mergeSort(arr,0,n-1);
        /*
        for(int i=0;i<n;i++)
            printf("%d ",arr[i]);
        printf("\n");
        */
        int p1 = 0,p2 = n-1;
        for(int i=0;i<n-1;i++)
        {
            if(arr[i]==arr[i+1])
                printf("%d ",arr[i]);
        }
        printf("\n");
    }
    return 0;
}
