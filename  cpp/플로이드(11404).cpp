#include<iostream>
#include<algorithm>
#define MAX 987654321
using namespace std;
int n, m;
long long list[102][102];

int main(){

    cin>>n>>m;

    long long a, b, w;

    for (int i = 1; i <=n; i++)
    {
        for (int j = 1; j <=n; j++)
        {
            list[i][j]=MAX;
        }
    }
    

    for (int i = 0; i < m; i++)
    {
        cin>>a>>b>>w;
        if(w<list[a][b]){
            list[a][b]=w;
        }
        
    }

    for (int k = 1; k <=n; k++)
    {
        for (int s = 1; s <= n; s++)
        {
            for (int e = 1; e <= n; e++)
            {
                list[s][e]=min(list[s][e], list[s][k]+list[k][e]);
            }
            
        }
        
    }
    
    
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if(i==j || list[i][j]==MAX){
                cout<<0<<" ";
            }else{
                cout<<list[i][j]<<" "; 
            }
            
        }
        cout<<endl;
        
    }
    


    return 0;
}