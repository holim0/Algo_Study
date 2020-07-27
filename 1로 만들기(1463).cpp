#include<iostream>
#include<algorithm>
#define MAX 1000005

using namespace std;
int dp[MAX]={0, 0, };
int N;
int main(){

    cin>>N;

    for (int i = 2; i <=N; i++)
    {
        dp[i]=dp[i-1]+1;      //일단 -1 빼는 경우 더해주고 
 
        if(i%2==0){         // 2로 나눠지면 1뺀 최소랑, 나누기 2한거 최소 중 최소 구함
            dp[i]=min(dp[i], dp[i/2]+1);
        }
  
        if(i%3 ==0){        //2나누는거랑 똑같음
			dp[i] = min(dp[i], dp[i / 3]+1);
		}
    }
    

    cout<<dp[N]<<endl;
    return 0;
}