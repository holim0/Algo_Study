#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int map[10][10];
int copymap[10][10];

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

vector<pair<int, int>> guard;
bool check[10][10]={false,};
vector<pair<int, int>> t;
queue<pair<int, int>> qu;
int N, M;

int result=-1;

int getSafeNum(){

    int cnt=0;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if(copymap[i][j]==0) cnt++;
        }
        
    }
    

    return cnt;

}


void goVirus(){

        bool tmpcheck[10][10]={false, };
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <=M; j++)
            {
                if(copymap[i][j]==2 && !tmpcheck[i][j]){
                    qu.push({i,j});
                    tmpcheck[i][j]=true;
                    while(!qu.empty()){
                        int ix=qu.front().first; int iy=qu.front().second;
                        qu.pop();
                        for (int k = 0; k < 4; k++)
                        {
                            int nx=ix+dx[k]; int ny=iy+dy[k];
                            if(nx>0 && nx<=N && ny>0 && ny<=M && copymap[nx][ny]==0){
                                qu.push({nx, ny});
                                copymap[nx][ny]=2;
                                tmpcheck[nx][ny]=true;

                            }
                        }    
                    }
                    
                }
            }
            
        }
      
    


}



void Copy(){

    for (int i = 1; i <=N; i++)
        {
            for (int j = 1; j <=M; j++)
            {
                copymap[i][j]=map[i][j];
            }
        }

}

void getjJohab(int n, int start){

    if(n==3){
        Copy();
        for (int i = 0; i < t.size(); i++)
        {
            copymap[t[i].first][t[i].second]=1;
        }
        
        goVirus();
        int val=getSafeNum();
        result= val>result ? val : result;
        return;
    }


    for (int i = start; i < guard.size(); i++)
    {
        int x=guard[i].first; int y=guard[i].second;
        if(!check[x][y]){
            check[x][y]=true;
            t.push_back({x, y});
            getjJohab(n+1, i);
            check[x][y]=false;
            t.pop_back();
        }
    }
    



}


int main(){

    cin>>N>>M;

    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=M; j++)
        {
            cin>>map[i][j];
        }
    }


    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=M; j++)
        {
            if(map[i][j]==0) guard.push_back({i, j});
        }
    }


    getjJohab(0, 0);


    cout<<result<<endl;
    return 0;
}