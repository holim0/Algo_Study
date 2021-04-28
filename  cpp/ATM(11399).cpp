#include<iostream>
#include<algorithm>

using namespace std;
int arr[1005];

int n;
int main(){

    cin>>n;
    int sum=0;

    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }

    sort(arr, arr+n);

    for (int i = 1; i < n; i++)
    {
        arr[i]+=arr[i-1];
    }

    for (int i = 0; i < n; i++)
    {
        sum+=arr[i];
    }
    
    
    cout<<sum<<endl;



    return 0;
}