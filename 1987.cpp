#include<iostream>

using namespace std;

int R, C;
char map[25][25];
bool check[100]={false, };

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

int result=-1;
bool range(int x, int y){
    
    if(x>=0 && x<R && y>=0 && y<C) return true;
    else return false;
}


bool dontGo(int x, int y){

    for (int i = 0; i < 4; i++)
    {
        int nx=x+dx[i];
        int ny=y+dy[i];
        
        if(!check[map[nx][ny]] && range(nx, ny)) return false;
    }
    
    return true;

}

void dfs(int cx, int cy, int num){

    
    if(dontGo(cx, cy)){
        result= num > result ? num : result;
        return;
    }


    for (int i = 0; i < 4; i++)
    {
        int nx=cx+dx[i];
        int ny=cy+dy[i];
        
        if(!check[map[nx][ny]] && range(nx, ny)){
            check[map[nx][ny]]=true;
            dfs(nx, ny, num+1);
            check[map[nx][ny]]=false;
        }
    }
    

}


int main(){


    cin>>R>>C;

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin>>map[i][j];
        }
    }
    
    check[map[0][0]]=true;
    dfs(0, 0, 1);


    cout<<result<<endl;
    return 0;
}