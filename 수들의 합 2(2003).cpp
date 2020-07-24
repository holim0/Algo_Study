#include<iostream>
#include<vector>


using namespace std;
int N, M;
int result=0;

long long arr[10005];


    

    
    
int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        cin>>arr[i];
    }


    

    for (int i = 0; i < N; i++)
    {   
        long long val=arr[i];

        if(val==M) result++;
        for (int j = i+1; j < N; j++)
        {
            val+=arr[j];
            if(val==M) result++;
        }
        
    }

    cout<<result<<endl;

    return 0;
}