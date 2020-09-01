#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int N, M, K;

int A[105][105];

int map[105][105];



vector<int> tree[105][105];

int dx[]={1, -1, 0, 0, 1, -1, 1, -1};
int dy[]={0, 0, -1, 1, 1, -1, -1, 1};



int result(){

    int cnt=0;
    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=N; j++)
        {
            if(tree[i][j].size()==0) continue;

            cnt+=tree[i][j].size();
        }
        
    }
    return cnt;
}

bool range(int x, int y){

    if(x>0 && x<=N && y>0 && y<=N) return true;

    else return false;
}




void springAndSummer(){

    
    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=N; j++)
        {
            if(tree[i][j].size()==0) continue;

            sort(tree[i][j].begin(), tree[i][j].end());
            vector<int> tmp;
            int val=0;
            for (int k = 0; k < tree[i][j].size(); k++)
            {
                int age=tree[i][j][k];
                if(map[i][j]>=age){
                    map[i][j]-=age;
                    tmp.push_back(age+1);
                }else{
                    val+=age/2;
                }
            }

            tree[i][j].clear();
            for (int k = 0; k < tmp.size(); k++)
            {
                tree[i][j].push_back(tmp[k]);
            }
            map[i][j]+=val;
            
        }
        
    }
    
}


void fall(){

    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=N; j++)
        {   
            if(tree[i][j].size()==0) continue;

            for (int k = 0; k < tree[i][j].size(); k++)
            {
                int age= tree[i][j][k];
                
                if(age%5==0){
                    for (int d = 0; d < 8; d++)
                    {
                        int nx=i+dx[d];
                        int ny=j+dy[d];
                        if(range(nx, ny)){
                            tree[nx][ny].push_back(1);
                        }
                    }
                    
                }
            }
            
        }
        
    }

}

void winter(){

    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=N; j++)
        {
            map[i][j]+=A[i][j];
        }
        
    }
    

}

void year(){

    springAndSummer();
    fall();
    winter();
}



int main(){

    cin>>N>>M>>K;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <=N; j++)
        {
            cin>>A[i][j];
            map[i][j]=5;
        }
    }

    for (int i = 0; i < M; i++)
    {
        int x, y, age;
        cin>>x>>y>>age;
        tree[x][y].push_back(age);
    }
    

    for (int i = 0; i < K; i++)
    {   
        year();
    }

    
    cout<<result()<<endl;

    return 0;
}