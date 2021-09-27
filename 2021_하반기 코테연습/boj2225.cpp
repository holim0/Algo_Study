#include<iostream>
#include<cstdlib>
#define MOD 1000000000

using namespace std;


long long dp[202][202]= {0, };

int main(){

    int n, K;
    
    cin>>n>>K;

    for(int i=0; i<=K; i++){
        dp[0][i] = 1;
    }
    for(int i=0; i<=n; i++){
        dp[i][1] = 1;
    }

    for(int k=2; k<=K; k++){
        for(int i=1; i<=n; i++){
            for(int j=0; j<=i; j++){
                
                dp[i][k] += dp[i-j][k-1];
            }
            dp[i][k]%=MOD;
        }
        
    }
    


    cout<<dp[n][K]%MOD<<endl;

    return 0;
}