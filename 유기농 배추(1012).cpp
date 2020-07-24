#include<iostream>
#include<queue>
#include<cstring>


using namespace std;
int result=0;

int T;
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

int map[53][53];
bool check[53][53]={false, };
queue<pair<int, int>> q;
int M, N, K;

void getSol(){


    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(!check[i][j] && map[i][j]==1){
                q.push({i, j});
                check[i][j]=true;
                while(!q.empty()){
                    int curx=q.front().first; int cury=q.front().second;
                    q.pop();

                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k]; int ny=cury+dy[k];
                        if(nx>=0 && nx<M && ny>=0 && ny<N && !check[nx][ny] && map[nx][ny]==1){
                            check[nx][ny]=true;
                            q.push({nx, ny});
                        }
                    }
                }
                result++;
            }
        }
        
    }
    





}



int main(){

    cin>>T;
    int x, y;

    for(int t=0; t<T; t++){
        cin>>M>>N>>K;
        result=0; 
        memset(check, false, sizeof(check));
        memset(map, 0, sizeof(map));
        for (int i = 0; i < K; i++)
        {
            cin>>x>>y;
            map[x][y]=1;
        }
        getSol();
        cout<<result<<endl;
    }    


    return 0;
}