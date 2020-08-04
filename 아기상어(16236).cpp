#include<iostream>
#include<queue>
#include<cstring>
#include<algorithm>

using namespace std;
int map[25][25];
int N;
int timeVal=0;
int fishSize=2;
bool check[25][25]={false, };
int dx[]={1, -1, 0,0};
int dy[]={0,0, -1, 1};

queue<pair<pair<int, int>, int>> q;
vector<pair<pair<int, int>, int>> v;

bool range(int x, int y){
    if(x>=0 && x<N && y>=0 && y<N) return true;
    
    return false;
}

bool checkAll(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(map[i][j]!=0 && map[i][j]!=9) return false;
        }
        
    }

    return true;
    
}


bool sortFunc(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b){

    if(a.second==b.second){
        if(a.first.first==b.first.first) {
            return a.first.second<b.first.second;
        }
        return a.first.first<b.first.first;
    }

    return a.second<b.second;
}


void getSol(int x, int y, int eatcnt){

    if(checkAll()){
        cout<<timeVal<<endl;
        return;
    }

    v.clear();
    if(eatcnt==fishSize){
        fishSize++;
        eatcnt=0;
    }
    memset(check, false, sizeof(check));
    check[x][y]=true;
    q.push({{x, y}, 0});

    while(!q.empty()){
        int curx=q.front().first.first; int cury=q.front().first.second;
        int dist=q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx=curx+dx[i]; int ny=cury+dy[i];
            if(!check[nx][ny] && map[nx][ny]<=fishSize && range(nx, ny)){
                check[nx][ny]=true;
                q.push({{nx, ny}, dist+1});
                if(map[nx][ny]<fishSize && map[nx][ny]!=0){
                    v.push_back({{nx, ny}, dist+1});
                }
            }
        }
    }

    if(v.size()==0){
        cout<<timeVal<<endl;
        return;
    }

    sort(v.begin(), v.end(), sortFunc);

    int nextx=v[0].first.first; int nexty=v[0].first.second;
    timeVal+=v[0].second;
    map[x][y]=0;
    map[nextx][nexty]=9;
    getSol(nextx, nexty, eatcnt+1);


    
}

int main(){

    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);


    cin>>N;
    int sx, sy;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
            if(map[i][j]==9){
                sx=i; sy=j;
            }
        }
    }
    


    getSol(sx, sy, 0);


    return 0;
}