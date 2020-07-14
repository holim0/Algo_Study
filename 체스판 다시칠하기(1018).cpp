#include<iostream>
#include<algorithm>

using namespace std;

int N, M;

char chess[52][52];
char tmpmap[52][52];
int cnt;
int result=98765431;

char map1[8][8]={

    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'}
};

char map2[8][8]={

    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'}
};

void Copy(){

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            tmpmap[i][j]=chess[i][j];
        }
        
    }
    
}

void getslice(int x, int y){

    if(x+7>=N || y+7>=M) return;
    
    int cnt1=0; int cnt2=0;
    for (int i = x; i < x+8; i++)
    {
        for (int j = y; j < y+8; j++)
        {
            if(chess[i][j]!=map1[i-x][j-y]) {cnt1++;}

            if(chess[i][j]!=map2[i-x][j-y]) {cnt2++;}
           
        } 
    }
    
    result= min(cnt1, min(cnt2, result));

}

int main(){

    cin>>N>>M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin>>chess[i][j];
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            getslice(i, j);
        }
        
    }

    cout<<result<<endl;


    return 0;
}