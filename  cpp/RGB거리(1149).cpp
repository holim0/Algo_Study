#include<iostream>
#define MAX 987654321

using namespace std;
int map[1005][4];
int N;
int dp[1005][4];
int main(){
    int result=MAX;
    cin>>N;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <=3; j++)
        {
            cin>>map[i][j];
        }
    }

    dp[1][1]=map[1][1];  //red
    dp[1][2]=map[1][2]; // green
    dp[1][3]=map[1][3];  // blue

    for(int zip=2; zip<=N; zip++){
        
        dp[zip][1]=map[zip][1]+min(dp[zip-1][2],dp[zip-1][3]);
    
        dp[zip][2]=map[zip][2]+min(dp[zip-1][1],dp[zip-1][3]);

        dp[zip][3]=map[zip][3]+min(dp[zip-1][1],dp[zip-1][2]);
            
    }
    
    for(int i=1; i<=3; i++){
        result=min(result, dp[N][i]);
    }

    cout<<result<<endl;

    return 0;
}