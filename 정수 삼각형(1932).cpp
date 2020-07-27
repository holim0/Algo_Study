#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int N;

vector<int> v[502];

int dp[502][502];

int main(){

    cin>>N;

    int result=-10;

    for (int i = 1; i <= N; i++)
    {   
        int n;
        for(int j=0; j<i; j++){
            cin>>n;
            v[i].push_back(n);
        }
    }

    dp[1][0]=v[1][0];

    for(int i=2; i<=N; i++){
        for(int j=0; j<i; j++){
            if(j==0){
                dp[i][j]= v[i][j]+dp[i-1][j];
            }else if(j==i-1){
                dp[i][j]= v[i][j]+dp[i-1][j-1];
            }else{
                dp[i][j]=v[i][j]+max(dp[i-1][j], dp[i-1][j-1]);
            }
            
        }

    }

    
    for(int i=0; i<N; i++){
        result=max(result, dp[N][i]);
    }


    cout<<result<<endl;
    




    return 0;
}