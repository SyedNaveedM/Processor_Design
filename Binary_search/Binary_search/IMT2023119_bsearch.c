#include<stdio.h>
//The following function returns the index of the key given using binary search and returns -1 if the element is not present in the array
int bisearch(int a[],int n,int key)
{
        int mid,i=0,j=n-1;
        do
        {
                mid=(i+j)/2;
                if(a[mid]>key)
                {
                        j=mid-1;
                }
                else if(a[mid]<key)
                {
                        i=mid+1;
                }
                else
                {
                        return mid;
                }
        }
        while(i<=j);
        return -1;
}
int main()
{
        int key,n;
        int a[10]={1, 3, 7, 9, 12, 13, 16, 18, 25, 35};
        key=25;
        printf("%d ", bisearch(a, 10, key));
}

