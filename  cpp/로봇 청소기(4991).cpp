///////bfs로 각각 최소거리 구한뒤에 dfs로 모든 조합 따져서 구하면 된다.


#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#define MAX 987654321

using namespace std;
int w, h;
char map[25][25];
int result=MAX;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

vector<pair<int, int>> v[12];
vector<pair<int, int>> node;


bool checknode[12]={false, };

bool IsCleanAll(){

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {   
            
            if(map[i][j]=='*') return false;
        }
        
    }
    return true;
    
}

bool range(int x, int y){

    if(x>=0 && x<h && y>=0 && y<w) return true;
    else return false;
}

int getSol(int sx, int sy, int tx, int ty){

    int ans=-1;

    bool check[25][25]={false, };
    queue<pair<pair<int, int>, int>> q;

    check[sx][sy]=true;
    q.push({{sx, sy}, 0});

    while(!q.empty()){
        int curx=q.front().first.first;
        int cury=q.front().first.second;
        int cnt=q.front().second;
        q.pop();

        if(curx==tx && cury==ty){
            ans=cnt;
            break;
        }

        for (int i = 0; i < 4; i++)
        {
            int nx=curx+dx[i]; int ny=cury+dy[i];
            
            if(!check[nx][ny] && range(nx, ny) && map[nx][ny]!='x'){
                check[nx][ny]=true;
                q.push({{nx, ny}, cnt+1});
            }
        }
    }
    
    return ans;
}



void getMin(int n, int cnt, int num){
    
    if(cnt==node.size()-1){
        result= result> num ? num : result;
        return; 
    }   

    //cout<<n<<endl;
    for (int i = 0; i < v[n].size(); i++)
    {
        int nextNode=v[n][i].first;
        int cost=v[n][i].second;

        if(!checknode[nextNode]){
            checknode[nextNode]=true;
            getMin(nextNode, cnt+1, num+cost);
            checknode[nextNode]=false;
        }
    }

}


int main(){
    
    int sx, sy;

    while(1){

        cin>>w>>h;
        string s;
        if(w==0 && h==0) break;
        result=MAX;


        for (int i = 0; i < 12; i++)
        {
            v[i].clear();
        }
        
        node.clear();
        memset(checknode, false, sizeof(checknode));
        for (int i = 0; i < h; i++)
        {   
            cin>>s;
            for (int j = 0; j < w; j++)
            {
                map[i][j]=s[j];
                if(map[i][j]=='o' ||  map[i][j]=='*'){
                    if(map[i][j]=='o'){
                        sx=i; sy=j;
                    }
                    node.push_back({i, j});
                }
                
            }
            
        }
        bool flag=false;
        int startnode;
        for (int i = 0; i < node.size(); i++)
        {   
            if(node[i].first==sx && node[i].second==sy) startnode=i;
            for (int j = i+1; j < node.size(); j++)
            {
                int w=getSol(node[i].first, node[i].second, node[j].first, node[j].second);
                if(w==-1){
                    cout<<-1<<endl;
                    flag=true;
                    break;
                }
                v[i].push_back({j, w});
                v[j].push_back({i, w});
            }
            if(flag) break;
        }

        if(flag) continue;

        checknode[startnode]=true;
        getMin(startnode, 0, 0);
        cout<<result<<endl;

    }

    return 0;
}