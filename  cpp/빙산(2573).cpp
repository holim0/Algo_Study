#include<iostream>
#include<queue>

using namespace std;
int N, M;
int map[305][305];
int dx[]={1, -1, 0, 0};
int dy[]={0, 0,-1, 1};

bool range(int x, int y);

bool checkAll(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]!=0) return false;
        }
        
    }

    return true;
    
}

bool checkTwo(){
    bool tmp[305][305]={false, };
    int cnt=0;
    queue<pair<int, int>>q;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]!=0 && !tmp[i][j]){
                tmp[i][j]=true;
                q.push({i, j});
                while(!q.empty()){
                    int curx= q.front().first; int cury=q.front().second;
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k];  int ny=cury+dy[k];
                        if(!tmp[nx][ny] && map[nx][ny]!=0 && range(nx, ny)){
                            tmp[nx][ny]=true;
                            q.push({nx, ny});
                        }
                    }
                }
                cnt++; 
            }
        }
        
    }


    return cnt>=2;
}

bool range(int x, int y){
    
    if(x>=0 && x<N && y>=0 && y<M) return true;
    else return false;
}

void go(){

    bool check[305][305]={false, };
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]!=0){
                for (int k = 0; k < 4; k++)
                {
                    int nx=i+dx[k]; int ny=j+dy[k];
                    if(range(nx, ny) && map[nx][ny]==0 && !check[nx][ny]){
                        map[i][j]--;
                        if(map[i][j]<=0){
                            map[i][j]=0;
                            check[i][j]=true;
                            break;
                        }
                    }
                }
                

            }
        }
        
    }
    // cout<<endl;
    // for (int i = 0; i < N; i++)
    // {
    //     for (int j = 0; j < M; j++)
    //     {
    //         cout<<map[i][j]<<" ";
    //     }
    //     cout<<endl;
        
    // }
    


}

int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j< M; j++)
        {
            cin>>map[i][j];
        }
        
    }


    int num=0;
    while(1){
        go();
        if(checkAll()){
            cout<<0<<endl;
            return 0;
        }
        num++;
        if(checkTwo()) break;
    }
    
    cout<<num<<endl;

    return 0;
}