#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void merge(int a[],int lo,int m,int hi)
{
    int i=lo,k=0,j=m+1,b[hi-lo+1];
    for(int x=0;x<hi-lo+1;x++)
        b[x]=0;
    while(i<=m && j<=hi)
    {
        if(a[i]>a[j])
            b[k++]=a[j++];
        else
            b[k++]=a[i++];
    }
    while(i<=m)
        b[k++]=a[i++];
    while(j<=hi)
        b[k++]=a[j++];
    for(i=lo,k=0;i<=hi;i++,k++)
        a[i]=b[k];
}
void mergeSort(int a[],int lo,int hi)
{
    if(lo<hi)
    {
        int m = (lo+hi)/2;
        mergeSort(a,lo,m);
        mergeSort(a,m+1,hi);
        merge(a,lo,m,hi);
    }
    return;
}

int BSR(int a[],int lo,int hi,int K)
{
    
    if(lo<=hi)
    {
        
        int mid = lo+(hi-lo)/2;    
        //printf("lo=%d mid = %d hi=%d K=%d a[mid]=%d\n",lo,mid,hi,K,a[mid]);
        if(a[mid]==K)
            return 1;
        else if(K<a[mid])
            return BSR(a,lo,mid-1,K);
        else
            return BSR(a,mid+1,hi,K);
    }
    return 0;
}
int main() {
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,k,i;
        scanf("%d%d",&n,&k);
        int arr[n];
        for(i=0;i<n;i++)
            scanf("%d",&arr[i]);
        mergeSort(arr,0,n-1);
        for(i=0;i<n;i++)
        {
            //printf("%d ",arr[i]);
            if(BSR(arr,i+1,n-1,k-arr[i]))
            {
                printf("True\n");
                i = -1;
                break;
            }
        }
        if(i!=-1)
            printf("False\n");
    }
    return 0;
}
