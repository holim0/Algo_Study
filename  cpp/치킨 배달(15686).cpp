#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#define MAX 987654321

using namespace std;

vector<pair<int, int>> home;
vector<pair<int, int>> chicken;
vector<pair<int, int>> selected;
int N, M;
int map[55][55];
int result=MAX;
bool check[55][55]={false, };

int getSol(){

    int sum=0;
    int tmpdist=MAX;
    int dist;

    for (int i = 0; i < home.size(); i++)
    {
        tmpdist=MAX;
        int hx=home[i].first; int hy= home[i].second;
        for (int j = 0; j < selected.size(); j++)
        {   
            int sx=selected[j].first; int sy=selected[j].second;
            dist=abs(hx-sx)+abs(hy-sy);
            tmpdist= tmpdist > dist ? dist : tmpdist;
        }

        sum+=tmpdist;
    }

    return sum;

}


void johab(int start, int cnt, int num){

    if(num==cnt){
        
        int val=getSol();

        result= result> val ? val : result;
        
        return;
    }

    for (int i = start; i < chicken.size(); i++)
    {
        int x=chicken[i].first; int y=chicken[i].second;
        if(!check[x][y]){
            check[x][y]=true;
            selected.push_back({x, y});
            johab(i, cnt+1, num);
            check[x][y]=false;
            selected.pop_back();
        }
    }
    
}


int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
            if(map[i][j]==1){
                home.push_back({i, j});
            }else if(map[i][j]==2){
                chicken.push_back({i, j});
            }
        }
        
    }

    for (int i = 1; i <=M; i++)
    {   
        memset(check, false, sizeof(false));
        johab(0,0, i);
    }


    cout<<result<<endl;


    return 0;
}