#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;
int map[25][25];
int numbering[25][25];
int dist[11]={0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
bool checkdist[11]={false, };
int N;

int result=987654321;

bool flag=true;

vector<int> tmpdist;   // 거리 조합 저장 벡터.
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

bool range(int x, int y){

    if(x>=1 && x<=N && y>=1 && y<=N) return true;
    else return false;
}

int bfs(int num){

    bool ch[25][25]={false, };
    int sum=0;
    queue<pair<int, int>> q;
    
    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if(!ch[i][j] && numbering[i][j]==num){
                ch[i][j]=true;
                q.push({i, j}); sum+=map[i][j];
                while(!q.empty()){
                    int curx=q.front().first; int cury=q.front().second;
                    //cout<<curx<<cury<<endl;
                    q.pop();

                    for(int k=0; k<4; k++){
                        int nx=curx+dx[k]; int ny=cury+dy[k];
                        if(num==5){
                            if(range(nx, ny) && !ch[nx][ny] && (numbering[nx][ny]==5 || numbering[nx][ny]==0)){
                                ch[nx][ny]=true;
                                q.push({nx, ny}); sum+=map[nx][ny];
                            }
                        }else{
                            if(range(nx, ny) && !ch[nx][ny] && numbering[nx][ny]==num){
                                ch[nx][ny]=true;
                                q.push({nx, ny}); sum+=map[nx][ny];
                            }
                        }
                    }
                }
            }
        }
        
    }

    return sum;
}

bool checkDist(int x, int y, int d1, int d2){

    if(x+d1+d2<=N && y-d1>=1 && y+d2<=N) return true;
    else return false;
}

void selectArea(int basex, int basey, int d1, int d2){
    
    if(!checkDist(basex, basey, d1, d2)){
        flag=false;
        return;
    }
    memset(numbering, 0, sizeof(numbering));


    int idx=basex; int idx2=basey;

    while(1){

        numbering[idx][idx2]=5;
        numbering[idx+d2][idx2+d2]=5;
        idx++;
        idx2--;
        if(idx>basex+d1 || idx2<basey-d1) break;
    }
    idx=basex; idx2=basey;
    while(1){
        
        numbering[idx][idx2]=5;
        numbering[idx+d1][idx2-d1]=5;
        idx++;
        idx2++;
        if(idx>basex+d2 || idx2>basey+d2) break;
    }

    ///////////////////////////////////////////////////////////

    //number1//

    for (int i = 1; i < basex+d1; i++)
    {
        for (int j = 1; j <=basey; j++)
        {   
            if(numbering[i][j]==5) break;
            numbering[i][j]=1;
        }
    }

    //number2//

    
        for (int j = basey+1; j <=N; j++)
        {
            for(int i=1; i<=basex+d2; i++){
                if(numbering[i][j]==5) break;
                numbering[i][j]=2;
            }
        }
        
    

    // //number3 //

    for (int i = basex+d1; i <=N; i++)
    {
        for (int j = 1; j < basey-d1+d2; j++)
        {
            if(numbering[i][j]==5) break;
            numbering[i][j]=3;
        }
        
    }
    
    for (int i =basex+d2+1; i <=N; i++)
    {
        for (int j =N; j>=basey-d1+d2; j--)
        {
            if(numbering[i][j]==5) break;
            numbering[i][j]=4;
        }
        
    }

}


void distJohab(int cnt){
    if(cnt==2){
        int n1, n2;
        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {  
                flag=true; n1=-1; n2=987654321;
                selectArea(i, j, tmpdist[0], tmpdist[1]);
                if(flag){   
                    for (int k = 1; k <= 5; k++)
                    {   
                        int val=bfs(k);
                        
                        n1=max(val, n1);
                        n2=min(val, n2);
                        
                        
                    }
                    result=min(result, n1-n2);
                }
                
            }
            
        }
        return;
    }
        for (int i = 1; i <=10; i++)
        {
            if(!checkdist[i]){
                tmpdist.push_back(i);
                distJohab(cnt+1);
                tmpdist.pop_back();
            }
        }
        

}




int main(){

    cin>>N;

    for (int i = 1; i <=N; i++)
    {
        for (int j = 1; j <=N; j++)
        {
            cin>>map[i][j];
        }
    }
    
    distJohab(0);


    cout<<result<<endl;
    return 0;
}