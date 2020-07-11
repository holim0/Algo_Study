#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>


using namespace std;

int N, M, D;
int enmap[18][18];
vector<int> pos;
int allpos[18];
bool check[18]={false, };
int copymap[18][18];
int catchval=-1;
bool checkEnemy[18][18]={false, };

int cnt=0;

void move(){

    for(int i=N-1; i>=1; i--){
        for(int j=0; j<M; j++){
            copymap[i][j]=copymap[i-1][j];
            copymap[i-1][j]=0;
        }
    }

    
}

bool isdone(){
    
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(copymap[i][j]==1) return false;
        }
    }

    return true;
}


void Copy_MAP()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            copymap[i][j] = enmap[i][j];
        }
    }

    
}

bool positionSort(pair<int, pair<int, int>> &a, pair<int, pair<int, int>> &b){
    if(a.first==b.first){
        return a.second.second<b.second.second;
    }
    return a.first<b.first;
}

pair<int, int> whoAttack(int x){
    int dist;
    int idx1, idx2;  bool findtar=false;
    int minitarget=987654321;
    vector<pair<int, pair<int, int>>> v;
    for (int i = N-1; i>=0; i--)
    {
        for(int j=0; j<M; j++){
            if(copymap[i][j]==1){
                dist= abs(N-i)+abs(x-j);
                if(dist<=D){
                    findtar=true;
                    v.push_back({dist, {i, j}});
                }
            }
        }
    }

    if(findtar){
        sort(v.begin(), v.end(),positionSort);
        return {v[0].second.first, v[0].second.second};
    } 
    else return {-1, -1};



}


void getE(int n1, int n2, int n3){
    
    int round=0; 
    pair<int, int> p[3];
    while(round<N){
        memset(checkEnemy, false, sizeof(checkEnemy));
        p[0]=whoAttack(n1);
        p[1]=whoAttack(n2);
        p[2]=whoAttack(n3);
        // cout<<"position: ";
        // cout<<p[0].first<<p[0].second<<endl;
        // cout<<p[1].first<<p[1].second<<endl;
        // cout<<p[2].first<<p[2].second<<endl;

        for(int i=0; i<3; i++){
            if(p[i].first==-1 || p[i].second==-1) continue;
            else{
                if(!checkEnemy[p[i].first][p[i].second]){
                    checkEnemy[p[i].first][p[i].second]=true;
                    copymap[p[i].first][p[i].second]=0;
                    cnt++;
                }
            }
        }
        // cout<<"after shoot cnt:"<<endl;
        // cout<<cnt<<endl;
        // cout<<"after shoot map:"<<endl;
        // for(int i=0; i<N; i++){
        //     for(int j=0; j<M; j++){
        //         cout<<copymap[i][j]<<" ";
        //     }
        //     cout<<'\n';
        // }
        
        
        move();
        if(isdone()){
            // cout<<"cnt:" <<cnt<<endl;
            catchval = cnt > catchval ? cnt : catchval;
            return;
        }
    //     cout<<"After move:"<<endl;
    // for(int i=0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         cout<<copymap[i][j]<<" ";
    //     }
    //         cout<<'\n';
    //     }
        
        
        round++;
    }    

    

    



    

}

void getPos(int cnt1, int start){
    if(cnt1==3){
        Copy_MAP();
        cnt=0;
        // cout<<"original map:"<<endl;
        // for(int i=0; i<N; i++){
        //     for(int j=0; j<M; j++){
        //         cout<<copymap[i][j]<<" ";
        //     }
        //     cout<<'\n';
        // }
        // cout<<pos[0]<<pos[1]<<pos[2]<<endl;
        getE(pos[0], pos[1], pos[2]);
        // cout<<catchval<<endl;
        return;
    }

    for(int i=start; i<M; i++){
        if(!check[i]){
            check[i]=true;
            pos.push_back(allpos[i]);
            getPos(cnt1+1, i);
            check[i]=false;
            pos.pop_back();
        }
    }
    



}


int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    cin>>N>>M>>D;

    memset(enmap, -1, sizeof(enmap));

    for(int i=0; i<N; i++){
        for(int j=0; j< M; j++){
            cin>>enmap[i][j];
        }
    }

    for(int i=0; i<M; i++){
        allpos[i]=i;
    }

    getPos(0, 0);
    
    
    cout<<catchval<<endl;

    return 0;
}