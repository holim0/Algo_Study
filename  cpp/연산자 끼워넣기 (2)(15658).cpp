#include<iostream>
#include<vector>
#include<string>
#include<climits>
#include<algorithm>

using namespace std;

int N;
int num[15];
int copynum[15];
vector<char> v;

int oper[4];

bool check[20]={false, };

int minval=INT32_MAX;
int maxval=INT32_MIN;




void go(int plus, int minus, int mul, int div, int cnt, int sum){

    if(cnt==N){
        minval=min(minval, sum);
        maxval=max(maxval, sum);
        return;

    }

    if(plus>0){
        go(plus-1, minus, mul, div, cnt+1, sum+num[cnt]);
    }
    if(minus>0){
        go(plus, minus-1, mul, div, cnt+1, sum-num[cnt]);
    }
    if(mul>0){
        go(plus, minus, mul-1, div, cnt+1, sum*num[cnt]);
    }
    if(div>0){
        go(plus, minus, mul, div-1, cnt+1, sum/num[cnt]);
    }

    
    
}

int main(){

    cin>>N;

    for (int i = 0; i < N; i++)
    {
        cin>>num[i];
    }


    for (int i = 0; i < 4; i++)
    {
        cin>>oper[i];
    }
    
    
        
    
    go(oper[0], oper[1], oper[2], oper[3], 1, num[0]);


    cout<<maxval<<'\n'<<minval<<endl;

    return 0;
}