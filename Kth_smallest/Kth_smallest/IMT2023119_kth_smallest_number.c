#include<stdio.h>
int lsearch(int a[],int n,int mid)
{
	int count=0;
	for(int i=0;i<n;i++)
	{
		if(a[i]<=mid)
		{
			count+=1;
		}
	}
	return count;
}
int bsearch(int a[],int n,int k)
{
	int low=a[0],high=a[0],mid;
	for(int i=0;i<n;i++)
	{
		if(a[i]<low)
		{
			low=a[i];
		}
		else if(a[i]>high)
		{
			high=a[i];
		}
	}
	while(low<high)//here
	{
		mid=(low+high)/2;
		if(lsearch(a,7,mid)<k)
		{
			low=mid+1;
		}
		else
		{
			high=mid;
		}
	}
	return low;
}

int main()
{
	int a[7]={3,1,4,2,5,7,9};
	int k=3;
	printf("%d\n",bsearch(a,7,k));
}
