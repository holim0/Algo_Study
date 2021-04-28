#include<iostream>
#include<algorithm>

using namespace std;
int n;
int num[1005];
int dp[1005]={0, };
int main(){

    cin>>n;

    for (int i = 1; i <=n; i++)
    {
        cin>>num[i];
        dp[i]=num[i];
    }

    for (int i = 2; i <=n; i++)
    {
        for(int j=1; j<i; j++){
            dp[i]=max(dp[i], dp[j]+dp[i-j]);
        }
        dp[i]=max(dp[i], i*dp[1]);
    }
    
    cout<<dp[n]<<endl;



    return 0;
}