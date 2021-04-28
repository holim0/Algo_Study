#include<iostream>
#include<algorithm>


using namespace std;

int n;
int dp[10005][3];
int num[10005];
int result=-1;
int main(){

    cin>>n;
    
    for (int i = 1; i <= n; i++)
    {
        cin>>num[i];
    }

    for(int i=1; i<=n; i++){
        for (int j = 0; j < 3; j++)
        {
            dp[i][j]=0;
        }
        
    }

    dp[1][1]=num[1];
    dp[1][2]=0;

    dp[2][1]=num[2];
    dp[2][2]=num[2]+dp[1][1];


    for(int i=3; i<=n; i++){
        int val=-1;
        for(int j=1; j<=i-2; j++){
            val=max(val, max(dp[j][1], dp[j][2]));
        }

        dp[i][1]=num[i]+val;
        dp[i][2]=dp[i-1][1]+num[i];
        
        

    }

    for (int i = 1; i <=n; i++)
    {
        result=max(result, max(dp[i][1], dp[i][2]));
    }
    

    
    cout<<result<<endl;

    return 0;
}