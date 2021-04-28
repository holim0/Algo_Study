#include<iostream>
#include<cstring>

using namespace std;
int N, M, K;

int dx[]={1, 0};
int dy[]={0, 1};
int map[17][17];
int r1=0;
int r2=0;

bool check[20][20]={false, };

bool range(int x, int y){
    if(x>=1 && x<=N && y>=1 && y<=M) return true;
    else return false;
}


void dfs(int x, int y, int tx, int ty){

    if(x==tx && y==ty){
        if(tx==N && ty==M){
            r2++;
        }else{
            r1++;
        }
        return;
    }

    for (int i = 0; i < 2; i++)
    {
        int nx=x+dx[i]; int ny=y+dy[i];

        if(!check[nx][ny] && range(nx, ny)){
            check[nx][ny]=true;
            dfs(nx, ny, tx, ty);
            check[nx][ny]=false;
        }
    }
    
    

}
int main(){

    cin>>N>>M>>K;
    int n=1;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            map[i][j]=n;
            n++;
        }
    }
    int tx, ty;

    if(K==0){
        dfs(1, 1, N, M);
        cout<<r2<<endl;

    }else{
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= M; j++)
            {
                if(map[i][j]==K){
                    tx=i; 
                    ty=j;
                    break;
                }
                
            }
        }
        check[1][1]=true;
        dfs(1, 1, tx, ty);
        memset(check, false, sizeof(check));
        check[tx][ty]=true;
        dfs(tx, ty, N, M);

        cout<<r1*r2<<endl;
    }

    return 0;
}