#include<iostream>
#define Mod 10007

using namespace std;
int dp[1001]={0, 1, 3,};
int main(){

    int n;

    cin>>n;


    for (int i = 3; i <=n; i++)
    {
        dp[i]=(dp[i-1]+2*dp[i-2])%Mod;
    }
    
    cout<<dp[n]%Mod<<endl;

    return 0;
}
