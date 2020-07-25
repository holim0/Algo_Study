#include<iostream>
#include<queue>
using namespace std;

int N, K;

queue<pair<int, int>> q;

bool check[100005]={false, };
int result;
int main(){


    cin>>N>>K;

    q.push({N, 0});
    check[N]=true;

    while(!q.empty()){
        int cur=q.front().first;
        int cnt=q.front().second;
        q.pop();
        if(cur==K){
            result=cnt;
            break;
        }

        if(cur-1>=0 && !check[cur-1]){
            check[cur-1]=true;
            q.push({cur-1, cnt+1});
        }

        if(cur+1<=100000 && !check[cur+1]){
            check[cur+1]=true;
            q.push({cur+1, cnt+1});
        }
        
        if(2*cur<=100000 && !check[2*cur]){
            check[2*cur]=true;
            q.push({2*cur, cnt+1});
        }

    }

    cout<<result<<endl;


    return 0;
}