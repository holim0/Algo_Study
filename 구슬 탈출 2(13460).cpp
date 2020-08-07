#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
bool isOver=false;
char map[15][15];
int N, M;
int result=987654321;

int Rx, Ry, Bx, By, tx, ty;

void move(int rx, int ry, int bx, int by, int num, int dir){

    if(num>10){
        return;
    }
    int orx=rx;    int obx=bx;
    int ory=ry;    int oby=by;

    bool isRedIn=false;
    bool isBlueIn=false;

    


    while(1){
        
        if(map[rx+dx[dir]][ry+dy[dir]]=='#') break;
        if(map[rx+dx[dir]][ry+dy[dir]]=='O'){
            isRedIn=true;
            break;
        }
        rx+=dx[dir]; ry+=dy[dir];
    }

    while(1){

        if(map[bx+dx[dir]][by+dy[dir]]=='#') break;
        if(map[bx+dx[dir]][by+dy[dir]]=='O'){
            isBlueIn=true;
            break;
        }

        bx+=dx[dir]; by+=dy[dir];
    }

    if(isBlueIn) return;
    else{
        if(isRedIn){
            result= min(result, num);
            return;
        }
    }

    if(rx==bx && ry==by){
        int d1=abs(orx-rx)+abs(ory-ry);
        int d2=abs(obx-bx)+abs(oby-by);

        if(d1>d2){
            rx-=dx[dir]; ry-=dy[dir];
        }else{
            bx-=dx[dir]; by-=dy[dir];
        }
    }

    
    if(dir==0 || dir==1){
        move(rx, ry, bx, by, num+1, 2);
        move(rx, ry, bx, by, num+1, 3);
    }else{
        move(rx, ry, bx, by, num+1, 0);
        move(rx, ry, bx, by, num+1, 1);
    }
    

}

int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
            if(map[i][j]=='O'){
                tx=i; ty=j;
            }else if(map[i][j]=='R'){
                Rx=i; Ry=j;
            }else if(map[i][j]=='B'){
                Bx=i; By=j;
            }
        }
        
    }
    
    for (int i = 0; i < 4; i++)
    {
        move(Rx, Ry, Bx, By, 1, i);
    }
    
    if(result==98764321 || result>10){
        cout<<-1<<endl;
    }else{
        cout<<result<<endl;
    }
}