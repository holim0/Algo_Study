#include<iostream>
#include<vector>
#include<cstring>

using namespace std;
int N, M, x, y, k;
int map[25][25];
int dx[]={0, 0, 0, -1, 1};  //동 서 북 남.
int dy[]={0, 1, -1, 0, 0};
int cur=1;
int cube[7]={0, };
int adj[5];
bool check[7]={false, };


bool range(int nx, int ny){
    if(nx>=0 && nx<N && ny>=0 && ny<M) return true;
    else return false;
}

bool chkCube(int cx, int cy){

    if(cx>=0 && cx<N && cy>=0 && cy<M) return true;
    else return false;
}
int reverse(int n){
    if(n==1) return 2;
    if(n==2) return 1;
    if(n==3) return 4;
    if(n==4) return 3;
    
    return 0;
}

void cubeMove(int dir){
    memset(check, false, sizeof(check));

    check[cur]=true;
    for (int i = 1; i <= 4; i++)
    {
        check[adj[i]]=true;
    }
    
    int tmp=cur;
    cur=adj[dir];
    adj[reverse(dir)]=tmp;

    for (int i = 1; i <= 6; i++)
    {
        if(!check[i]){
            adj[dir]=i;
        }
    }
    
}

void move(int dir){

    int nx=x+dx[dir]; int ny=y+dy[dir];

    if(!range(nx, ny)) return;
    x=nx; y=ny;
    cubeMove(dir);

    if(map[nx][ny]==0){
        map[nx][ny]=cube[cur];
    }else{
        cube[cur]=map[nx][ny];
        map[nx][ny]=0;
    }

    
    for (int i = 1; i  <= 6; i++)
    {   bool flag=false;
        for (int j = 1; j <=4; j++)
        {
            if(i==adj[j]) {
                flag=true;
                break;
            }
        }
        if(!flag && i!=cur){
            cout<<cube[i]<<endl;
        }
    }
    

}


int main(){

    cin>>N>>M>>x>>y>>k;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            int n; cin>>n;
            map[i][j]=n;
        }
    }
    adj[1]=3;
    adj[2]=4;
    adj[3]=2;
    adj[4]=5;

    int order;

    for (int i = 0; i < k; i++)
    {
        cin>>order;
        move(order);
    }
    



    return 0;
}