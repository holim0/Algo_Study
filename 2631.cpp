#include<iostream>
#include<algorithm>
using namespace std;
int N;

int num[205];
int dp[205];
int result = -1;
int main(){

    cin>>N;

    for (int i = 1; i <= N; i++)
    {
        cin>>num[i];
    }

    dp[1]=1;

    result=max(result, dp[1]);

    for (int i = 2; i <=N; i++)
    {
        for (int j = i-1; j>=1; j--)
        {
            if(num[i]>num[j]){
                dp[i]=max(dp[j]+1, dp[i]);
            }
        }
        if(dp[i]==0){
            dp[i]=1;
        }
        result=max(result, dp[i]);
        
    }
    
    cout<<N-result<<endl; 

    return 0;
}