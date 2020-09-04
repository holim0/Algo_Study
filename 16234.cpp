#include<iostream>
#include<queue>
#include<cmath>

using namespace std;


int N, L, R;
int map[52][52];

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
int result=0;
bool mapCheck[52][52];
bool IsMove=false;

void reset(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            mapCheck[i][j]=false;
        }
    }

    IsMove=false;
    

}

bool range(int x, int y){
    
    if(x>=0 && x<N && y>=0 && y<N) return true;
    else return false;
}

bool check(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < 4; k++)
            {   
                int nx=i+dx[k]; int ny=j+dy[k];
                if(range(nx, ny)){
                    if(abs(map[i][j]-map[nx][ny])>=L && abs(map[i][j]-map[nx][ny])<=R) return true;
                }
            }
            
        }
        
    }
    

    return false;
}


void bfs(int x, int y){

    queue<pair<int, int>> q;
    queue<pair<int, int>> tmp;

    q.push({x, y});
    tmp.push({x, y});
    int cnt=1;
    int sum=map[x][y];
    mapCheck[x][y]=true;

    

    while(!q.empty()){
        int cx=q.front().first;
        int cy=q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx=cx+dx[i]; int ny = cy+dy[i];

            if(range(nx, ny) && !mapCheck[nx][ny]){
                if(abs(map[cx][cy]-map[nx][ny])>=L && abs(map[cx][cy]-map[nx][ny])<=R){
                    IsMove=true;
                    mapCheck[nx][ny]=true;
                    cnt++;
                    sum+=map[nx][ny];
                    q.push({nx, ny});
                    tmp.push({nx, ny});
                }
            }
        }
    }

    if(IsMove){
        int number=sum/cnt;
        while(!tmp.empty()){
            int cx=tmp.front().first;
            int cy=tmp.front().second;
            tmp.pop();  
            map[cx][cy]=number;
        }


        
    }

    
    
    
}


int main(){

    cin>>N>>L>>R;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
        }
    }


    while(check()){

        reset();
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if(!mapCheck[i][j]) bfs(i, j);
                
            }
        }

        if(IsMove){
            result++;
        }
    }
    

    cout<<result<<endl;
    return 0;
}