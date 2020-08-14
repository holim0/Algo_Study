#include<iostream>

using namespace std;
int n, m;
int map[1026][1026];
int main(){

    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n>>m;
    
    for (int i = 1; i <=n; i++)
    {
        for (int j = 1; j <=n; j++)
        {
            cin>>map[i][j];
        }
    }

    for (int i = 1; i <=n; i++)
    {
        for (int j = 1; j <=n; j++)
        {
            map[i][j]+=map[i][j-1];
        }
    }

    for (int i = 0; i < m; i++)
    {
        int x1, y1, x2, y2;
        cin>>x1>>y1>>x2>>y2;
        
        int sum=0;
        
        for (int i = x1; i <=x2; i++)
        {
            if(y1>1){
                sum+=map[i][y2]-map[i][y1-1];
            }else{
                sum+=map[i][y2];
            }
            
        }
        cout<<sum<<'\n';

    }
    
    
    

    return 0;
}