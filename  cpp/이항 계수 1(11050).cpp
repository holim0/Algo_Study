#include<iostream>
#include<vector>

using namespace std;
int N, K;

int num[11];
bool check[11]={false, };
int result=0;

void go(int start, int cnt){
    
    if(cnt==K){
        result++;
        return;
    }

    for(int i=start; i<=N; i++){
        
        if(!check[i]){
            check[i]=true;
            go(i, cnt+1);
            check[i]=false;
        }
        
    }

}

int main(){


    cin>>N>>K;

    for(int i=1; i<=N; i++){
        num[i]=i;
    }

    go(1, 0);

    cout<<result<<endl;

    return 0;
}