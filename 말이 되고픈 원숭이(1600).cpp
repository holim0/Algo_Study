#include<iostream>
#include<queue>
#include<cmath>
#define MAX 987654321
using namespace std;

int dx[]={1, -1, 0, 0,    -2, -1, -2, -1, 1, 2, 1, 2};
int dy[]={0, 0, -1, 1,    1, 2, -1, -2, 2, 1, -2, -1};

queue<pair<pair<int, int>, pair<int, int>>> q;

int K, W,H;

int map[205][205];
bool check[205][205][35]={false, };
int result=MAX;


bool range(int x, int y){

    if(x>=0 && x<H && y>=0 && y<W) return true;
    else return false;
}

void go(int x, int y, int cnt, int malcnt){

    q.push({{x, y}, {cnt, malcnt}});
    check[0][0][0]=true;

    while(!q.empty()){
        int curx=q.front().first.first;
        int cury=q.front().first.second;
        int count=q.front().second.first;
        int mal=q.front().second.second;
        q.pop();

        if(curx==H-1 && cury==W-1){
            result=count;
            break;
        }

        for (int i = 0; i < 12; i++)
        {
            int nx=curx+dx[i]; int ny=cury+dy[i];
            if(abs(dx[i])==2 || abs(dy[i])==2){
                if(range(nx, ny) && map[nx][ny]!=1 && !check[nx][ny][mal+1] && mal<K){
                    check[nx][ny][mal+1]=true;
                    q.push({{nx, ny}, {count+1, mal+1}});
                }
            }
            else{
                if(range(nx, ny) && map[nx][ny]!=1 && !check[nx][ny][mal]){
                    check[nx][ny][mal]=true;
                    q.push({{nx, ny}, {count+1, mal}});
                } 
            }
        }
        



    }
    
    
}

int main(){

    ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);

    cin>>K>>W>>H;

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            cin>>map[i][j];
        }
        
    }
    
    go(0, 0, 0, 0);

    if(result==MAX){
        cout<<-1<<endl;
        return 0;
    }
    cout<<result<<endl;

    return 0;
}