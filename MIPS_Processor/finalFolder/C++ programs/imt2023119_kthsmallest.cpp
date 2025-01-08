#include<bits/stdc++.h>
using namespace std;
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
	while(low<high)
	{
		mid=(low+high)/2;
		if(lsearch(a,n,mid)<k)
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
    cout<<"Enter the size of the array ";
    int n;
    cin>>n;
    cout<<"Enter the elements of the array\n";
    int a[100];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int k;
    cout<<"Enter the value of k ";
    cin>>k;
	cout<<bsearch(a,n,k)<<"\n";
}