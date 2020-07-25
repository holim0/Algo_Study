#include<iostream>
#include<queue>


using namespace std;

int cnt=0;
int N, P;
int map[105][105];
bool check[105]={false, };
queue<int> q;
int main(){

    cin>>N>>P;
    int x, y;
    for (int i = 0; i < P; i++)
    {
        cin>>x>>y;
        map[x][y]=1; 
        map[y][x]=1;
    }

    q.push(1);
    check[1]=true;

    while(!q.empty()){
        int cur=q.front();
        q.pop();

        for(int i=1; i<=N; i++){
            if(!check[i] && map[cur][i]==1){
                check[i]=true;
                q.push(i);
                cnt++;
            }
        }

    }

    
    cout<<cnt<<endl;

    return 0;
}