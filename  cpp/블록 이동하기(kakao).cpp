#include<iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};
int result=-1;
int size;
bool check[105][105][2];

struct machine{
    int fx;
    int fy;
    int sx;
    int sy;
    int dir;  //가로 0 세로 1
    int time;
};

bool range(int x, int y){
    
    if(x>=0 && x<size && y>=0 && y<size) return true;
    else return false;
}

void bfs(vector<vector<int>> map){
    
    queue<machine> q;
    q.push({0, 0, 0, 1, 0, 0}); 
    check[0][0][0]=true;
    check[0][1][0]=true;
    
    while(!q.empty()){
        machine cur= q.front(); q.pop();
        //cout<<cur.fx<<cur.fy<<cur.sx<<cur.sy<<" "<<cur.dir<<endl;
        if((cur.fx==size-1 && cur.fy==size-1) || (cur.sx==size-1 && cur.sy==size-1)){
            result=cur.time;
            break;
        }
        if(cur.dir==0){
                for(int i=0; i<4; i++){
                    int nx1=cur.fx+dx[i];
                    int ny1=cur.fy+dy[i];
                    int nx2=cur.sx+dx[i];
                    int ny2=cur.sy+dy[i];
                    if(range(nx1, ny1) && range(nx2, ny2)){
                        if(dy[i]==1){
                            if(!check[nx2][ny2][cur.dir] && map[nx2][ny2]==0){
                                check[nx2][ny2][cur.dir]=true;
                                q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                            }
                        }else if(dy[i]==-1){
                            if(!check[nx1][ny1][cur.dir] && map[nx1][ny1]==0){
                                check[nx1][ny1][cur.dir]=true;
                                q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                            }

                        }else{
                            if(!check[nx1][ny1][cur.dir] && !check[nx2][ny2][cur.dir] && map[nx1][ny1]==0 && map[nx2][ny2]==0){
                                check[nx1][ny1][cur.dir]=true;
                                check[nx2][ny2][cur.dir]=true;
                                q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                            }   
                       }    
                 }
            }
        }else{
            for(int i=0; i<4; i++){
                int nx1=cur.fx+dx[i];
                int ny1=cur.fy+dy[i];
                int nx2=cur.sx+dx[i];
                int ny2=cur.sy+dy[i];
                
                if(range(nx1, ny1) && range(nx2, ny2)){
                    //cout<<"next: "<<nx1<<ny1<<nx2<<ny2<<endl;
                    if(dy[i]==-1 || dy[i]==1){
                        if(map[nx1][ny1]==0 && map[nx2][ny2]==0 && !check[nx1][ny1][1] && !check[nx2][ny2][1]){
                            check[nx1][ny1][1]=true;
                            check[nx2][ny2][1]=true;
                            q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                        }
                    }else if(dx[i]==-1){
                        if(map[nx1][ny1]==0 && !check[nx1-1][ny1][1]){
                            check[nx1][ny1][cur.dir]=true;
                            q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                        }
                    }else if(dx[i]==1){
                        if(map[nx2][ny2]==0 && !check[nx2][ny2][1]){
                            check[nx2][ny2][cur.dir]=true;
                            q.push({nx1, ny1, nx2, ny2, cur.dir, cur.time+1});
                        }
                    }
                }
            }    
        }
        
        
        if(cur.dir==0){     //가로
            for(int i=0; i<2; i++){
                int nx= cur.fx+dx[i];
                int ny= cur.fy+dy[i];
                if(range(nx, ny) && range(nx, ny+1) && map[nx][ny]==0 && map[nx][ny+1]==0){
                    if(!check[nx][ny][1]){
                        check[nx][ny][1]=true;
                        check[cur.fx][cur.fy][1]=true;
                        if(dx[i]==-1){
                            q.push({nx, ny, cur.fx, cur.fy, 1, cur.time+1});
                        }else{
                            q.push({cur.fx, cur.fy, nx, ny, 1, cur.time+1});
                        }
                    } 
                }
            }
        
            for(int i=0; i<2; i++){
                int nx=cur.sx+dx[i];
                int ny=cur.sy+dy[i];
                if(range(nx, ny) && range(nx, ny-1) && map[nx][ny]==0 && map[nx][ny-1]==0){
                    if(!check[nx][ny][1]){
                        check[nx][ny][1]=true;
                        check[cur.sx][cur.sy][1]=true;
                        if(dx[i]==-1){
                            q.push({nx, ny, cur.sx, cur.sy, 1, cur.time+1});
                        }else{
                             q.push({cur.sx, cur.sy, nx, ny, 1, cur.time+1});
                        }
                    
                    }
                }
            }
        }else{    // 세로
            for(int i=2; i<4; i++){
                int nx=cur.fx+dx[i];
                int ny=cur.fy+dy[i];
                if(map[nx][ny]==0 && map[nx+1][ny]==0 && range(nx, ny) && range(nx+1, ny)){
                    if(!check[nx][ny][0]){
                        check[nx][ny][0]=true;
                        check[cur.fx][cur.fy][0]=true;
                        if(dy[i]==1){
                            q.push({cur.fx, cur.fy, nx, ny, 0, cur.time+1});
                        }else{
                             q.push({nx, ny, cur.fx, cur.fy, 0, cur.time+1});
                        }
                        
                       
                    }
                } 
            }
            
            for(int i=2; i<4; i++){
                int nx=cur.sx+dx[i];
                int ny=cur.sy+dy[i];
                if(map[nx][ny]==0 && map[nx-1][ny]==0 && range(nx, ny) && range(nx-1, ny)){
                    check[nx][ny][0]=true;
                    check[cur.sx][cur.sy][0]=true;
                    if(dy[i]==1){
                        q.push({cur.sx, cur.sy, nx, ny, 0, cur.time+1});
               
                    }else{
                        q.push({nx, ny, cur.sx, cur.sy, 0, cur.time+1});
                    }
                }  
            }           
        }  
    }
}


int solution(vector<vector<int>> board) {
    int answer = 0;
    
    
    size=board.size();
    bfs(board);
    
    answer=result;
    return answer;
}