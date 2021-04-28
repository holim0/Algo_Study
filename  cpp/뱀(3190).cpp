#include<iostream>
#include<cstring>
#include<queue>
#define Apple 4
#define bam 9

using namespace std;

int map[105][105];
int N, K;  // k는 사과 개수

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
int playtime=0;
queue<pair<int, char>>command;
queue<pair<int, int>> bambody;




void play(int headx, int heady, string curDir){
    int time=10000;
    char dir;
    if(!command.empty()){
        time=command.front().first;
        dir=command.front().second;
        command.pop();
    }


    if(curDir=="right"){
        while(playtime<time){
            if(map[headx][heady+1]==Apple && heady+1<=N){
                map[headx][heady+1]=bam;
                heady+=1;
                bambody.push({headx, heady});
            }else if(map[headx][heady+1]==bam || heady+1>N){
                playtime++;
                return;
            }else if(map[headx][heady+1]==0 &&heady+1<=N){
                map[headx][heady+1]=bam;
                heady+=1;            
                bambody.push({headx, heady});
                map[bambody.front().first][bambody.front().second]=0;
                bambody.pop();
            }
            playtime++;
        }
        
        
        if(dir=='D'){
            curDir="Down";
        }else{
            curDir="Up"; 
        }
        play(headx, heady,curDir);

    }else if(curDir=="left"){
        while(playtime<time){
            if(map[headx][heady-1]==Apple && heady-1>0){
                map[headx][heady-1]=bam;
                heady-=1;
                bambody.push({headx, heady});
            }else if(map[headx][heady-1]==bam || heady-1<=0){
                playtime++;
                return;
            }else if(map[headx][heady-1]==0 &&heady-1>0){
                map[headx][heady-1]=bam;
                heady-=1;
                bambody.push({headx, heady});
                map[bambody.front().first][bambody.front().second]=0;
                bambody.pop();
            }
            playtime++;
        }
        if(dir=='D'){
            curDir="Up";
        }else{
            curDir="Down"; 
        }
        play(headx, heady,curDir);

    }else if(curDir=="Down"){
        while(playtime<time){
            if(map[headx+1][heady]==Apple && headx+1<=N){
                map[headx+1][heady]=bam;
                headx+=1;
                bambody.push({headx, heady});
            }else if(map[headx+1][heady]==bam || headx+1>N){
                playtime++;
                return;
            }else if(map[headx+1][heady]==0 &&headx+1<=N){
                map[headx+1][heady]=bam;
                headx+=1;
                bambody.push({headx, heady});
                map[bambody.front().first][bambody.front().second]=0;
                bambody.pop();
            }
            playtime++;
        }

        if(dir=='D'){
            curDir="left";
        }else{
            curDir="right"; 
        }
        play(headx, heady,curDir);

    }else if(curDir=="Up"){
        while(playtime<time){
            if(map[headx-1][heady]==Apple && headx-1>0){
                map[headx-1][heady]=bam;
                headx-=1;
                bambody.push({headx, heady});
            }else if(map[headx-1][heady]==bam || headx-1<=0){
                playtime++;
                return;
            }else if(map[headx-1][heady]==0 &&headx-1>0){
                map[headx-1][heady]=bam;
                headx-=1;
                bambody.push({headx, heady});
                map[bambody.front().first][bambody.front().second]=0;
                bambody.pop();
            }
            playtime++;
        }

        if(dir=='D'){
            curDir="right";
        }else{
            curDir="left"; 
        }
        play(headx, heady,curDir);

    }




}



int main(){

    cin>>N>>K;

    memset(map, 0, sizeof(map));

    int x, y;
    map[1][1]=bam; //처음 뱀 위치 

    for (int i = 0; i < K; i++)
    {
        cin>>x>>y;
        map[x][y]=Apple;
    }

    int dir; cin>>dir;
    int a; char b;
    for (int i = 0; i < dir; i++)
    {
        cin>>a>>b;
        command.push({a, b});
    }

    bambody.push({1, 1});
    play(1,1, "right");
    


    cout<<playtime<<endl;


    return 0;
}