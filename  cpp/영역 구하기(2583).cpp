#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std; 
int M, N, k;
bool check[105][105]={false, };
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
int cnt=0;
vector<int> v;

bool range(int x, int y){
    if(x>=0 && x<M && y>=0 && y<N) return true;
    else return false;
}
void bfs(){

    queue<pair<int, int>> q;
    
    

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {   
            int size=0;
            if(!check[i][j]){
                check[i][j]=true;
                q.push({i, j});
                size++;
                while(!q.empty()){
                    int curx=q.front().first; int cury=q.front().second;
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k]; int ny=cury+dy[k];
                        if(!check[nx][ny] && range(nx, ny)){
                            check[nx][ny]=true; 
                            q.push({nx, ny});
                            size++;
                        }
                    }
                    
                }
                cnt++;
                v.push_back(size);
            }
            
            
        }
        
    }
    

}

void checkR(int x1, int y1, int x2, int y2){
    
    for(int i=x1; i<x2; i++){
        for (int j = y1; j < y2; j++)
        {
            check[i][j]=true;
        }
    }

}


int main(){

    cin>>M>>N>>k;
    int x1, x2, y1, y2;

    for (int i = 0; i < k; i++)
    {
        cin>>x1>>y1>>x2>>y2;
        checkR(y1, x1, y2, x2);
    }
    
    bfs();

    sort(v.begin(), v.end());

    cout<<cnt<<endl;

    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    


    return 0;
}