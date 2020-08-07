#include<iostream>
#include<vector>
using namespace std;
int N, M;
int parent[205];
bool check[205]={false, };
int find(int x){

    if(x==parent[x]){
        return x;
    }
    else{
        return parent[x]=find(parent[x]);
    }
}

void uni(int x, int y){

    x= find(x);
    y= find(y);

    parent[y]=x;
}

int main(){

    cin>>N>>M;
    int val;
    for (int i = 1; i <=N; i++)
    {
        parent[i]=i;
    }
    
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {   
            cin>>val;
            if((!check[i] || !check[j]) && val==1){
                check[i]=true; check[i]=true;
                uni(i, j);
            }else{
                continue;
            }
        }
        
    }
    vector<int> v;
    for (int i = 0; i < M; i++)
    {
        int n; cin>>n;
        v.push_back(n);
    }

    for (int i = 0; i < v.size()-1; i++)
    {
        int x=find(v[i]);
        int y=find(v[i+1]);
        if(x!=y){
            cout<<"NO"<<endl;
            return 0;
        }
    }
    
    
    cout<<"YES"<<endl;


    return 0;
}