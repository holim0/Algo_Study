#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int dx[]={-1, 1, 0, 0}; // 위 아래 왼 오
int dy[]={0, 0, -1, 1};
int result=-1;
int map[25][25];
int N;


int findMAX(int map2[][25]){
    int sum=-1;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            sum=max(sum, map2[i][j]);
        }
        
    }
    

    return sum;
}

bool canP(int x1, int y1, int x2, int y2, int map2[][25]){
    
    if(map2[x1][y1] == map2[x2][y2] && map2[x1][y1]!=0 && map2[x2][y2]!=0) return true;


    return false;

}

void copy(int map3[][25], int map2[][25]){
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            map2[i][j]=map3[i][j];
        }
        
    }
    
}



void move(int cnt, int map3[][25], int num, int dir){

    if(cnt==5){
        result= max(result, num);
        return ;
    }
    int map2[25][25];

    copy(map3, map2);    
    
    switch (dir)
    {
    case 0: 
    
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && i>0){
                    int nx=i; 
                    while(1){
                        nx-=1;
                        if(nx<0 || map2[nx][j]!=0) break;
                    }
                    if(map2[nx+1][j]!=map2[i][j]){
                        map2[nx+1][j]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
            
        }

        for (int i = 0; i <N; i++)
        {
            for (int j = 0; j<N-1; j++)
            {
                if(canP(j, i, j+1, i, map2)){
                    map2[j][i]+=map2[j+1][i];
                    map2[j+1][i]=0;
                }
            }
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && i>0){
                    int nx=i; 
                    while(1){
                        nx-=1;
                        if(nx<0 || map2[nx][j]!=0) break;
                    }
                    if(map2[nx+1][j]!=map2[i][j]){
                        map2[nx+1][j]=map2[i][j];
                        map2[i][j]=0;
                    }
                    
                }
            }   
        }
    
        break;
        
    case 1:
        
        for (int i = N-1; i>=0; i--)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && i<N-1){
                    int nx=i; 
                    while(1){
                        nx+=1;
                        if(nx>=N || map2[nx][j]!=0) break;
                    }
                    if(map2[nx-1][j]!=map2[i][j]){
                        map2[nx-1][j]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
            
        }
        
        for (int i = 0; i <N; i++)
        {
            for (int j = N-1; j>0; j--)
            {
                if(canP(j, i, j-1, i, map2)){
                    map2[j][i]+=map2[j-1][i];
                    map2[j-1][i]=0;
                }
            }
        }
        

        for (int i = N-1; i>=0; i--)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && i<N-1){
                    int nx=i; 
                    while(1){
                        nx+=1;
                        if(nx>=N || map2[nx][j]!=0) break;
                    }
                    if(map2[nx-1][j]!=map2[i][j]){
                        map2[nx-1][j]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
        }   

        break;
    case 2:   // 왼
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && j>0){
                    int ny=j;
                    while(1){
                        ny-=1;
                        if(ny<0 || map2[i][ny]!=0) break;
                    }
                    if(map2[i][ny+1]!=map2[i][j]){
                        map2[i][ny+1]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N-1; j++)
            {
                if(canP(i, j, i, j+1, map2)){
                    map2[i][j]+=map2[i][j+1];
                    map2[i][j+1]=0;
                }
            }
            
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if(map2[i][j]!=0 && j>0){
                    int ny=j;
                    while(1){
                        ny-=1;
                        if(ny<0 || map2[i][ny]!=0) break;
                    }
                    if(map2[i][ny+1]!=map2[i][j]){
                        map2[i][ny+1]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
        }
        
            
        break;
    case 3:  //오
        
        for (int i = 0; i < N; i++)
        {
            for (int j = N-1; j>=0; j--)
            {
                if(map2[i][j]!=0 && j<N-1){
                    int ny=j;
                    while(1){
                        ny+=1;
                        if(ny>=N || map2[i][ny]!=0) break;
                    }
                    if(map2[i][ny-1]!=map2[i][j]){
                        map2[i][ny-1]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = N-1; j>0; j--)
            {
                if(canP(i, j, i, j-1, map2)){
                    map2[i][j]+=map2[i][j-1];
                    map2[i][j-1]=0;
                }
            }
            
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = N-1; j>=0; j--)
            {
                if(map2[i][j]!=0 && j<N-1){
                    int ny=j;
                    while(1){
                        ny+=1;
                        if(ny>=N || map2[i][ny]!=0) break;
                    }
                    if(map2[i][ny-1]!=map2[i][j]){
                        map2[i][ny-1]=map2[i][j];
                        map2[i][j]=0;
                    }
                }
            }
        }
        
        break;
    
    default:
        break;
    }

    num=findMAX(map2);
    for (int i = 0; i < 4; i++)
    {   
        move(cnt+1, map2, num, i);
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

    for (int i = 0; i < 4; i++)
    {
        move(0, map, 0, i);
    }
    
    
    cout<<result<<endl;

    return 0;
}