#include<iostream>
#include<queue>

using namespace std;

int N, M;
int result=0;
int map[1001][1001]={0,};
bool check[1001]={false, };

void bfs(){

    queue<int> q;
    

    for(int i=1; i<=N; i++){
        if(!check[i]){
            q.push(i);
            check[i]=true;
            while(!q.empty()){
                int cur=q.front();
                q.pop();
                for (int j = 1; j <=N; j++)
                {
                    if(!check[j] && map[cur][j]==1){
                        check[j]=true;
                        q.push(j);
                    }
                }

            }
            result++;
        }
    }

    while(!q.empty()){

        int cur= q.front();
        q.pop();

        for(int i=1; i<=N; i++){

        }


    }


}


int main(){

    cin>>N>>M;
    
    for (int i = 0; i < M; i++)
    {
        int a,b;
        cin>>a>>b;
        map[a][b]=1;
        map[b][a]=1;
        
    }

    bfs();
    cout<<result<<endl;
    

    return 0;
}