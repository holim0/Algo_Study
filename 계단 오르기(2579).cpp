#include<iostream>
#include<algorithm>


using namespace std; 
int n;
int num[305];
int dp[305][3];
int main(){

    cin>>n;

    for (int i = 1; i <= n; i++)
    {
        cin>>num[i];
    }
    dp[0][1]=0; dp[0][2]=0;
    dp[1][1]=num[1];
    dp[1][2]=0;

    for (int i = 2; i <=n; i++)
    {
        dp[i][1]=num[i]+max(dp[i-2][1], dp[i-2][2]);

        dp[i][2]=num[i]+dp[i-1][1];
    }
    
    

    cout<<max(dp[n][1], dp[n][2])<<endl;
    

    
    
    return 0;

}