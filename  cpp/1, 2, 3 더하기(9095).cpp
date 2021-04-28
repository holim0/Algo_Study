#include<iostream>

using namespace std;
int T;
int dp[12];

int main(){

    cin>>T;
    dp[0]=1;
    dp[1]=1;

    dp[2]=dp[1]+dp[0];

    for (int i = 3; i <= 10; i++)
    {
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
    }
    
    int n;
    for (int i = 0; i < T; i++)
    {
        cin>>n;
        cout<<dp[n]<<endl;
        
    }
    
    
    


    return 0; 
}