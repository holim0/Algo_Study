#include<iostream>
#include<queue>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
#define MAX 1000

using namespace std;
int N, M;
int map[12][12];
bool check[12][12]={false, };

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

bool islandCheck[10]={false, };
bool mst[8]={false, };

int islandcnt=0;
int answer=0;
vector<pair<int, int>> island[8];    // 섬 좌표들 저장.
vector<pair<int, pair<int, int>>> connect;    //비용 연결.

bool range(int x, int y){
    
    if(x>=0 && x<N && y>=0 && y<M) return true;
    else return false;
}
int inum=1;  // 섬개수
void bfs(){

    queue<pair<int, int>> q;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if(map[i][j]==1 && !check[i][j]){
                q.push({i, j});
                check[i][j]=true;
                island[inum].push_back({i, j});
                while(!q.empty()){
                    int curx=q.front().first; int cury=q.front().second;
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k]; int ny=cury+dy[k];
                        if(!check[nx][ny] && map[nx][ny]==1 && range(nx, ny)){
                            island[inum].push_back({nx, ny});
                            check[nx][ny]=true;
                            q.push({nx, ny});
                        }
                    }
                    
                }
                inum++;
            }
        }
        
    }
    
}
bool checkgaroCorrupt(int x1, int y1, int x2, int y2){    // 중간에 장애물 있는지 판단.  가로로

    bool val= y1<y2;

    if(val){
        for(int i=y1+1; i<y2; i++){
            if(map[x1][i]==1) return false;
        }
    }else{
        for (int i = y2+1; i < y1; i++)
        {
            if(map[x1][i]==1) return false;
        }
    }

    return true;
}

bool checkseroCorrupt(int x1, int y1, int x2, int y2){

    bool val=x1<x2;

    if(val){
        for (int i = x1+1; i < x2; i++)
        {
            if(map[i][y1]==1) return false;
        }
        
    }else{
        for (int i = x2+1; i < x1; i++)
        {
            if(map[i][y1]==1) return false;
        }
        
    }

    return true;
}

void getPath(){     //섬 마다 최단거리 저장.

    int basex, basey;

    int dist;

    for (int i = 1; i < inum; i++)
    {   
        int minx=0 ,miny=0; 
        
        for (int j = i+1; j < inum; j++)
        {   
            int len=MAX;
            for (int k = 0; k < island[i].size(); k++)
            {
                basex=island[i][k].first; basey=island[i][k].second;
                
                for (int z = 0; z < island[j].size(); z++)
                {
                    if(basex==island[j][z].first){
                        if(checkgaroCorrupt(basex, basey, island[j][z].first, island[j][z].second)){
                            dist=abs(basey-island[j][z].second)-1;
                            if(dist>=2){
                                len= min(len, dist);
                            }
                            
                        }
                        

                    }else if(basey==island[j][z].second){
                        //cout<<"i j: "<<i<<j<<" "<<basex<<basey<<" "<<island[j][z].first<<island[j][z].second<<endl;
                        if(checkseroCorrupt(basex, basey, island[j][z].first, island[j][z].second)){
                            dist=abs(basex-island[j][z].first)-1;
                            if(dist>=2){
                                len= min(len, dist);
                            }
                            
                        }
                        
                    }
                }
                
            }
            if(len==MAX){
                continue;
            }
            connect.push_back({len, {i, j}});
            
        }
        
    }
    
}

bool checkallTrue(){

    for (int i = 1; i < inum; i++)
    {
        if(!mst[i]) return false;
    }
    

    return true;
    
}

void sol(){

    mst[1]=true;

    while(checkallTrue()!=true){
        for(int i=0; i<connect.size(); i++){
            int n1=connect[i].second.first;
            int n2=connect[i].second.second;
            int val=connect[i].first;
            if(mst[n1] || mst[n2]){
                if(mst[n1] && mst[n2]){
                    continue;
                }
                else{
                    mst[n1]=true; mst[n2]=true;
                    answer+=val;
                    break;
                }
            }
        }
    }
}

bool checkNetwork(){      /// 연결이 잘 돼 있는지 파악하기 위해서 bfs 한 번 더 사용.
    queue<int> q1;

    int list[10][10]={0, };
    bool check[10]={false, };

    for (int i = 0; i < connect.size(); i++)
    {
        int x=connect[i].second.first; int y=connect[i].second.second;
        list[x][y]=1; list[y][x]=1;
    }

    check[1]=true;
    q1.push(1);
    
    while(!q1.empty()){
        int cur=q1.front();
        q1.pop();
        for(int i=1; i<inum; i++){
            if(!check[i] && list[cur][i]==1){
                check[i]=true;
                q1.push(i);
            }
        }
    }
    
    
    for(int i=1; i<inum; i++){
        if(check[i]==false) return false;
    }
    
    return true;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
        }
        
    }
    
    bfs();
    getPath();
    
    if(checkNetwork()){
        sort(connect.begin(), connect.end());
        sol();
    }
    else{
        cout<<-1<<endl;
        return 0;
    }

    
    
    
        cout<<answer<<endl;
    

    return 0;
}