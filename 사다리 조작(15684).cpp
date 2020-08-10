#include<iostream>
#include<algorithm>

using namespace std;
int N, M, H;
int con[35][11][11];
bool check[35][12][12];
int result= 100;
int move(int cur, int h){

    bool flag=false;
    int next, nexth;
    for (int i = h; i <=H; i++)
    {
        if(con[i][cur][cur+1]==1){
            next=cur+1;
            nexth=i+1;
            flag=true;
            break;
        }else if(con[i][cur][cur-1]==1){
            next=cur-1;
            nexth=i+1;
            flag=true;
            break;
        }
    }
    
    if(flag){
        return move(next, nexth);
    }
    else{
        return cur;
    }
    
    
    

}

bool done(){

    for (int i = 1; i <= N; i++)
    {
        int dest=move(i, 1);
        if(i!=dest) return false;
    }
    
    return true;
    
}
void go(int cnt, int limit){


    if(cnt==limit){
        if(done()){
            result=min(cnt, result);
            return;
        }
        return;
    }


    for (int h = 1; h <= H; h++)
    {
        for (int n = 1; n < N; n++)
        {
            if(!check[h][n][n+1] && con[h][n][n+1]==0){
                con[h][n][n+1]=1; con[h][n+1][n]=1;
                check[h][n][n+1]=true; check[h][n+1][n]=true;
                check[h][n-1][n]=true; check[h][n][n-1]=true;
                check[h][n+1][n+2]=true; check[h][n+2][n+1]=true;
                go(cnt+1, limit);
                con[h][n][n+1]=0; con[h][n+1][n]=0;
                check[h][n][n+1]=false; check[h][n+1][n]=false;
                check[h][n-1][n]=false; check[h][n][n-1]=false;
                check[h][n+1][n+2]=false; check[h][n+2][n+1]=false;
            }
        }
        
    }
    



}

int main(){
    
    cin>>N>>M>>H;

    int a, b;

    for (int i = 0; i < M; i++)
    {
        cin>>a>>b;
        con[a][b][b+1]=1;
        con[a][b+1][b]=1;
        check[a][b][b+1]=true;
        check[a][b+1][b]=true;
        if(b+2<=N){
            check[a][b+1][b+2]=true;
            check[a][b+2][b+1]=true;
        }

        if(b-1>0){
            check[a][b-1][b]=true;
            check[a][b][b-1]=true;        
        }
        
    }
    
    
    if(done()){
        cout<<0<<endl;
        return 0;
    }

    for (int i = 1; i <= 3; i++)
    {
        go(0, i);
    }

    if(result==100){
        cout<<-1<<endl;
    }else{
        cout<<result<<endl;
    }
    
    return 0;
}