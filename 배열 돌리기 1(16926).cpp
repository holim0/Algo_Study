#include<iostream>

using namespace std;

int N, M, R;

int map[305][305];
int copymap[305][305];

void Copy(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            copymap[i][j]=map[i][j];
        }
        
    }
    
}

void Back(){
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            map[i][j]=copymap[i][j];
        }
        
    }

}

void go(int x, int y, int garo, int sero){

    if(garo<=1 || sero<=1){
        return;
    }
    ///위쪽
   
    int val=copymap[x][y];
    
    for (int i = y; i < y+garo-1; i++)
    {
        copymap[x][i]=copymap[x][i+1];
    }

    ///왼쪽
    int val2=copymap[x+sero-1][y];
    for(int i=x+sero-1; i>x; i--){
        if(i==x+1){
            copymap[i][y]=val;
        }else{
            copymap[i][y]=copymap[i-1][y];
        }
        
    }

    //아래쪽
    int val3=copymap[x+sero-1][y+garo-1];
    for (int i = y+garo-1; i>y; i--)
    {
        if(i==y+1){
            copymap[x+sero-1][i]=val2;
        }else{
            copymap[x+sero-1][i]=copymap[x+sero-1][i-1];
        }
    }

    //오른쪽

    for (int i = x; i < x+sero-1; i++)
    {   
        if(i==x+sero-2){
            copymap[i][y+garo-1]=val3;
        }else{
            copymap[i][y+garo-1]=copymap[i+1][y+garo-1];
        }
    }

    go(x+1, y+1, garo-2, sero-2);
}

int main(){

    cin>>N>>M>>R;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>map[i][j];
        }
        
    }

    for (int i = 0; i < R; i++)
    {   
        Copy();
        go(0, 0, M, N);
        Back();
    }
    
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout<<map[i][j]<<" ";
        }
        cout<<endl;
    }


    return 0;
}