#include<iostream>

using namespace std;

int map[53][53];
bool cleanCheck[53][53]={false,};
int N, M, r, c, dir;
int result=0;
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

bool chLeft(int x, int y){

    if(x>=0 && x<N && y>=0 && y<M && map[x][y]==0 && !cleanCheck[x][y]) return true;

    return false;

}

bool chAll(int x, int y){

    for (int i = 0; i < 4; i++)
    {
        int nx=x+dx[i]; int ny=y+dy[i];
        if(nx>=0 && nx<N && ny>=0 && ny<M && map[nx][ny]==0 && !cleanCheck[nx][ny]) return false;
    }


    return true;
    

}

void startClean(int curx, int cury, int dir){

    //cout<<curx<<cury<<dir<<endl;
    
    switch (dir)
    {
    case 0:   //북

        if(chAll(curx, cury)){
            if(curx+1<N && map[curx+1][cury]!=1){
                curx+=1;
                startClean(curx, cury, dir);
            }else{
                return;
            }
        }else{
            if(chLeft(curx, cury-1)){
                dir=3;
                cleanCheck[curx][cury-1]=true;
                result++;
                cury-=1;
                startClean(curx, cury, dir);
            }else{
                dir=3;
                startClean(curx, cury, dir);
            }

        }

        


        break;
    case 1:    //동
        
        if(chAll(curx, cury)){
            if(cury-1<M && map[curx][cury-1]!=1){
                cury-=1;
                startClean(curx, cury, dir);
            }else{
                return;
            }
        }else{
            if(chLeft(curx-1, cury)){
                dir=0;
                cleanCheck[curx-1][cury]=true;
                result++;
                curx-=1;
                startClean(curx, cury, dir);
            }else{
                dir=0;
                startClean(curx, cury, dir);
            }

        }

       

        break;

    case 2:    //남
        if(chAll(curx, cury)){
            if(curx-1>=0 && map[curx-1][cury]!=1){
                curx-=1;
                startClean(curx, cury, dir);
            }else{
                return;
            }
        }
        else{
            if(chLeft(curx, cury+1)){
                dir=1;
                cleanCheck[curx][cury+1]=true;
                result++;
                cury+=1;
                startClean(curx, cury, dir);
            }else{
                dir=1;
                startClean(curx, cury, dir);
            }



        }

        
        break;
    case 3:    // 서
        if(chAll(curx, cury)){
            if(cury+1<M && map[curx][cury+1]!=1){
                cury+=1;
                startClean(curx, cury, dir);
            }else{
                return;
            }
        }else{
            if(chLeft(curx+1, cury)){
                dir=2;
                cleanCheck[curx+1][cury]=true;
                curx+=1;
                result++;
                startClean(curx, cury, dir);
            }else{
                dir=2;
                startClean(curx, cury, dir);
            }
        }

        
        break;
    
    default:
        break;
    }

    

}


int main(){

    cin>>N>>M;
    cin>>r>>c>>dir;
   
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
            if(map[i][j]==1) cleanCheck[i][j]=true;
        }
        
    }

    

    cleanCheck[r][c]=true; result++;
    
    
    startClean(r, c, dir);
    


    cout<<result<<endl;
    



    return 0;
}