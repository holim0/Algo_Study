#include<iostream>
#include<queue>
#include<cstring>

using namespace std;
int N, M;
int map[505][505];
bool check[505][505]={false, };
int result=-1;
int dx[]={-1, 1, 0, 0};
int dy[]={0, 0, -1, 1};

bool range(int x, int y){
    if(x>=0 && x<N && y>=0 && y<M) return true;
    else return false;
}

void dfs(int x, int y, int cnt , int num){

    if(cnt==3){
        result= num> result ? num : result;
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        int nx=x+dx[i]; int ny=y+dy[i];

        if(!check[nx][ny] && range(nx, ny)){
            check[nx][ny]=true;
            dfs(nx, ny, cnt+1, num+map[nx][ny]);
            check[nx][ny]=false;
        }
    }

}

void bfs(int x, int y){

    
    queue<pair<int, int>> q;
    int sum=0;
    sum+=map[x][y];
    for (int i = 0; i < 4; i++)
    {
        int nx=x+dx[i]; int ny=y+dy[i];
        if(range(nx, ny)){
            q.push({nx, ny});
        }
    }

    if(q.size()<3){
        return;
    }
    else if(q.size()==3){
        while(!q.empty()){
            int cx=q.front().first; int cy=q.front().second;
            sum+=map[cx][cy];
            q.pop();
        }
        result= sum > result ? sum : result;
    }else{
        int minv=map[q.front().first][q.front().second];
        while(!q.empty()){
            int cx=q.front().first; int cy=q.front().second;
            sum+=map[cx][cy];
            minv= minv > map[cx][cy] ? map[cx][cy] : minv;
            q.pop();
        }
        sum-=minv;
        result= sum > result ? sum : result;
    }

    
    
    

}

int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {   
            check[i][j]=true;
            dfs(i, j, 0, map[i][j]);
            check[i][j]=false;
        }
    }
    
    memset(check, false, sizeof(check));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            bfs(i, j);
        }
        
    }
    
    cout<<result<<endl;
    


    return 0;
}