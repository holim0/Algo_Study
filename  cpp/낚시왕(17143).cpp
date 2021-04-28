#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<cstring>

using namespace std;
int R, C, M;
int result=0;
bool check[10005]={false, };
queue<pair<pair<int, int>, int>> map[105][105];



void move2(int i, int j){

    int speed=map[i][j].front().first.first;
    int dist=map[i][j].front().first.second;
    int size=map[i][j].front().second;
    map[i][j].pop();
    int ndist=dist;
    if(dist==1 || dist==2){
        for(int k=1; k<=speed; k++){
            
            if(ndist==1 && i>1){
                i-=1;
            }
            else if(ndist==1 && i==1){
                ndist=2;
                i+=1;
            }else if(ndist==2 && i<R){
                i+=1;
            }else if(ndist==2 && i==R){
                ndist=1;
                i-=1;
            }
        }
        
    }
    else{
        for (int k = 1; k <= speed; k++)
        {
            if(ndist==3 && j<C){
                j+=1;
            }else if(ndist==3 && j==C){
                ndist=4; 
                j-=1;
            }else if(ndist==4 && j>1){
                j-=1;
            }else if(ndist==4 && j==1){
                ndist=3;
                j+=1;
            }
        }
    }
    map[i][j].push({{speed, ndist}, size});

}

void move(){

    for (int i = 1; i <= R; i++)
    {
        for (int j = 1; j <= C; j++)
        {
            if(map[i][j].size()>=1 && !check[map[i][j].front().second]){
                check[map[i][j].front().second]=true;
                move2(i, j);
            }
        }
        
    }
    


}

void getSol(int location){

    if(location==C+1){
        cout<<result<<endl;
        return;
    }
    int mindist=200; int minlo=-1;
    for (int i = 1; i <=R; i++)
    {
        if(map[i][location].size()> 0){
            minlo=i;
            break;
        }   
    }
    
    if(minlo!=-1){
        
        result+=map[minlo][location].front().second;
        map[minlo][location].pop();
    }
    
    

    memset(check, false, sizeof(check));
    move();    

    int maxspeed, maxd, maxsize;
    for (int i = 1; i <= R; i++)
    {
        for (int j = 1; j <= C; j++)
        {
            if(map[i][j].size()>1){
                maxsize=-1;
                while(!map[i][j].empty()){

                    if(maxsize<map[i][j].front().second){
                        maxsize=map[i][j].front().second;
                        maxd=map[i][j].front().first.second;
                        maxspeed=map[i][j].front().first.first;
                    }
                    map[i][j].pop();
                }
                map[i][j].push({{maxspeed, maxd}, maxsize});
                
            }
        }
        
    }
    

    getSol(location+1);

}

int main(){

    cin>>R>>C>>M;
    int r, c, s, d, z;

    for (int i = 0; i < M; i++)
    {
        cin>>r>>c>>s>>d>>z;
        map[r][c].push({{s, d}, z});
    }

    
    getSol(1);


    return 0;
}