#include<iostream>

using namespace std; 
int T, N, M;

int go(int n, int m){
    int dp[35][35];

    for (int i = 1; i <=M; i++)
    {
        dp[i][i]=1;
        dp[i][1]=i;
    }

    for (int i = 2; i <= M; i++)
    {
        for (int j = 1; j <=i; j++)
        {
            if(j==1 || j==i) continue;
            else
            {
                dp[i][j]=(dp[i][j-1]*dp[i-j+1][1])/j;
            }
            
        } 
    }
    
    
    return dp[m][n];

}
int main(){

    cin>>T;
    

    for (int i = 0; i < T; i++)
    {
        cin>>N>>M;
        cout<<go(N, M)<<endl;

    }
    

    return 0;
}