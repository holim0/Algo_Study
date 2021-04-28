#include<iostream>
#include<vector>
#include<queue>
#define MAX 1000+5
#define INF 987654321
using namespace std;

int N, M;
vector<pair<int, int>> v[MAX];
int dist[MAX];
int main(){

    cin>>N>>M;
    int s, e, w;
    priority_queue<pair<int, int>> pq;

    for (int i = 0; i < M; i++)
    {
        cin>>s>>e>>w;
        v[s].push_back({w, e});
    }


    int start, end;
    cin>>start>>end;

    for (int i = 0; i < MAX; i++)
    {
        dist[i]=INF;
    }


    dist[start]=0;

    pq.push({0, start});

    while(!pq.empty()){
        int cur=pq.top().second;
        int weight= -pq.top().first;
        pq.pop();
        
        if(weight>dist[cur]) continue;

        for (int i = 0; i < v[cur].size(); i++)
        {
            int next=v[cur][i].second;
            
            int nextDist=v[cur][i].first+dist[cur];

            if(nextDist<dist[next]){
                dist[next]=nextDist;
                pq.push({-nextDist, next});
            }
        }
    }


    cout<<dist[end]<<endl;

    




    





    return 0;
}