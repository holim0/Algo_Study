#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;
#define MAX 102
int map[MAX][MAX];

int r, c, k;

int resulttime=0;



bool vsort(pair<int, int> &a, pair<int, int> &b){

    if(a.second==b.second){
        return a.first<b.first;
    }
    return a.second<b.second;

}

int calR(int sero, int garo){
    int checkcnt[102];
    bool checknum[102]={false, };
    vector<pair<int, int>> tmp;
    int maxgaro=-1;
    bool over=false;
    for(int i=1; i<=sero; i++){
        tmp.clear();
        memset(checknum, false, sizeof(checknum));
        memset(checkcnt, 0, sizeof(checkcnt));
        for (int j = 1; j <=garo; j++)
        {
            if(map[i][j]!=0) checkcnt[map[i][j]]++;
        }

        for(int j=1; j<=garo; j++){
            if(checkcnt[map[i][j]]>0 && !checknum[map[i][j]]){
                checknum[map[i][j]]=true;
                tmp.push_back({map[i][j], checkcnt[map[i][j]]});
            }
        }
        sort(tmp.begin(), tmp.end(), vsort);
        
        for(int k=0; k<MAX; k++){     //0 으로 초기화.
            map[i][k]=0;
        }
        int idx=1; 
        for(int j=0; j<tmp.size(); j++){
            map[i][idx]=tmp[j].first;
            map[i][idx+1]=tmp[j].second;
            idx+=2;
            if(idx>100) {
                over=true;
                break;
            }
        }
        
        maxgaro=max(maxgaro, idx);
    }
    if(over) return 100;
    //cout<<maxgaro<<endl;
    return maxgaro-1;
}

int calC(int sero, int garo){
    int checkcnt[102];
    bool checknum[102]={false, };
    vector<pair<int, int>> tmp;
    int maxsero=-1;
    bool over=false;
    for(int i=1; i<=garo; i++){
        tmp.clear();
        memset(checknum, false, sizeof(checknum));
        memset(checkcnt, 0, sizeof(checkcnt));
        for (int j = 1; j <=sero; j++)
        {
            if(map[j][i]!=0) checkcnt[map[j][i]]++;
        }

        for(int j=1; j<=sero; j++){
            if(checkcnt[map[j][i]]>0 && !checknum[map[j][i]]){
                checknum[map[j][i]]=true;
                tmp.push_back({map[j][i], checkcnt[map[j][i]]});
            }
        }
        sort(tmp.begin(), tmp.end(), vsort);
        
        for(int k=0; k<MAX; k++){     //0 으로 초기화.
            map[k][i]=0;
        }
        int idx=1; 
        for(int j=0; j<tmp.size(); j++){
            map[idx][i]=tmp[j].first;
            map[idx+1][i]=tmp[j].second;
            idx+=2;
            if(idx>100) {
                over=true;
                break;
            }
        }

        maxsero=max(maxsero, idx);
    }

    if(over) return 100;
    //cout<<maxgaro<<endl;
    return maxsero-1;

}

void go(int sero, int garo){

    if(sero>=garo){
        int newgaro=calR(sero, garo);
        resulttime++;
        if(resulttime>100){
            cout<<-1<<endl;
            return;
        }
        // cout<<"after R: "<<endl;
        // for(int i=1; i<=sero; i++){
        //     for(int j=1; j<=newgaro; j++){
        //         cout<<map[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        if(map[r][c]==k) return;
        go(sero, newgaro);

    }else{
        int newsero=calC(sero, garo);
        resulttime++;
        if(resulttime>100){
            cout<<-1<<endl;
            return;
        }
        // cout<<"after C: "<<endl;
        // for(int i=1; i<=newsero; i++){
        //     for(int j=1; j<=garo; j++){
        //         cout<<map[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
        if(map[r][c]==k) return;
        go(newsero, garo);

        
    }


}
int main(){

    cin>>r>>c>>k;   int val;

    for(int i=1; i<=3; i++){
        for (int j = 1; j <= 3; j++)
        {
        cin>>val;
        map[i][j]=val;
        }
    }
    
    if(map[r][c]==k){
        cout<<0<<endl;
        return 0;
    }
    go(3, 3);
    

    if(resulttime<=100){

        cout<<resulttime<<endl;
    }



    return 0;
}