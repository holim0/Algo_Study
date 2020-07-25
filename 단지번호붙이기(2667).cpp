#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int total=0;

int map[27][27];
int N;
int dx[]={1, -1, 0, 0};
int dy[]={0, 0, -1, 1};

bool check[27][27]={false, };
queue<pair<int, int>> q;
vector<int> v;

bool Range(int x, int y){

    if(x>=0 && x<N && y>=0 && y<N) return true;
    else return false;

}



int main(){

    cin>>N;

    for (int i = 0; i < N; i++)
    {   
        string s;
        cin>>s;
        for (int j = 0; j < N; j++)
        {
            map[i][j]=s[j]-'0';
        }
    }
    int home=0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(map[i][j]==1 && !check[i][j]){
                q.push({i, j}); check[i][j]=true; home++;
                while(!q.empty()){
                    int curx=q.front().first;
                    int cury=q.front().second;
                    q.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx=curx+dx[k]; int ny=cury+dy[k];
                        if(!check[nx][ny] && map[nx][ny]==1 && Range(nx, ny)){
                            q.push({nx, ny}); home++;
                            check[nx][ny]=true;
                        }
                    }
                }
                v.push_back(home);
                home=0;
                total++;
            }
        }
        
    }


    cout<<total<<endl;

    
    sort(v.begin(), v.end());

    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<'\n';
    }
    
    
    


    return 0;
}