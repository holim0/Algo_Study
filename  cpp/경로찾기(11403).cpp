#include<iostream>
#include<cstring>

using namespace std;

int map[105][105];
bool check[105]={false, };
int result[105][105];

int N;
void go(int start, int end, int base){
    
    if(map[start][end]==1){
        result[base][end]=1;
        return;
    }
    

    for (int i = 0; i < N; i++)
    {
        if(!check[i] && map[start][i]==1){
            check[i]=true;
            go(i, end, base);
        }
    }
}

int main(){

    cin.tie(NULL);
	cout.tie(NULL);
    cin>>N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin>>map[i][j];
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {   
            memset(check, false, sizeof(check));
            go(i, j, i);
        }
        
    }


    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout<<result[i][j]<<" ";
        }
        cout<<'\n';
        
    }
    
    
    

    return 0;
}