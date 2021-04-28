#include<iostream>
#include<queue>
#include<algorithm>
#include<cstring>

using namespace std;

int N;
int map[105][105];
int minRain=200;
int maxRain=-1;
bool check[105][105]={false, };

int result=-1;

int dx[]={1, -1, 0 ,0};
int dy[]={0, 0, -1, 1};

int getSol(){

    queue<pair<int, int>> q;
    int region=0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(!check[i][j]){
                q.push({i, j});
                check[i][j]=true;
                while(!q.empty()){
                    int x=q.front().first; int y=q.front().second;
                    q.pop();
                    for(int k=0; k<4; k++){
                        int nx=x+dx[k]; int ny=y+dy[k];
                        if(!check[nx][ny] && nx>=0 && nx<N && ny>=0 && ny<N){
                            check[nx][ny]=true;
                            q.push({nx, ny});
                        }
                    }
                }  
                region++;
            }

        }
        
    }
    

    return region;

}

void rainning(int gangsu){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(map[i][j]<=gangsu) check[i][j]=true;
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
            minRain=min(map[i][j], minRain);
            maxRain=max(map[i][j], maxRain);
        }
        
    }
    
    int val;
    for (int i = 0; i <= maxRain; i++)
    {
        memset(check, false, sizeof(check));
        rainning(i);
        val= getSol();
        result= val> result ? val :result;
    }
    

    
    cout<<result<<endl;

    return 0;
}