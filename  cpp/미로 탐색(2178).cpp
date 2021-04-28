#include<iostream>
#include<queue>
#include<string>
using namespace std;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

int N, M;
int map[105][105];
int result;

bool check[105][105]={false, };
queue<pair<pair<int, int>, int>> q;

bool range(int x, int y){


    if(x>=0 && x<N && y>=0 && y<M) return true;
    else return false;

}
void go(int x, int y){

    q.push({{x, y}, 0});
    check[x][y]=true;

    while(!q.empty()){
        int curx=q.front().first.first;
        int cury=q.front().first.second;
        int cnt=q.front().second;
        q.pop();

        if(curx==N-1 && cury==M-1){
            result=cnt;
            break;
        }

        for (int i = 0; i < 4; i++)
        {
            int nx=curx+dx[i]; int ny=cury+dy[i];

            if(!check[nx][ny] && map[nx][ny]!=0 && range(nx, ny)){
                q.push({{nx, ny}, cnt+1});
                check[nx][ny]=true;
            }

        }

    }

}
int main(){

    cin>>N>>M;
    string s;
    for (int i = 0; i < N; i++)
    {
        cin>>s;
        for (int j = 0; j< M; j++)
        {
            map[i][j]=s[j]-'0';
        }
        
    }

    go(0, 0);
    

    cout<<result+1<<endl;

    return 0;
}