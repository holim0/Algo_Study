#include<iostream>
#include<vector>
#include<algorithm>
#define MAX 987654321;

using namespace std;
int N, M;

int list[105][105];

bool check[105];
int result=987654321;
int idx;

void getSol(){

    
    for (int k = 1; k <=N; k++){
        for(int start=1; start<=N; start++){
            for (int end = 1; end <=N; end++)
            {
                
                list[start][end]=min(list[start][end], list[start][k]+list[k][end]);
                    
            }
            
        }
    }   

    for (int i = 1; i <= N; i++)
    {
        int sum=0;
        for (int j = 1; j<=N; j++)
        {
            if(i==j) continue;
            sum+=list[i][j];
        }
        
        if(result>sum){
            result=sum;
            idx=i;
        }
        
        
    }
    
    


}



int main(){

    cin>>N>>M;

    int a, b;
    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j <=N; j++)
        {
            list[i][j]=MAX;
        }
        
    }

    for (int i = 0; i < M; i++)
    {
        cin>>a>>b;
        list[a][b]=1;
        list[b][a]=1;
    }
    getSol();

    cout<<idx<<endl;    

    return 0;
}