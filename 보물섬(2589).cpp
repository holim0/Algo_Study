#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;

int N, M;
char map[55][55];
bool check[55][55]={false,};

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
int dist[55][55];

int maxpath=-10;



bool range(int x, int y){

    if(x>=0 && x<N && y>=0 && y<M) return true;
    else return false; 

}

void bfs(int x, int y){

    memset(check, false, sizeof(check));
    memset(dist, 0, sizeof(dist));
    queue<pair<int, int>> q;
    q.push({x, y});
    check[x][y]=true;
    int pathcnt=-1;

    while(!q.empty()){
        int curx=q.front().first;
        int cury=q.front().second;
        q.pop();


        for (int i = 0; i < 4; i++)
        {
            int nx=curx+dx[i]; int ny=cury+dy[i];
            if(!check[nx][ny] && map[nx][ny]=='L' && range(nx, ny)){
                check[nx][ny]=true;
                q.push({nx, ny});
                dist[nx][ny]=dist[curx][cury]+1;
                pathcnt=max(pathcnt, dist[nx][ny]);
            }

        }
        
        
        
    }

    maxpath=pathcnt>maxpath? pathcnt : maxpath;
}


int main(){

    cin>>N>>M;

    string s;

    for (int i = 0; i < N; i++)
    {
        cin>>s;
        for (int j = 0; j < M; j++)
        {
            map[i][j]=s[j];
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]=='L'){
                bfs(i, j);
            }
        }
        
    }

    cout<<maxpath<<endl;


    return 0;
}