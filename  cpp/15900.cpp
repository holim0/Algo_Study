#include<iostream>
#include<vector>
#include<cstring>
#include<queue>
#define MAX 500000+1
using namespace std;

int N;

vector<int> list[MAX];
int len=0;


bool check[MAX]={false, };

void dfs(int cur, int cnt){

    if(cur!=1 && list[cur].size()==1){
        len+=cnt;
        return;
    }

    for (int i = 0; i < list[cur].size(); i++)
    {
        int next=list[cur][i];

        if(!check[next]){
            check[next]=true;
            dfs(next, cnt+1);
        }
    }
    
    
    
}

int main(){

    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>N;
    int a, b;
    for (int i = 0; i < N-1; i++)
    {
        cin>>a>>b;
        list[a].push_back(b);
        list[b].push_back(a);
    }

    

    dfs(1, 0);

    if(len%2==0){
        cout<<"No";
    }else{
        cout<<"Yes";
    }

    return 0;
}