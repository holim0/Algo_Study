#include<iostream>
#include<queue>
#include<cstring>
#include<vector>
#define MAX 1000000+5

using namespace std;

int n, m;
int parent[MAX];

int find(int x){

    if(x==parent[x]){
        return x;
    }else{
        int p=find(parent[x]);
        parent[x]=p;
        return p;
    }
}

void Union(int x, int y){

    x = find(x);
    y = find(y);

    
    parent[y] = x;
    
}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>n>>m;

    int a, b, c;

    for (int i = 0; i <= n; i++)
    {
        parent[i]=i;
    }
    
    
    for (int i = 0; i < m; i++)
    {
        cin>>a>>b>>c;
        if(a==0){
            Union(b, c);
        }else{
            int val1= find(b);
            int val2= find(c);

            if(val1==val2){
                cout<<"yes"<<'\n';
            }else{
                cout<<"no"<<'\n';
            }
        }
        
    }
    

    return 0;

}