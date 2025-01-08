#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[100];
    int size,sum;
    cout<< "Enter the size of the array ";
    cin>>size;
    cout<<"Enter the elements of the array(Each element in a new line)\n";
    for(int i=0;i<size;i++)
    {
        cin>>a[i];
    }
    cout<<"Enter the value of sum ";
    cin>>sum;
    int i=0,j=size-1;
    int flag=0;
    while(i<j)
    {
        if(a[i]+a[j]==sum)
        {
            cout<<a[i]<<" "<<a[j];
            flag=1;
            break;
        }
        else if(a[i]+a[j]<sum)
        {
            i+=1;
        }
        else
        {
            j-=1;
        }
    }
    if(!flag)
    {
        cout<<-1<<endl;
    }
}