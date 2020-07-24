#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int map[105][105];
bool check[105][105]={false, };
int N;

int dx[]={1, -1, 0 ,0};
int dy[]={0, 0,-1, 1};
queue<pair<int, int>> q;

vector<pair<int, int>> island[10005];
vector<int> tmp;
int islandNum=1;
int finalResult=987654321;
int arr[10005];
bool arr2[10005]={false, };

void go(){


    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(!check[i][j] && map[i][j]==1){
                q.push({i, j});
                island[islandNum].push_back({i, j});
                check[i][j]=true;
                while(!q.empty()){
                    int curx= q.front().first; int cury=q.front().second;
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k]; int ny= cury+dy[k];
                        if(nx>=0 && nx<N && ny >=0 && ny<N && !check[nx][ny] && map[nx][ny]==1){
                            check[nx][ny]=true;
                            q.push({nx, ny}); island[islandNum].push_back({nx, ny});
                        }
                    }
                }
                islandNum++;
                
            }
        }
        
    }

}

int getlen(int land1, int land2){

    int minLen=987654321;
    int comLen;
    int val1, val2;

    for (int i = 0; i <island[land1].size(); i++)
    {
        for (int j = 0; j < island[land2].size(); j++)
        {
            val1=abs(island[land1][i].first-island[land2][j].first);
            val2=abs(island[land1][i].second-island[land2][j].second);
            comLen=val1+val2-1;
            minLen=min(minLen, comLen);
        }
        
    }

    return minLen;

}

void getJohab(int start, int cnt){
    if(cnt==2){
        
        int val=getlen(tmp[0], tmp[1]);
        finalResult= finalResult>val ? val : finalResult;
        return;
    }

    for(int i=start; i<islandNum; i++){
        if(!arr2[i]){
            arr2[i]=true;
            tmp.push_back(i);
            getJohab(i, cnt+1);
            arr2[i]=false;
            tmp.pop_back();
        }
    }

}


int main(){

    cin>>N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
        }   
    }

    go();

    for (int i = 1; i < islandNum; i++){
        arr[i]=i;
    }

    getJohab(1, 0);


    cout<<finalResult<<endl;

    
    
    return 0;
}