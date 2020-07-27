#include<iostream>
#define Mod 10007

using namespace std;
int dp[1001]={0, 1, 2, };
int main(){


    int n;
    cin>>n;

    for (int i = 3; i <=n; i++)            // 전에꺼에 가로 1더하는 경우와 전전꺼에서 가로 2짜리 2개 더하는 경우를 생각하면 된다. 
    {
        dp[i]=(dp[i-1]+dp[i-2])%Mod;
    }
    
    cout<<dp[n]%Mod<<endl;
    return 0;
}