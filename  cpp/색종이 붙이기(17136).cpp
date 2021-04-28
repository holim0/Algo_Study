#include<iostream>

#include<algorithm>


using namespace std; 


int map[11][11];
int n1, n2, n3, n4, n5;
bool mapCheck[11][11];
int dx[]={0, 1};
int dy[]={1, 0};
int cnt=0;
int paper[]={0, 5, 5, 5, 5, 5};

int result=987654321;


bool isdone(){

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if(map[i][j]==1) return false;
        }
        
    }
    
    return true;

}

void go(int x, int y){

    if(y==10){
        go(x+1, 0);
    }

    if(x==10){
        result=min(result, cnt);
        return;
    }
    
    if(map[x][y]==0){
        go(x, y+1);
    }

    for (int size = 5; size>=1 ; size--)
    {
        if(x+size>10 || y+size>10 || paper[size]==0) continue;


        bool check=true;

        for (int i = x; i < x+size; i++)
        {
           for (int j = y; j < y+size; j++)
           {
               if(map[i][j]==0) {check= false; break;}
           }
           if(!check) break;
        }

        if(!check){
            continue;
        }

        paper[size]--;
        cnt++;
        for (int i = x; i < x+size; i++)
        {
           for (int j = y; j < y+size; j++)
            {
               map[i][j]=0;
            }
        }

        go(x, y+size);

        for (int i = x; i < x+size; i++)
        {
           for (int j = y; j < y+size; j++)
            {
               map[i][j]=1;
            }
        }

        paper[size]++;
        cnt--;

    }
    



}
    



int main(){

    for(int i=0; i<10; i++){
        for (int j = 0; j < 10; j++)
        {
            cin>>map[i][j];
        }
    }

    if(isdone()){
        cout<<0<<endl;
        return 0;
    }
    
    go(0, 0);

    if(result==987654321){
        cout<<-1<<endl;
        return 0;
    }

    cout<<result<<endl;

    return 0;
}