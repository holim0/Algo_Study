#include<iostream>
#include<cstring>
using namespace std;

char map[105][105];
bool map2[105][105];
bool map3[105][105];
int n;


void reset(){

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            map2[i][j]=map3[i][j];
        }
        
    }
    
}
int main(){

    cin>>n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin>>map[i][j];
            if(map[i][j]=='X') {map2[i][j]=true; map3[i][j]=true;}
        }
    }

    int garo=0;

    for (int i = 0; i < n; i++)
    {   
        for (int j = 0; j < n-1; j++)
        {
            if(!map2[i][j]){
                if(!map2[i][j+1]){
                    for (int k = j; k < n; k++)
                    {
                        if(!map2[i][k]) map2[i][k]=true;
                        else break;
                    }
                    garo++; 
                }
            }
        }
    }

    int sero=0;
    reset();

    for (int i = 0; i < n; i++)
    {   
        for (int j = 0; j < n-1; j++)
        {
            if(!map2[j][i]){
                if(!map2[j+1][i]){
                    for (int k = j; k < n; k++)
                    {
                        if(!map2[k][i]) map2[k][i]=true;
                        else break;
                    }
                    sero++; 
                }
            }
        }
    }
    
    
    cout<<garo<<" "<<sero<<endl;

    return 0;

}