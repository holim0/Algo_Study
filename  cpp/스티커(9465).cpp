#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;
int T;  
int num[2][100005];
int dp[2][100005];
int n;

int sol(){

    int result;
    
    memset(dp, 0, sizeof(dp));

    dp[0][0]=num[0][0];
    dp[1][0]=num[1][0];
    dp[0][1]=num[0][1]+dp[1][0];
    dp[1][1]=num[1][1]+dp[0][0];

    for(int i=2; i<n; i++){
        
        dp[0][i]=num[0][i]+max(max(dp[1][i-1], dp[1][i-2]), dp[0][i-2]);
        dp[1][i]=num[1][i]+max(max(dp[0][i-1], dp[0][i-2]), dp[1][i-2]);
        
    }

    result=max(dp[0][n-1], dp[1][n-1]);

    return result;
}

int main(){

    cin>>T;
    
    for (int i = 0; i < T; i++)
    {
        cin>>n; memset(num, 0, sizeof(num));
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin>>num[i][j];
            }
            
        }

        cout<<sol()<<endl;
        
    }
    
    return 0;
}