#include<iostream>
#define Mod 10007

using namespace std;

int N;

long long dp[10][1001];  // i로 시작하는 길이 j인 오르막 수의 개수.

int main(){

    cin>>N;

    for(int i=0; i<10; i++){
        dp[i][1]=1;
    }

    for(int len=2; len<=N; len++){

        for(int i=0; i<10; i++){
            for(int j=i; j<10; j++){
                dp[i][len]+=dp[j][len-1];
                dp[i][len]%=Mod;
            }
        }
    }

    long long sum=0;

    for(int i=0; i<10; i++){
        sum+=dp[i][N];
    }

    cout<<sum%Mod<<endl;
    return 0;
}